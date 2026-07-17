import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TMDB_TOKEN")

HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

IMAGE = "https://image.tmdb.org/t/p/w500"

st.set_page_config(
    page_title="CinemaVerse",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

html,body,.stApp{
    background:#0E1117;
    color:white;
}

.block-container{
    padding-top:2rem;
}

h1,h2,h3{
    color:white;
}

.movie-card{
    background:#1B1F27;
    border-radius:15px;
    padding:10px;
    text-align:center;
    box-shadow:0px 0px 10px rgba(255,255,255,0.08);
    transition:0.3s;
}

.movie-card:hover{
    transform:scale(1.02);
}

.rating{
    color:#FFD700;
    font-weight:bold;
    font-size:18px;
}

.title{
    font-size:18px;
    font-weight:bold;
    color:white;
}

.release{
    color:#B0B0B0;
}

.sidebar-title{
    font-size:28px;
    font-weight:bold;
    color:#4DA3FF;
}

</style>
""",unsafe_allow_html=True)

# ---------------- Sidebar ---------------- #

st.sidebar.markdown("# 🎬 CinemaVerse")

page = st.sidebar.radio(
    "Navigation",
    [
        "Trending",
        "Search"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Created using TMDB API")

# ---------------- API ---------------- #

def get_trending():

    url="https://api.themoviedb.org/3/trending/movie/week"

    response=requests.get(url,headers=HEADERS)

    return response.json()["results"]


def search_movie(name):

    url="https://api.themoviedb.org/3/search/movie"

    params={
        "query":name
    }

    response=requests.get(url,
                          headers=HEADERS,
                          params=params)

    return response.json()["results"]


# ---------------- Card ---------------- #

def show_movies(movies):

    cols=st.columns(4)

    for index,movie in enumerate(movies):

        with cols[index%4]:

            poster=IMAGE+movie["poster_path"] if movie["poster_path"] else ""

            if poster:
                st.image(poster,use_container_width=True)

            st.markdown(
                f"<div class='title'>{movie['title']}</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div class='rating'>⭐ {movie['vote_average']}</div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div class='release'>📅 {movie['release_date']}</div>",
                unsafe_allow_html=True
            )

            overview=movie["overview"]

            if len(overview)>120:
                overview=overview[:120]+"..."

            st.caption(overview)

            st.divider()

# ---------------- Pages ---------------- #

if page=="Trending":

    st.title("🔥 Trending Movies")

    with st.spinner("Loading Movies..."):

        movies=get_trending()

    show_movies(movies[:20])

# ---------------- Search ---------------- #

if page=="Search":

    st.title("🔍 Search Movies")

    movie=st.text_input("Enter Movie Name")

    if movie:

        with st.spinner("Searching..."):

            movies=search_movie(movie)

        if len(movies)==0:

            st.warning("Movie Not Found")

        else:

            show_movies(movies)