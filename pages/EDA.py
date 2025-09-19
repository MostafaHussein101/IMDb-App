import streamlit as st 
import pandas as pd 
import numpy as np
import plotly_express as px
import Helper 

# Page setup
st.set_page_config(layout="wide")
df = Helper.load_data() 
Helper.Nav_Bar() 

st.title("📊 IMDB 1000 Movies EDA")
st.write("---")

# ==============================
# Movies Ranking Plot
# ==============================
st.header("🎬 Movies Ranking Plot")

col1, col2 = st.columns(2)

with col1:
    x = st.select_slider("Select the number of movies to display", range(1, 51), value=10)

with col2:
    exclude = ["Movie Title", "Poster_Link", "Overview","Director","Star1","Star2","Star3","Star4",
               'Released Year','Genre',"Certificate","Runtime"]
    columns = [col for col in df.columns if col not in exclude]
    Y = st.selectbox("Select your category", columns)

TOB = st.toggle("Top (ON) or Bottom (OFF)")

# Sort dataframe
if TOB:
    sorted_df = df.sort_values(Y, ascending=False)
    title_prefix = "Top"
else:
    sorted_df = df.sort_values(Y, ascending=True)
    title_prefix = "Bottom"

# Display chart
st.subheader(f"{title_prefix} {x} Movies by {Y}")

fig = px.bar(
    sorted_df.head(x),
    x="Movie Title",
    y=Y,
    color=Y,
    color_continuous_scale=px.colors.sequential.Blues,
    height=600
)

st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Genre Distribution
# ==============================
st.header("🎭 Distribution of Movies by Genre")

genre_split = df["Genre"].dropna().str.split(", ")
genre_exploded = genre_split.explode()

genre_counts = genre_exploded.value_counts().reset_index()
genre_counts.columns = ["Genre", "Count"]

fig = px.pie(
    genre_counts,
    names="Genre",
    values="Count",
    hole=0.11 
)

st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Movies Growth by Year
# ==============================
st.header("📈 Movies Growth Over the Years")

movies_per_year = df["Released Year"].value_counts().reset_index()
movies_per_year.columns = ["Year", "Movie Count"]

movies_per_year = movies_per_year.sort_values("Year")

