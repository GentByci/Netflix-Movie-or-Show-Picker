import pandas as pd
import numpy as np
import random
from random import choice

df_movies = pd.read_csv("Best Movies Netflix.csv")

comedy = df_movies

df_shows = pd.read_csv("Best Shows Netflix.csv")

movie_picker = random.choice(df_movies.TITLE)

show_picker = random.choice(df_shows.TITLE)

user_input = ''

while True:
    user_input = input(
        'Pick one: 1) Movie | 2) TV Show [1/2]? ')

    if user_input == '1':
        print('You picked a Movie. \nYour movie is:',movie_picker)
        break
    elif user_input == '2':
        print('You picked a TV Show. \nYour TV Show is:', show_picker)
        break
    else:
        print('Type 1 or 2')
        continue







