"""
CSAPX Project 1: Movie

In this project we worked with datasets from the IMDB website. We got
experience reading in the data and using various structures and collections in Python to
store, organize and efficiently query for different kinds of information relating to the movies
and their ratings.

***                                         ***
    This module contains all query functions
***                                         ***

author: Miguel Reyes
date: 09/26/21
"""
import operator


def lookup(tconst: str, movies: dict, ratings: dict):
    """
    LOOKUP Query:
    This function will look up a movie and its rating by using tconst(the movies unique identifier) and
    print the following:
    processing: LOOKUP {tconst}
        MOVIE: Identifier: {tconst}, Title: {primaryTitle}, Type: {titleType}, Year: {startYear}, Runtime: {runTime},
        Genres: {genres}
        RATING: Identifier: {tconst}, Rating: {rating}, Votes: {numVotes}
    elapsed time (s): {###}

    If either the movie or rating is not found the output should be:
    processing: LOOKUP tt0080684
        Movie not found!
        Rating not found!
    elapsed time (s): {###}

    :param tconst: unique identifier - unique for every movie
    :param movies: dictionary of Movie objects
    :param ratings: dictionary of Rating objects
    :return: None
    """
    if tconst in ratings:  # only want the tconst(key) in the ratings dictionary because we don't want to deal with ->
        # movies that don't have ratings
        print("\tMOVIE: Identifier: " + tconst + ", Title: " + movies[
            tconst].primary_title + ", Type: " + movies[tconst].title_type + ", Year: " + movies[tconst].start_year
              + ", Runtime: " + movies[tconst].runtime_minutes + ", Genres: "
              + movies[tconst].genres.replace(",", ", "))
        print("\tRATING: Identifier: " + tconst + ", Rating: " + ratings[tconst].avg_rating + ", Votes: " +
              ratings[tconst].num_votes)
    else:
        print("\tMovie not found!\n\tRating not found!")


def contains(title_type: str, words: str, movies: dict):
    """
    CONTAINS Query:
    When looking up movies of a certain title type, whose primary title contains the sequence
    of words from the input, there are two possible outcomes. In the event one or more movies
    are found, the movies should be displayed in the order they appear in the dataset.
    processing: CONTAINS {titleType} {words}
        Identifier: {tconst}, Title: {primaryTitle}, Type: {titleType}, Year: {startYear}, Runtime: {runTime},
        Genres: {genres}
        ...
    elapsed time (s): {###}

    If there are no movies that match the output should be:
    processing: CONTAINS {titleType} {words}
        No match found!
    elapsed time (s): {###}

    :param title_type: type of movie - examples are short, movies, tv episode or tv series
    :param words: string of words that may be substrings of movie objects primary_title field variable
    :param movies: dictionary of Movie objects
    :return: None
    """
    counter = 0  # this will keep track of all the movies that do not meet the conditions below - if conditions met ->
    # increment counter otherwise it stays at 0 and will print "No match found!"
    for movie in movies.values():  # iterating through movies values
        if title_type == movie.title_type and words in movie.primary_title:  # Conditions to check title_type match ->
            # and words is a substring of the movie objects primary_title
            print("\tIdentifier: " + movie.tconst + ", Title: " + movie.primary_title +
                  ", Type: " + movie.title_type + ", Year: " + movie.start_year + ", Runtime: " +
                  movie.runtime_minutes + ", Genres: " + movie.genres.replace(",", ", "))
            counter += 1
        else:
            continue
    if counter == 0:
        print("\tNo match found!")


def filter_year_and_genre_only(title_type: str, year: str, genre: str, movies: dict) -> list:
    """
    This function will take in the movies dictionary, iterate through its values(movie objects) and filter out the
    movie objects that do not pass the following conditions - Movies of a certain title type, start year and genre.
    The movies that do pass the conditions are stored into a list and that list is returned.

    The purpose of this function is to return a much smaller collection so when sorting is done in the year_and_genre
    function it is done much more efficiently because sorting a much smaller collection decreases run time.

    :param title_type: type of movie - examples are short, movies, tv episode or tv series
    :param year: start_year of movie object
    :param genre: genre of movie object
    :param movies: dictionary of Movie objects
    :return: list of Movie objects
    """
    new_list = list()
    for movie in movies.values():
        if title_type == movie.title_type and year == movie.start_year and genre in movie.genres:
            new_list.append(movie)

    return new_list