fig = px.line(
    movies_per_year,
    x="Year",
    y="Movie Count",
    markers=True 
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Ratings Distribution
# ==============================
st.header("⭐ IMDB Rating Distribution")

fig = px.histogram(
    df,
    x="IMDB Rating",
    nbins=20,
    title="Distribution of IMDB Ratings",
    color_discrete_sequence=["#636EFA"]
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Average Gross by Genre
# ==============================
st.header("💲 Average Gross by Genre")

avg_gross = df.dropna(subset=["Gross", "Genre"])
avg_gross["Genre"] = avg_gross["Genre"].str.split(", ").str[0]  # take only first genre
genre_gross = avg_gross.groupby("Genre")["Gross"].mean().reset_index()

fig = px.bar(
    genre_gross.sort_values("Gross", ascending=False),
    x="Genre",
    y="Gross",
    title="Average Gross per Genre",
    color="Gross",
    color_continuous_scale=px.colors.sequential.Viridis
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Top Directors by Number of Movies
# ==============================
st.header("🎥 Top Directors by Number of Movies")

director_counts = df["Director"].value_counts().reset_index().head(10)
director_counts.columns = ["Director", "Movie Count"]

fig = px.bar(
    director_counts,
    x="Director",
    y="Movie Count",
    title="Directors with Most Movies in Dataset",
    color="Movie Count",
    color_continuous_scale=px.colors.sequential.Magma
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Correlation Heatmap
# ==============================
st.header("🔗 Correlation Between Numerical Features")

numeric_df = df.select_dtypes(include="number")

fig = px.imshow(
    numeric_df.corr(),
    text_auto=True,
    title="Correlation Heatmap",
    color_continuous_scale="RdBu_r"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Certificates Distribution
# ==============================
st.header("🎟️ Distribution of Movie Certificates")

cert_counts = df["Certificate"].value_counts().reset_index()
cert_counts.columns = ["Certificate", "Count"]

fig = px.pie(
    cert_counts,
    names="Certificate",
    values="Count",
    hole=0.15,
    title="Movie Certificates"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")
# ==============================
# Runtime Distribution
# ==============================
st.header("⏱️ Runtime Distribution")

fig = px.histogram(
    df,
    x="Runtime",
    nbins=30,
    title="Distribution of Movie Runtimes",
    color_discrete_sequence=["#00CC96"]
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Top Actors by Number of Movies
# ==============================
st.header("👥 Top Actors by Number of Movies")

all_actors = pd.concat([df["Star1"], df["Star2"], df["Star3"], df["Star4"]])
actor_counts = all_actors.value_counts().reset_index().head(15)
actor_counts.columns = ["Actor", "Movie Count"]

fig = px.bar(
    actor_counts,
    x="Actor",
    y="Movie Count",
    title="Actors with Most Movies in Dataset",
    color="Movie Count",
    color_continuous_scale="Tealgrn"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Gross vs IMDB Rating
# ==============================
st.header("💵 Gross vs ⭐ IMDB Rating")

fig = px.scatter(
    df.dropna(subset=["Gross", "IMDB Rating"]),
    x="IMDB Rating",
    y="Gross",
    size="Number of votes",
    color="Genre",
    title="Gross vs IMDB Rating (Bubble Size = Votes)"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Average IMDB Rating per Year
# ==============================
st.header("📊 Average IMDB Rating per Year")

avg_rating_year = df.groupby("Released Year")["IMDB Rating"].mean().reset_index()

fig = px.line(
    avg_rating_year,
    x="Released Year",
    y="IMDB Rating",
    markers=True,
    title="Average IMDB Rating Over the Years"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Top Genres by Average Rating
# ==============================
st.header("🎭 Top Genres by Average IMDB Rating")

genre_split = df["Genre"].dropna().str.split(", ")
genre_exploded = df.loc[df["Genre"].notna()].copy()
genre_exploded = genre_exploded.assign(Genre=genre_exploded["Genre"].str.split(", ")).explode("Genre")

avg_genre_rating = genre_exploded.groupby("Genre")["IMDB Rating"].mean().reset_index()

fig = px.bar(
    avg_genre_rating.sort_values("IMDB Rating", ascending=False).head(15),
    x="Genre",
    y="IMDB Rating",
    title="Top 15 Genres by Average IMDB Rating",
    color="IMDB Rating",
    color_continuous_scale="Sunset"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Meta Score Distribution
# ==============================
st.header("📑 Meta Score Distribution")

fig = px.histogram(
    df.dropna(subset=["Meta score"]),
    x="Meta score",
    nbins=20,
    title="Distribution of Meta Scores",
    color_discrete_sequence=["#AB63FA"]
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")
# ==============================
# Top Certificates by Average Rating
# ==============================
st.header("🎟️ Certificates by Average IMDB Rating")

cert_rating = df.groupby("Certificate")["IMDB Rating"].mean().reset_index().dropna()

fig = px.bar(
    cert_rating.sort_values("IMDB Rating", ascending=False),
    x="Certificate",
    y="IMDB Rating",
    title="Average IMDB Rating by Certificate",
    color="IMDB Rating",
    color_continuous_scale="Aggrnyl"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Votes Distribution
# ==============================
st.header("🗳️ Number of Votes Distribution")

fig = px.histogram(
    df,
    x="Number of votes",
    nbins=40,
    title="Distribution of Number of Votes",
    color_discrete_sequence=["#EF553B"]
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Top 10 Directors by Gross
# ==============================
st.header("🎬 Top 10 Directors by Total Gross")

directors_gross = df.dropna(subset=["Gross"]).groupby("Director")["Gross"].sum().reset_index()
directors_gross = directors_gross.sort_values("Gross", ascending=False).head(10)

fig = px.bar(
    directors_gross,
    x="Director",
    y="Gross",
    title="Top Directors by Total Gross",
    color="Gross",
    color_continuous_scale="Plasma"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Average Gross per Actor
# ==============================
st.header("💰 Actor Star Power (Avg Gross)")

all_actors = pd.concat([df["Star1"], df["Star2"], df["Star3"], df["Star4"]])
actors_gross = all_actors.dropna().reset_index()
actors_gross.columns = ["Index", "Actor"]

actor_avg_gross = df.melt(id_vars=["Gross"], value_vars=["Star1", "Star2", "Star3", "Star4"], var_name="Role", value_name="Actor")
actor_avg_gross = actor_avg_gross.dropna().groupby("Actor")["Gross"].mean().reset_index().sort_values("Gross", ascending=False).head(15)

fig = px.bar(
    actor_avg_gross,
    x="Actor",
    y="Gross",
    title="Actors with Highest Average Gross",
    color="Gross",
    color_continuous_scale="Viridis"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")

# ==============================
# Runtime vs Rating Scatter
# ==============================
st.header("⏳ Runtime vs ⭐ IMDB Rating")

fig = px.scatter(
    df,
    x="Runtime",
    y="IMDB Rating",
    size="Number of votes",
    color="Genre",
    title="Runtime vs IMDB Rating"
)
st.plotly_chart(fig, use_container_width=True)
st.write("---")
