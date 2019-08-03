# Proposal

Train a neural network on a dataset of 5000 movie trailers. And build a model to make a prediction on the movie genre, based on the prevoius 5k genre-labled dataset.

# dataset
use: https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset
a csv cointaining 5k movie metadata. With the following features:
color
director_nameName of the Director of the Movie
num_critic_for_reviews
duration
director_facebook_likes
actor_3_facebook_likes
actor_2_name
actor_1_facebook_likesNumber of likes of the Actor_1 on his/her Facebook Page
gross
genres
actor_1_namePrimary actor starring in the movie
movie_title
num_voted_users
cast_total_facebook_likes
actor_3_name
facenumber_in_poster
plot_keywords
movie_imdb_link
num_user_for_reviews
language
country
content_rating
budget
title_year
actor_2_facebook_likes
imdb_score
aspect_ratio
movie_facebook_likes

# feature creation
Given a metadata csv. What is still missing is the trailer content.
In this case, what could be done is to create a webscraper that works as follows:

- youtube search "data['title'] + 'trailer'"
- click on first video
- add link of the trailer to the movie row, in a new column named 'trailer'

# NN training
 [nn training]
 
# storage
given the large dataset, using `youtube-dl` to download the videos. They have to be stored in the cloud.
Very likley using mongodb, in the form of a single collection of documents. Where each movie is stored as {'title': trailer_file}

# user facing product
the model should be presented as a single page website. Where the user inputs a youtube link to a movie trailer. And the trained model tries to predict the genre of the trailer, printed out in a text box.


# more than genre:
given that we have also a list of actors, 3 in each movie row. If given enough time, a possible method to add would be a prediction of actors showing in the trailer.

This of course is with the assumption that our neural network would be sufficient to notice that the same featur of 'actor' keeps showing up in Batman1, Batman2, Batman3. Without the need to point to a face. What is need is to detect that the actor is 'somewhere there' in the trailer, without needing to actually print or point out the face of the actor.