def year_and_genre(title_type: str, year: str, genre: str, movies: dict):
    """
    YEAR_AND_GENRE Query:
    When looking up movies of a certain title type, whose start year and genre matches, there are
    two possible outcomes. In the event one or more movies are found, the movies should be displayed alphabetically by
    primary title.
    processing: YEAR_AND_GENRE {titleType} {startYear} {genre}
        Identifier: {tconst}, Title: {primaryTitle}, Type: {titleType}, Year: {startYear},
        Runtime: {runTime}, Genres: {genres}
        ...
    elapsed time (s): {###}

    If there are no movies that match the output should be:
    processing: YEAR_AND_GENRE {titleType} {startYear} {genre}
        No match found!
    elapsed time (s): {###}

    :param title_type: type of movie - examples are short, movies, tv episode or tv series
    :param year: start_year of movie object
    :param genre: genre of movie object
    :param movies: dictionary of Movie objects
    :return: None
    """
    final_movies = filter_year_and_genre_only(title_type, year, genre, movies)  # list of movies from ----------->
    # filter_year_and_genre_only function

    final_movies.sort(key=operator.attrgetter("primary_title"))  # Sort final_movies by ascending primary_title

    counter = 0  # this will keep track of all the movies that do not meet the conditions below - if conditions met ->
    # increment counter otherwise it stays at 0 and will print "No match found!"

    for movie in final_movies:
        print("\tIdentifier: " + movie.tconst + ", Title: " + movie.primary_title +
              ", Type: " + movie.title_type + ", Year: " + movie.start_year + ", Runtime: " +
              movie.runtime_minutes + ", Genres: " + movie.genres.replace(",", ", "))
        counter += 1
    if counter == 0:
        print("\tNo match found!")


def filter_runtime_only(title_type: str, min_mins: str, max_mins: str, movies: dict) -> list:
    """
    This function will take in the movies dictionary, iterate through its values(movie objects) and filter out the
    movie objects that do not pass the following conditions - Movies of a certain title type, whose runtime is
    between the start and end times (inclusive). The movies that do pass the conditions are stored into a list and
    that list is returned.

    The purpose of this function is to return a much smaller collection so when sorting is done in the runtime function
    it is done much more efficiently because sorting a much smaller collection decreases run time.

    :param title_type: type of movie - examples are short, movies, tv episode or tv series
    :param min_mins: minimum minutes passed in as string but evaluated as an int in the condition
    :param max_mins: maximum minutes passed in as string but evaluated as an int in the condition
    :param movies: dictionary of Movie objects
    :return: list of Movie objects
    """
    new_list = list()
    for movie in movies.values():
        if title_type == movie.title_type and int(min_mins) <= int(movie.runtime_minutes) <= int(max_mins):
            new_list.append(movie)

    return new_list


def runtime(title_type: str, min_mins: str, max_mins: str, movies: dict):
    """
    RUNTIME Query:
    When looking up movies of a certain title type, whose runtime is between the start and end
    times (inclusive), there are two possible outcomes. In the event one or more movies are found, the movies should be
    displayed first by descending runtime, and second ascending alphabetically by primary title.
    processing: RUNTIME {titleType} {startTime} {endTime}
        Identifier: {tconst}, Title: {primaryTitle}, Type: {titleType}, Year: {startYear},
        Runtime: {runTime}, Genres: {genres}
        ...
    elapsed time (s): {###}

    If there are no movies that match the output should be:
    processing: RUNTIME {titleType} {min-minutes} {max-minutes}
        No match found!
    elapsed time (s): {###}

    :param title_type: type of movie - examples are short, movies, tv episode or tv series
    :param min_mins: minimum minutes passed in as string but evaluated as an int in the condition
    :param max_mins: maximum minutes passed in as string but evaluated as an int in the condition
    :param movies: dictionary of Movie objects
    :return: None
    """
    final_movies = filter_runtime_only(title_type, min_mins, max_mins, movies)  # list of movies from ----------->
    # filter_runtime_only function

    # Must sort things in the opposite order you intend - so if you want to sort by runtime then primary title must ->
    # call sorts in the reverse order such as primary title then runtime.
    final_movies.sort(key=operator.attrgetter("primary_title"))  # Sort final_movies by ascending primary_title
    final_movies.sort(key=operator.attrgetter("runtime_minutes"), reverse=True)  # Sort final_movies by descending --->
    # runtime_minutes

    counter = 0  # this will keep track of all the movies that do not meet the conditions below - if conditions met ->
    # increment counter otherwise it stays at 0 and will print "No match found!"

    for movie in final_movies:
        print("\tIdentifier: " + movie.tconst + ", Title: " + movie.primary_title +
              ", Type: " + movie.title_type + ", Year: " + movie.start_year + ", Runtime: " +
              movie.runtime_minutes + ", Genres: " + movie.genres.replace(",", ", "))
        counter += 1
    if counter == 0:
        print("\tNo match found!")


