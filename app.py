import streamlit as st
import pickle
import pandas as pd
import requests

#fetched posters and poster path
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

    for i in movies_list:
        print(new_df.iloc[i[0]].title)

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movie_name=st.selectbox('Please select a movie',movies['title'].values)

if st.button('Recommend'):
   names,posters = recommend(selected_movie_name)

#made columns for the movie posters
   col1,col2,col3,col4,col5,col6,col7=st.columns(7)
   with col1:
        st.text(names[0])
        st.image(posters[0])
   with col2:
        st.text(names[1])
        st.image(posters[1])
   with col3:
        st.text(names[2])
        st.image(posters[2])
   with col4:
        st.text(names[3])
        st.image(posters[3])
   with col5:
        st.text(names[4])
        st.image(posters[4])
   with col6:
       st.text(names[5])
       st.image(posters[5])
   with col7:
        st.text(names[6])
        st.image(posters[6])

st.sidebar.header("About")
st.sidebar.text("This is a movie recommender system \n"
                "which recommends various movies \n"
                "with regard to the choice you have\n"
                "made from the options available.\n")