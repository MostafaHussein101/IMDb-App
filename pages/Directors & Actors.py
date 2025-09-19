import streamlit as st 
import pandas as pd 
import plotly_express as px
import Helper 

st.set_page_config(layout="wide")

df = Helper.load_data() 
Helper.Nav_Bar() 

 

st.title("🎥 Director's EDA")
col1,col2=st.columns(2)
with col1:
    Director = st.selectbox("Select a Director",df['Director'].unique())
    exclude = ["Movie Title", "Director","Poster_Link",'Overview',"Star1","Star2","Star3","Star4"]
    columns = [col for col in df.columns if col not in exclude]
with col2:
    Y = st.selectbox("Y axis", columns)
st.subheader(f"{Y} of Movies Directed by {Director}")
choice1=df[df['Director'] == Director]
plt1 = px.bar( 
    choice1,
    x="Movie Title",
    y=Y,
    color=Y,
    color_continuous_scale=px.colors.sequential.Blues,
)
st.plotly_chart(plt1)
st.write("---")


st.title("🎭 Actor's EDA")
col3,col4=st.columns(2)
with col3:
    all_actors = pd.concat([df["Star1"], df["Star2"], df["Star3"], df["Star4"]])
    all_actors = all_actors.dropna().unique()
    Actors = st.selectbox("Select an Actor",all_actors)
    exclude = ["Movie Title", "Director","Poster_Link",'Overview',"Star1","Star2","Star3","Star4"]
    columns = [col for col in df.columns if col not in exclude]
with col4:
    Y = st.selectbox("Choose a Category", columns)
st.subheader(f"{Y} of Movies Starred by {Actors}")
choice1 = df[
    (df["Star1"] == Actors) |
    (df["Star2"] == Actors) |
    (df["Star3"] == Actors) |
    (df["Star4"] == Actors)
]
plt1 = px.bar( 
    choice1,
    x="Movie Title",
    y=Y,
    color=Y,
    color_continuous_scale=px.colors.sequential.Magma_r,
)
st.plotly_chart(plt1)
