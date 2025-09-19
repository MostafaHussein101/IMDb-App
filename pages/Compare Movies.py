import streamlit as st 
import pandas as pd 
import plotly_express as px
import Helper 

st.set_page_config(layout="wide")
df = Helper.load_data() 
Helper.Nav_Bar() 

def clean_runtime(runtime):
    if pd.isna(runtime):
        return 0
    if isinstance(runtime, str):
        return int(''.join(filter(str.isdigit, runtime)))
    return int(runtime)

df['Runtime_Clean'] = df['Runtime'].apply(clean_runtime)

st.header("🎬 Movie Comparison Tool")
m1, m2 = st.columns(2)

def movie_selector(column, label):
    with column:
        search = st.text_input(f"🔎 Search for {label}", key=f"search_{label}")
        if st.checkbox("Use filters", key=f"filter_{label}"):
            exclude = ["Poster_Link",'Overview',"Gross","Number of votes"]
            columns = [col for col in df.columns if col not in exclude]
            option1 = st.selectbox("Filter by", columns, key=f"filter1_{label}")
            option2 = st.selectbox("Filter value", df[option1].dropna().unique(), key=f"filter2_{label}")
            filtered_df = df[df[option1] == option2]
        else:
            filtered_df = df
        
        if search:  
            results = filtered_df[
                filtered_df['Movie Title'].str.contains(search, case=False, na=False)
                | filtered_df['Genre'].str.contains(search, case=False, na=False)
                | filtered_df['Director'].str.contains(search, case=False, na=False)
                | filtered_df['Released Year'].astype(str).str.contains(search, case=False, na=False)
            ]
        else:  
            results = filtered_df
        
        movie_titles = results['Movie Title'].tolist()
        selected_movie = st.selectbox(f"Select {label} movie", movie_titles, key=f"select_{label}")
        return selected_movie

movie1 = movie_selector(m1, "first")
movie2 = movie_selector(m2, "second")

if movie1 and movie2:
    st.write("---")
    comp1, comp2 = st.columns(2)
    
    for col, movie in zip([comp1, comp2], [movie1, movie2]):
        with col:
            row = df[df['Movie Title'] == movie].iloc[0]
            st.image(row['Poster_Link'], width=300)
            st.markdown(f"### **{row['Movie Title']}**")
            st.markdown(f"**📅 Year:** {row['Released Year']}")
            st.markdown(f"**⭐ IMDB Rating:** {row['IMDB Rating']}")
            st.markdown(f"**📊 Meta Score:** {row['Meta score']}")
            st.markdown(f"**⏱️ Runtime:** {row['Runtime']} minutes")
            st.markdown(f"**🎭 Genre:** {row['Genre']}")
            st.markdown(f"**🎬 Director:** {row['Director']}")
            st.markdown(f"**👥 Cast:** {row['Star1']}, {row['Star2']}, {row['Star3']}, {row['Star4']}")
            st.markdown(f"**💲 Gross:** ${row['Gross']:,.0f}" if pd.notna(row['Gross']) else "**💲 Gross:** N/A")
            st.markdown(f"**🗳️ Votes:** {row['Number of votes']:,.0f}")
            st.markdown(f"**📝 Story:** {row['Overview']}")
    
    st.write("---")
    st.subheader("📊 Comparison Metrics")
    
    row1 = df[df['Movie Title'] == movie1].iloc[0]
    row2 = df[df['Movie Title'] == movie2].iloc[0]
    
    metrics = [
        ('IMDB Rating', '⭐ IMDB Rating'),
        ('Meta score', '📊 Meta Score'), 
        ('Runtime_Clean', '⏱️ Runtime (minutes)'),
        ('Gross', '💲 Gross ($)'),
        ('Number of votes', '🗳️ Number of Votes')
    ]
    
    comparison_data = []
    for metric, display_name in metrics:
        if metric == 'Runtime_Clean':
            val1 = row1['Runtime'] if pd.notna(row1['Runtime']) else "N/A"
            val2 = row2['Runtime'] if pd.notna(row2['Runtime']) else "N/A"
        else:
            val1 = row1[metric] if pd.notna(row1[metric]) else 0
            val2 = row2[metric] if pd.notna(row2[metric]) else 0
        comparison_data.append({'Metric': display_name, movie1: val1, movie2: val2})
    
    comp_df = pd.DataFrame(comparison_data).set_index('Metric')
    st.dataframe(comp_df, use_container_width=True)
    
    st.subheader("📈 Individual Metric Comparisons")
    
    for metric, display_name in metrics:
        metric_data = pd.DataFrame({
            'Movie': [movie1, movie2],
            'Value': [
                row1[metric] if pd.notna(row1[metric]) else 0,
                row2[metric] if pd.notna(row2[metric]) else 0
            ]
        })
        
        fig = px.bar(
            metric_data, 
            x='Movie', 
            y='Value', 
            title=f"{display_name} Comparison",
            color='Movie',
            text='Value'
        )
        
        if metric == 'Gross':
            fig.update_layout(yaxis_tickprefix='$', yaxis_tickformat=',.0f')
            fig.update_traces(texttemplate='$%{text:,.0f}')
        elif metric == 'Number of votes':
            fig.update_layout(yaxis_tickformat=',.0f')
            fig.update_traces(texttemplate='%{text:,.0f}')
        elif metric == 'Runtime_Clean':
            fig.update_traces(texttemplate='%{text} mins')
        else:
            fig.update_traces(texttemplate='%{text:.1f}')
        
        st.plotly_chart(fig, use_container_width=True)