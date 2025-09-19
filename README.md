# 🎬 IMDB Top 1000 Movies EDA

This project is an **Exploratory Data Analysis (EDA)** dashboard built with [Streamlit](https://streamlit.io/), showcasing insights from the **IMDB Top 1000 Movies Dataset**.  
The goal is to provide an **interactive and visually engaging way** to explore movie data, trends, and statistics such as ratings, genres, directors, actors, and financial performance.

---

## 🚀 Features
- 📊 **EDA Dashboard**: Interactive visualizations of IMDB ratings, genres, gross earnings, votes, runtime distributions, and more.  
- 🎭 **Movie Details**: Dive into individual movie information with posters, directors, cast, and ratings.  
- 🎥 **Directors & Actors**: Analyze top-performing directors and actors based on the number of movies, gross earnings, and ratings.  
- ⚖️ **Compare Movies**: Compare multiple movies side by side.  
- 🌐 **IMDb Link Integration**: Quick access to movie details on IMDB.  
- 🖼️ **Poster Gallery**: Browse all 1000 movies in a visually appealing poster wall with tooltips for extra information.

---

## 📂 Repository Structure
```bash
├── Home.py                  # Main entry page
├── pages/
│   ├── EDA.py               # Exploratory Data Analysis dashboard
│   ├── Movie Details.py     # Detailed info about movies
│   ├── Directors & Actors.py # Insights on directors and actors
│   ├── Compare Movies.py    # Compare multiple movies
├── Helper.py                # Shared functions (NavBar, data loading, etc.)
├── imdb_top_1000.csv        # Dataset (IMDB Top 1000 Movies)
```


---

## 📊 Insights
Some key insights extracted from the dataset:
- ⭐ **IMDB Ratings** mostly fall between 6.5 and 8.5, with a few exceptional movies scoring above 9.  
- 🎭 **Drama** is the most frequent genre, followed by **Comedy** and **Action**.  
- 🎥 Directors like **Steven Spielberg** and **Martin Scorsese** dominate in terms of number of movies.  
- 👥 Actors such as **Robert De Niro**, **Tom Hanks**, and **Meryl Streep** appear frequently in the dataset.  
- 💰 Gross earnings are dominated by blockbuster franchises, with a handful of movies contributing disproportionately.  
- ⏳ Most movies have runtimes between **90 and 150 minutes**.  
- 🗳️ Highly rated movies also tend to attract **more votes**, indicating popularity and critical acclaim.  
- 🎟️ Certificates like **R** and **PG-13** are the most common among top movies.  

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/imdb-eda.git
   cd imdb-eda
