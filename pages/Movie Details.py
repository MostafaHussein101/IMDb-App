import streamlit as st 
import Helper 
st.set_page_config(layout="wide")

df = Helper.load_data() 
Helper.Nav_Bar() 


search = st.text_input("🔎 Search for a movie Name | Genre | Director | Year")

if st.checkbox("Narrow the search using filters"):
    exclude = ["Poster_Link",'Overview',"Gross","Number of votes"]
    columns = [col for col in df.columns if col not in exclude]
    option1 = st.selectbox("Movie Filter", columns)
    if option1:
        option2 = st.selectbox("Choose your filter", df[option1].dropna().unique())
        filtered_df = df[df[option1] == option2]
    else:
        filtered_df = df
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


if not results.empty:
    for _, row in results.iterrows():
        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(row['Poster_Link'], width=300)

        with col2:
            st.markdown(f"### **{row['Movie Title']}**")
            st.markdown(f"**📅 Year:** {row['Released Year']}")
            st.markdown(f"**⏳ Run-Time:** {row['Runtime']}")
            st.markdown(f"**⭐ IMDB Rating:** {row['IMDB Rating']}")
            st.markdown(f"**🎭 Genre:** {row['Genre']}")
            st.markdown(f"**🎬 Director:** {row['Director']}")
            st.markdown(f"**👥 Cast:** {row['Star1']}, {row['Star2']}, {row['Star3']}, {row['Star4']}")
            st.markdown(f"**💲 Gross:** {row['Gross']}$")
            st.markdown(f"**📝 Story:** {row['Overview']}")

        st.write("---")
else:
    st.warning("No movies found. Try another input.")