def filter_most_votes_only(title_type: str, movies: dict, ratings: dict) -> list:
    """
    This function will take in the movies and ratings dictionary, iterate through the ratings values(rating objects)
    and filter out the movie objects that do not pass the following conditions - movies of a certain title type,
    and the key from the ratings dictionary must be a key in the movies dictionary. If conditions are met the movie
    objects along with the ratings num_votes field variable is stored as a tuple pair in a list.

    The purpose of this function is to return a much smaller collection so when sorting is done in the most_votes
    function it is done much more efficiently because sorting a much smaller collection decreases run time.

    :param title_type: type of movie - examples are short, movies, tv episode or tv series
    :param movies: dictionary of Movie objects
    :param ratings: dictionary of Rating objects
    :return: list of tuple pairs(Movie object, Rating.num_votes)
    """
    new_list = list()
    for key in ratings:
        if key in movies.keys() and title_type == movies.get(key).title_type:
            new_list.append((movies.get(key), int(ratings.get(key).num_votes)))
    return new_list


def most_votes(title_type: str, top_num: str, movies: dict, ratings: dict):
    """
    MOST_VOTES Query:
    When looking up the top number of movies of a certain title type, there are two possible
    outcomes. In the event one or more movies are found, the movies should be displayed first by descending number of
    votes, and second ascending alphabetically by primary title.
    processing: MOST_VOTES {titleType} {num}
        1. VOTES: {###}, MOVIE: Identifier: {tconst}, Title: {primaryTitle}, Type: {titleType}, Year: {startYear},
        Runtime: {runTime}, Genres: {genres}
        ...
    elapsed time (s): {###}

    If there are no movies that match the output should be:
    processing: MOST_VOTES {titleType} {num}
        No match found!
    elapsed time (s): {###}

    :param title_type:
    :param top_num: maximum number of output to the console - depends on the sorting done to the final_movies list
    :param movies: dictionary of Movie objects
    :param ratings: dictionary of Rating objects
    :return: None
    """
    final_movies = filter_most_votes_only(title_type, movies, ratings)  # list of movies from ----------->
    # filter_most_votes_only function

    # Must sort things in the opposite order you intend - so if you want to sort by runtime then primary title must ->
    # call sorts in the reverse order such as primary title then runtime.
    final_movies.sort(key=lambda x: x[0].primary_title)  # Sort final_movies by tuples first element in ascending ->
    # primary_title
    final_movies.sort(key=lambda x: x[1], reverse=True)  # Sort final_movies by tuples 2nd element in descending ->
    # num_votes

    counter = 0  # this will keep track of all the movies that do not meet the conditions below - if conditions met ->
    # increment counter otherwise it stays at 0 and will print "No match found!"

    num = 0  # Keeps track of how many times we send output to the console, once num is equal to top_num then ----->
    # we break out of the loop

    i = 1  # Used for displaying what output number we are at i <= top_num

    for movie in final_movies:
        if num == int(top_num):
            break
        else:
            print("\t" + str(i) + ". VOTES: " + str(movie[1]) + ", MOVIE: Identifier: " + movie[0].tconst + ", Title: "
                  + movie[0].primary_title + ", Type: " + movie[0].title_type + ", Year: " + movie[0].start_year
                  + ", Runtime: " + movie[0].runtime_minutes + ", Genres: " + movie[0].genres.replace(",", ", "))
            counter += 1
            num += 1
            i += 1
    if counter == 0:
        print("\tNo match found!")


