import streamlit as st
import Helper

st.set_page_config(layout="wide")

# Load data
df = Helper.load_data()
Helper.Nav_Bar()

st.title("🔍 IMDB Insights")
st.write("Here are some key insights from the IMDB Top 1000 Movies dataset.")
st.write("---")

# 1. Dataset size
st.subheader("📂 Dataset Overview")
st.write(f"- Total movies in dataset: **{df.shape[0]}**")
st.write(f"- Total columns (features): **{df.shape[1]}**")

# 2. Ratings
st.subheader("⭐ IMDB Ratings")
st.write(f"- Average IMDB Rating: **{df['IMDB Rating'].mean():.2f}/10**")
st.write(f"- Highest rated movie: **{df.loc[df['IMDB Rating'].idxmax(), 'Movie Title']}** ({df['IMDB Rating'].max()}/10)")
st.write(f"- Lowest rated movie: **{df.loc[df['IMDB Rating'].idxmin(), 'Movie Title']}** ({df['IMDB Rating'].min()}/10)")

# 3. Genres
st.subheader("🎭 Genres")
st.write(f"- Most common genre: **{df['Genre'].mode()[0]}**")
st.write(f"- Unique genres count: **{df['Genre'].nunique()}**")

# 4. Directors
st.subheader("🎬 Directors")
top_director = df['Director'].value_counts().idxmax()
st.write(f"- Director with the most movies: **{top_director}** ({df['Director'].value_counts().max()} movies)")

# 5. Release Years
st.subheader("📅 Release Years")
st.write(f"- Oldest movie: **{df.loc[df['Released Year'].idxmin(), 'Movie Title']}** ({df['Released Year'].min()})")
st.write(f"- Newest movie: **{df.loc[df['Released Year'].idxmax(), 'Movie Title']}** ({df['Released Year'].max()})")

# 6. Earnings
st.subheader("💰 Gross Earnings")
st.write(f"- Average gross earnings: **${df['Gross'].mean():,.0f}**")
st.write(f"- Highest grossing movie: **{df.loc[df['Gross'].idxmax(), 'Movie Title']}** (${df['Gross'].max():,.0f})")
st.write(f"- Lowest grossing movie: **{df.loc[df['Gross'].idxmin(), 'Movie Title']}** (${df['Gross'].min():,.0f})")

st.write("---")
