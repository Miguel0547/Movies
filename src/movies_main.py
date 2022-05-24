"""
CSAPX Project 1: Movie

In this project we worked with datasets from the IMDB website. We got
experience reading in the data and using various structures and collections in Python to
store, organize and efficiently query for different kinds of information relating to the movies
and their ratings.

***                                                                                         ***
    This module is the main module where we're running the main program - As described above.
***                                                                                         ***

author: Miguel Reyes
date: 09/26/21
"""

import sys
import movies_and_ratings
import queries
from timeit import default_timer as timer


def main():
    """
    Main function - uses the command line to determine whether to use the small or large datasets. If no command line
    arguments are present, the large datasets should be used. Otherwise the command line is assumed to contain a single
    argument "small", and the small datasets should be used.

    After the datasets are loaded, we read in the input files using the supplied run configurations which automatically
    redirect the supplied input file queries to standard input.

    Read each query line and storing every tab separated value into a list and using the values of the list we perform
    the query operations until there are no queries left.

    :return:None
    """
    number_of_commands = len(sys.argv)
    if number_of_commands < 2:
        small_or_large_basics = "title.basics"
        small_or_large_ratings = "title.ratings"
    else:
        small_or_large_basics = "small.basics"
        small_or_large_ratings = "small.ratings"

    print("reading data/" + small_or_large_basics + ".tsv into dict...")
    start = timer()
    movies = movies_and_ratings.read_movie_dataset(small_or_large_basics)  # dictionary of movies
    elapsed = timer() - start
    print("elapsed time (s):", elapsed, "\n")

    print("reading data/" + small_or_large_ratings + ".tsv into dict...")
    start2 = timer()
    ratings = movies_and_ratings.read_rating_dataset(small_or_large_ratings, movies)  # dictionary of movie ratings
    elapsed2 = timer() - start2
    print("elapsed time (s):", elapsed2, "\n")

    print("Total movies: " + movies_and_ratings.total_movies(movies))
    print("Total ratings: " + movies_and_ratings.total_ratings(ratings) + " \n")

    for line in sys.stdin:
        query = tuple(line.split())
        if "LOOKUP" in query:
            print("processing:", query[0], query[1])
            lookup_start = timer()
            queries.lookup(query[1], movies, ratings)
            elapsed = timer() - lookup_start
            print("elapsed time (s):", elapsed, "\n")
        if "CONTAINS" in query:
            empty_string = " "
            primary_title = empty_string.join(query[2:])
            print("processing:", query[0], query[1], primary_title)
            contains_start = timer()
            queries.contains(query[1], primary_title, movies)
            contains_elapsed = timer() - contains_start
            print("elapsed time (s):", contains_elapsed, "\n")
        if "YEAR_AND_GENRE" in query:
            print("processing:", query[0], query[1], query[2], query[3])
            year_and_genre_start = timer()
            queries.year_and_genre(query[1], query[2], query[3], movies)
            year_and_genre_elapsed = timer() - year_and_genre_start
            print("elapsed time (s):", year_and_genre_elapsed, "\n")
        if "RUNTIME" in query:
            print("processing:", query[0], query[1], query[2], query[3])
            runtime_start = timer()
            queries.runtime(query[1], query[2], query[3], movies)
            runtime_elapsed = timer() - runtime_start
            print("elapsed time (s):", runtime_elapsed, "\n")
        if "MOST_VOTES" in query:
            print("processing:", query[0], query[1], query[2])
            runtime_start = timer()
            queries.most_votes(query[1], query[2], movies, ratings)
            runtime_elapsed = timer() - runtime_start
            print("elapsed time (s):", runtime_elapsed, "\n")
        if "TOP" in query:
            print("processing:", query[0], query[1], query[2], query[3], query[4])
            runtime_start = timer()
            queries.top(query[1], query[2], query[3], query[4], movies, ratings)
            runtime_elapsed = timer() - runtime_start
            print("elapsed time (s):", runtime_elapsed, "\n")


if __name__ == '__main__':
    main()
