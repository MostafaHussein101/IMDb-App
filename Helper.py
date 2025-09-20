import streamlit as st 
import pandas as pd 
import numpy as np
import matplotlib as plt
import seaborn as sns
import plotly_express as px

@st.cache_data 
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/MostafaHussein101/IMDb-App/main/imdb_top_1000.csv")
    df.rename(columns={"Series_Title":"Movie Title","Released_Year":"Released Year","IMDB_Rating":"IMDB Rating","Meta_score":"Meta score","No_of_Votes":"Number of votes"},inplace=True)
    df.columns = df.columns.str.strip()
    df['Gross'] = df['Gross'].str.replace(',', '')
    df['Gross'] = df['Gross'].astype('float64')
    st.markdown(
    f"""
     <style>
     .stApp {{
         background-image: url("https://c4.wallpaperflare.com/wallpaper/307/12/896/simple-background-black-background-minimalism-theater-wallpaper-preview.jpg");
         background-size: cover;
         color: white;
     }}
     </style>
     """,
    unsafe_allow_html=True)
    return df
df = load_data() 

def Nav_Bar():
    x1,x2,x3,x4,x5,x6,x7 = st.columns(7)
    with x1:
        st.page_link("Home.py", label="🏠 Home")
    with x5:
        st.page_link("pages/EDA.py", label="📊 EDA")
    with x2:
        st.page_link("pages/Movie Details.py", label="🎭 Movie Details")
    with x4:
        st.page_link("pages/Directors & Actors.py",label="🎥 Directors & Actors")
    with x7:
        st.page_link("https://www.imdb.com/", label="🌐 IMDb website")
    with x3:
        st.page_link("pages/Compare Movies.py",label = "⚖️ Compare Movies")
    with x6:
        st.page_link('pages/Insights.py',label='🤔 Insights')
    st.logo(image='https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg',size="large")
