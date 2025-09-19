import streamlit as st 
import numpy as np
import Helper 

st.set_page_config(layout="wide")

df = Helper.load_data() 
df = df.replace("", np.nan)

Helper.Nav_Bar() 

st.title("Welcome to IMDB Top 1000 movies EDA")
st.markdown(""" 
This project analyzes one of the most popular movie datasets containing information on the **Top 1000 IMDB-rated movies and TV shows**.  
It includes details such as movie titles, release years, IMDB ratings, genres, directors, actors, runtime, gross earnings, audience votes, and more.  

Using **Streamlit and Plotly**, this dashboard provides:
- Interactive visualizations for exploring trends in ratings, votes, gross, runtime, and genres.  
- Comparative insights into directors, actors, and certificates.  
- Key statistics and correlations to understand what drives popularity and success in movies.  

The goal of this project is to make data exploration **simple, visual, and fun** for movie lovers, researchers, and data enthusiasts alike.
""")
st.info("Hover to see a brief about the movie") 

p1,p2,p3,p4,p5,p6,p7,p8,p9,p10 = st.tabs(["Page 1","Page 2","Page 3","Page 4","Page 5","Page 6","Page 7","Page 8","Page 9","Page 10"])

df['poster_html'] = df.apply(lambda row: f'<img src="{row["Poster_Link"]}" title="{row["Movie Title"]} \n Rating: ({row["IMDB Rating"]}/10) \n Genre: {row["Genre"]} \n Director: {row["Director"]}" width="200" style="border-radius: 8px;">', axis=1)
def images(p, k):
    with p: 
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            for i in range(k+0, k+20):
                html_to_show = df['poster_html'].iloc[i]
                st.markdown(html_to_show, unsafe_allow_html=True)
        with col2:
            for i in range(k+20, k+40):
                html_to_show = df['poster_html'].iloc[i]
                st.markdown(html_to_show, unsafe_allow_html=True)
        with col3:
            for i in range(k+40, k+60):
                html_to_show = df['poster_html'].iloc[i]
                st.markdown(html_to_show, unsafe_allow_html=True)
        with col4:
            for i in range(k+60, k+80):
                html_to_show = df['poster_html'].iloc[i]
                st.markdown(html_to_show, unsafe_allow_html=True)
        with col5:
            for i in range(k+80, k+100):
                html_to_show = df['poster_html'].iloc[i]
                st.markdown(html_to_show, unsafe_allow_html=True)


images(p1,0)
images(p2,100)
images(p3,200)
images(p4,300)
images(p5,400)
images(p6,500)
images(p7,600)
images(p8,700)
images(p9,800)
images(p10,900)
 
