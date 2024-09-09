# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:48:00 2024

@author: anjan
"""

import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/" +poster_path
    return full_path


movies=pickle.load(open("movies_list.pkl",'rb'))
similarity=pickle.load(open("similarity.pkl",'rb'))
movies_list=movies['title'].values
st.title("Dive into the world of fantasies and mind-bending imaginations")


st.header("Movies with highest IMDB ratings")

vote=list(enumerate(movies['vote_average']))
vote=sorted(vote,key=lambda x:x[1],reverse=True)
moviename=[]
movieposter=[]
for i in range(6,11):
  l=vote[i]
   
  movies_id=movies[movies.index==l[0]]['id'].values[0]
  moviename.append(movies[movies.index==l[0]]['title'].values[0])
  movieposter.append(fetch_poster(movies_id))
  
col1,col2,col3,col4,col5=st.columns(5)
with col1:
    st.text(moviename[0])
    st.image(movieposter[0])
with col2:
    st.text(moviename[1])
    st.image(movieposter[1])
with col3:
    st.text(moviename[2])
    st.image(movieposter[2])
with col4:
    st.text(moviename[3])
    st.image(movieposter[3])
with col5:
    st.text(moviename[4])
    st.image(movieposter[4])
    
if st.button("show more"):
    for i in range(11,21):
      l=vote[i]
       
      movies_id=movies[movies.index==l[0]]['id'].values[0]
      moviename.append(movies[movies.index==l[0]]['title'].values[0])
      movieposter.append(fetch_poster(movies_id))
      
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(moviename[5])
        st.image(movieposter[5])
    with col2:
        st.text(moviename[6])
        st.image(movieposter[6])
    with col3:
        st.text(moviename[7])
        st.image(movieposter[7])
    with col4:
        st.text(moviename[9])
        st.image(movieposter[9])
    with col5:
        st.text(moviename[10])
        st.image(movieposter[10])
        
    col6,col7,col8,col9,col10=st.columns(5)
    with col6:
         st.text(moviename[11])
         st.image(movieposter[11])
    with col7:
         st.text(moviename[12])
         st.image(movieposter[12])
    with col8:
         st.text(moviename[13])
         st.image(movieposter[13])
    with col9:
         st.text(moviename[14])
         st.image(movieposter[14])
    with col10:
         st.text(moviename[8])
         st.image(movieposter[8])
    
st.header("Watch movies you like")

#create a dropdown to select a movie
selected_movie=st.selectbox("select your last watched movie:", movies_list)

#import streamlit.components.v1 as components

def recommend(movie):

    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector: vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button("recommend"):
    st.header("These are some recommendations")
    movie_name,movie_poster=recommend(selected_movie)
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
else:
    st.header("These are some recommendations")
    movie_name,movie_poster=recommend("Avatar")
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
           

director_list=movies['director'].values
st.header("watch movies from your faviourite directors")    
selected_director=st.selectbox("select director name",director_list)
def recommend(director):
    list_directors=movies['director'].tolist()
    recommend_movie=[]
    recommend_poster=[]
    for i in range (len(list_directors)):
        if (list_directors[i]==director):
                           
         movies_id=movies[movies.index==i]['id'].values[0]
         recommend_movie.append(movies[movies.index==i]['title'].values[0])
         recommend_poster.append(fetch_poster(movies_id))
             
    return recommend_movie, recommend_poster 

if st.button("recommend movies"):
    st.header("These are some recommendations")
    movie_name,movie_poster=recommend(selected_director)
    for i in range(0,int(len(movie_name)/5),1):
        col1,col2,col3,col4,col5=st.columns(5)
    
        with col1:
            st.text(movie_name[i*5])
            st.image(movie_poster[i*5])
        with col2:
            st.text(movie_name[i*5+1])
            st.image(movie_poster[i*5+1])
        with col3:
            st.text(movie_name[i*5+2])
            st.image(movie_poster[i*5+2])
        with col4:
            st.text(movie_name[i*5+3])
            st.image(movie_poster[i*5+3])
        with col5:
            st.text(movie_name[i*5+4])
            st.image(movie_poster[i*5+4])
    i=len(movie_name)
    j=len(movie_name)%5
    k=0
    col1,col2,col3,col4,col5=st.columns(5)
    if(k<j):
        with col1:
            st.text(movie_name[i-j-1])
            st.image(movie_poster[i-j-1])
        k=k+1
        
    if(k<j):    
        with col2:
            st.text(movie_name[i-j])
            st.image(movie_poster[i-j])
            k=k+1
    
            
    if(k<j):        
        with col3:
            st.text(movie_name[i+1-j])
            st.image(movie_poster[i+1-j])
            k=k+1
    
        
    if(k<j):       
        with col4:
            st.text(movie_name[i+2-j])
            st.image(movie_poster[i+2-j])
            k=k+1
    
        
    if(k<j):
        with col5:
            st.text(movie_name[i+3-j])
            st.image(movie_poster[i+3-j])
            k=k+1
    
              
else:
    movie_name,movie_poster=recommend("James Cameron")
    col1,col2,col3,col4,col5=st.columns(5)
    
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])

