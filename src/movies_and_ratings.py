"""
CSAPX Project 1: Movie

In this project we worked with datasets from the IMDB website. We got
experience reading in the data and using various structures and collections in Python to
store, organize and efficiently query for different kinds of information relating to the movies
and their ratings.

***                                                                                                                 ***
    This module contains the Movie and Rating dataclasses as well as functions like reading the movie dataset and
    rating dataset into a dictionary of movie tconst strings to Movie objects and Rating objects.
***                                                                                                                 ***

author: Miguel Reyes
date: 09/26/21
"""
from dataclasses import dataclass

"""
Movie:
    tconst(str): unique identifier - unique for every movie
    title_type(str): type of movie - examples are short, movies, tv episode or tv series 
    primary_title(str): name of movie
    start_year(str): release date(year) of movie
    runtime_minutes(str): duration of movie in minutes
    genres(str): genre of movie - examples are Action, Comedy, or Drama
"""


@dataclass(frozen=True)
class Movie:
    """A dataclass to represent Movie."""
    tconst: str
    title_type: str
    primary_title: str
    start_year: str
    runtime_minutes: str
    genres: str


"""
Rating:
    tconst(str): unique identifier - unique for every move
    avg_rating(str): Movie average rating
    num_votes(str): Movie number of votes
"""


@dataclass(frozen=True)
class Rating:
    """A dataclass to represent Movie Rating."""
    tconst: str
    avg_rating: str
    num_votes: str


def read_movie_dataset(filename: str) -> dict:
    """
    Function to read in file, assign its content to the Movie objects field variables and store Movie objects into a
    dictionary.

    :param filename: The file name we're reading in
    :return: dictionary whose values are Movie objects
    """
    movies = dict()
    with open("data/" + filename + ".tsv", encoding="utf-8") as f:  # Will open to read and when done reading will -->
        # close file
        next(f)  # skips header line
        for line in f:
            newLine = line.rstrip()
            data_fields = list(newLine.split("\t"))  # line converted into a list
            if data_fields[4] == "1":  # will skip over list element(isAdult) when its equal to 1
                continue
            if data_fields[5] == "\\N":
                data_fields[5] = "0"
            if data_fields[7] == "\\N":
                data_fields[7] = "0"
            if data_fields[8] == "\\N":
                data_fields[8] = "None"
            movies[data_fields[0]] = Movie(data_fields[0], data_fields[1], data_fields[2], data_fields[5],
                                           data_fields[7], data_fields[8])
            #  Movie(tconst, title_type, primary_title, start_year, runtime_minutes, genres)

    return movies


def read_rating_dataset(filename: str, movies: dict) -> dict:
    """
    Function to read in a file, assign its content to the Rating objects field variables and store Rating objects into a
    dictionary.
    :param filename: The file name we're reading in
    :param movies: dictionary of Movie objects - returned from the read_movie_dataset function
    :return: dictionary whose values are Rating objects
    """
    ratings = dict()
    with open("data/" + filename + ".tsv", encoding="utf-8") as f:
        next(f)  # skips header line
        for line in f:
            newLine = line.rstrip()
            data_fields = tuple(newLine.split("\t"))  # line converted into a list
            if data_fields[0] in movies:  # We only want to store rating objects whose tconst is a key of a movie, -->
                # otherwise we don't need the rating object
                ratings[data_fields[0]] = Rating(data_fields[0], data_fields[1], data_fields[2])
                #  Rating(tconst, avg_rating, num_votes)

    return ratings


def total_movies(d: dict) -> str:
    """
    Function will count the total number of Movie objects

    :param d: dictionary of Movie objects - returned from the read_movie_dataset function
    :return: the total amount of Movie objects but in string format because we want to print this to the console
    """
    total = len(d)
    return str(total)


def total_ratings(d: dict) -> str:
    """
    Function will count the total number of Rating objects

    :param d: dictionary of Rating objects - returned from the read_movie_dataset function
    :return: the total amount of Rating objects but in string format because we want to print this to the console
    """
    total = len(d)
    return str(total)
