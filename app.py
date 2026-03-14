import streamlit as st
import pickle

st.title("Movie Selector App!")


movies = pickle.load(open("movies.pkl", "rb"))
movie_list = movies["title"].values  # Extract titles for the dropdown

similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie_title):
    # Find the index of the selected movie title
    index = movies[movies['title'] == movie_title].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    
    # Get the top 5 similar movies (excluding the first, which is itself)
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]]['title'])  # Append just the title for display
    
    return recommended_movies

option = st.selectbox("Choose a movie:", movie_list)

if st.button("Recommend"):
    recommendations = recommend(option)
    for rec in recommendations:
        st.write(rec)