def filter_top_only(title_type: str, start_year: str, end_year: str, movies: dict, ratings: dict):
    """
    This function will take in the movies and ratings dictionary, iterate through the ratings values(rating objects)
    and filter out the movie objects that do not pass the following conditions - movies of a certain title type, the key
    from the ratings dictionary must be a key in the movies dictionary, the start_year must be between start and year
    parameters, and rating object must have over 1000 votes. If conditions are met the movie and rating objects are
    stored as a tuple pair in a list.

    The purpose of this function is to return a much smaller collection so when sorting is done in the top function it
    is done much more efficiently because sorting a much smaller collection decreases run time.

    :param title_type: type of movie - examples are short, movies, tv episode or tv series
    :param start_year: start of range - evaluated as an int
    :param end_year: end of range - evaluated as an int
    :param movies: dictionary of Movie objects
    :param ratings: dictionary of Rating objects
    :return: list of tuple pairs(Movie object, Rating object)
    """
    new_list = list()
    for key in ratings:
        if key in movies.keys() and title_type == movies.get(key).title_type and \
                int(ratings.get(key).num_votes) >= 1000 \
                and int(start_year) <= int(movies.get(key).start_year) <= int(end_year):
            new_list.append((movies.get(key), ratings.get(key)))

    return new_list


def top(title_type: str, top_num: str, start_year: str, end_year: str, movies: dict, ratings: dict):
    """
    TOP Query:
    When looking up the top number of movies of a certain title type for each year in a range
    of years (with at least 1000 votes), there are two possible outcomes.
    In the event one or more movies are found, the movies should be displayed in increasing order
    by year. For each year, the top movies should display first by descending rating, second by
    descending number of votes, and third ascending alphabetically by primary title.
    processing: TOP {titleType} {num} {startYear} {endYear}
        YEAR: {####}
            1. RATING: {###}, VOTES: {###}, MOVIE: Identifier: {tconst}, Title: {primaryTitle},
            Type: {titleType}, Year: {startYear}, Runtime: {runTime}, Genres: {genres}
            ...
        YEAR: {####}
            ...
    elapsed time (s): {###}

    If there are no movies that match the output should be:
    processing: TOP {titleType} {num} {startYear} {endYear}
        YEAR: {####}
            No match found!
    elapsed time (s): {###}

    :param title_type: type of movie - examples are short, movies, tv episode or tv series
    :param top_num: maximum number of output to the console - depends on the sorting done to the final_movies list
    :param start_year: start of range - evaluated as an int
    :param end_year: end_year: end of range - evaluated as an int
    :param movies: movies: dictionary of Movie objects
    :param ratings: ratings: dictionary of Rating objects
    :return: None
    """
    final_movies = filter_top_only(title_type, start_year, end_year, movies, ratings)  # list of movies from --------->
    # filter_most_votes_only function

    # Must sort things in the opposite order you intend - so if you want to sort by runtime then primary title must ->
    # call sorts in the reverse order such as primary title then runtime.
    final_movies.sort(key=lambda x: x[0].primary_title)  # Sort final_movies by tuples first element in ascending ->
    # primary_title
    final_movies.sort(key=lambda x: int(x[1].num_votes), reverse=True)  # Sort final_movies by tuples 2nd element in ->
    # descending num_votes
    final_movies.sort(key=lambda x: float(x[1].avg_rating), reverse=True)  # Sort final_movies by tuples 2nd element ->
    # in descending avg_rating

    num = 0  # Keeps track of how many times we send output to the console, once num is equal to top_num then ---->
    # we break out of the loop

    j = 0  # Used to increment start_year_int up until it is equal to end year - covers range from start_year - end_year

    i = 1  # Used for displaying what output number we are at i <= top_num

    for y in range(int(start_year), (int(end_year) + 1)):
        counter = 0
        start_year_int = int(start_year) + j
        print("\tYEAR: " + str(start_year_int))
        for movie in final_movies:
            if int(movie[0].start_year) == start_year_int:
                if num == int(top_num):
                    continue
                else:
                    print("\t\t" + str(i) + ". RATING: " + movie[1].avg_rating + ", VOTES: " + movie[1].num_votes +
                          ", MOVIE: Identifier: " + movie[0].tconst + ", Title: "
                          + movie[0].primary_title + ", Type: " + movie[0].title_type + ", Year: " + movie[0].start_year
                          + ", Runtime: " + movie[0].runtime_minutes + ", Genres: " + movie[0].genres.replace(",",
                                                                                                              ", "))
                    num += 1
                    i += 1
                    counter += 1
        j += 1
        num = 0  # set num equal to zero again for every year within the range of start_year and end_year to print
        # max amount of output
        i = 1
        if counter == 0:
            print("\t\tNo match found!")
