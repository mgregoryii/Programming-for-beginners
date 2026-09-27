# ========================================
# MOVIE COLLECTION MANAGER
# ========================================
# 1. Add a movie
# 2. Display all movies
# 3. Search for a movie
# 4. Calculate average rating
# 5. Find highest-rated movie
# 6. Exit
# ========================================
# Enter your choice (1-6): 2

# ============================================================
# MOVIE COLLECTION First 5
# ============================================================

# Movie #1
# Title:  The Godfather
# Year:   1972
# Genres: Drama
# Rating: 9.2/10

# Movie #2
# Title:  Back to the Future
# Year:   1985
# Genres: Comedy, Science Fiction
# Rating: 8.5/10

# Movie #3
# Title:  The Shawshank Redemption
# Year:   1994
# Genres: Drama
# Rating: 9.3/10

# Movie #4
# Title:  The Matrix
# Year:   1999
# Genres: Action, Science Fiction
# Rating: 8.7/10

# Movie #5
# Title:  The Dark Knight
# Year:   2008
# Genres: Action, Drama
# Rating: 9.0/10

# Movie #10
# Title:  Inception
# Year:   2010
# Genres: Science Fiction, Action
# Rating: 9.5/10

# Highest-Rated Movie
# ------------------------------
# Title:  Transformers One
# Year:   2024
# Genres: Science Fiction
# Rating: 9.8/10
# ============================================================
# MOVIE COLLECTION by Year
# ============================================================

# Movie #1
# Title:  The Godfather
# Year:   1972
# Genres: Drama
# Rating: 9.2/10

# Movie #2
# Title:  Back to the Future
# Year:   1985
# Genres: Comedy, Science Fiction
# Rating: 8.5/10

# Movie #3
# Title:  The Shawshank Redemption
# Year:   1994
# Genres: Drama
# Rating: 9.3/10

# Movie #4
# Title:  The Matrix
# Year:   1999
# Genres: Action, Science Fiction
# Rating: 8.7/10

# Movie #5
# Title:  The Dark Knight
# Year:   2008
# Genres: Action, Drama
# Rating: 9.0/10

# Movie #6
# Title:  Inception
# Year:   2010
# Genres: Science Fiction, Fantasy
# Rating: 9.4/10

# Movie #7
# Title:  Toy Story 3
# Year:   2010
# Genres: Comedy
# Rating: 9.7/10

# Movie #8
# Title:  Rogue One
# Year:   2016
# Genres: Science Fiction, Action
# Rating: 8.4/10

# Movie #9
# Title:  Blade Runner 2049
# Year:   2017
# Genres: Science Fiction, Action
# Rating: 9.1/10

# Movie #10
# Title:  Transformers One
# Year:   2024
# Genres: Science Fiction
# Rating: 9.8/10

# Average movie rating: 9.11/10
# This is my movie tracker that creates a library of movies based
# on a user's input.
import datetime


# List that stores all movie dictionaries
movie_collection = []


def create_movie(title, year, genres, rating):
    """Create and return a movie dictionary."""
    return {
        "title": title,
        "year": year,
        "genres": genres,
        "rating": rating
    }

# Creates a list of genres to choose from to improve data quality
def get_genres():
    """Get and validate genre selections from the user."""

    available_genres = [
        "Drama",
        "Comedy",
        "Action",
        "Thriller",
        "Horror",
        "Romance",
        "Science Fiction",
        "Fantasy",
        "Documentary"
    ]

    print("\nSelect genre(s):")

    for number, genre in enumerate(available_genres, start=1):
        print(f"{number}. {genre}")

    while True:
        genre_input = input(
            "Enter genre number(s), separated by commas "
            "(example: 2, 3): "
        ).strip()

        # Reject empty genre selections
        if not genre_input:
            print("You must select at least one genre.")
            continue

        # Split input into individual choices
        choices = genre_input.split(",")

        # Reject empty selections such as 2,,3 or 2, ,3
        if any(choice.strip() == "" for choice in choices):
            print("Empty genre selections are not allowed.")
            continue

        try:
            selections = [
                int(choice.strip())
                for choice in choices
            ]

            # Reject duplicate selections
            if len(selections) != len(set(selections)):
                print(
                    "Duplicate genres are not allowed. "
                    "Please select each genre only once."
                )
                continue

            # Check that all selections are valid
            if all(
                1 <= choice <= len(available_genres)
                for choice in selections
            ):
                genres = [
                    available_genres[choice - 1]
                    for choice in selections
                ]

                return genres

            print("Please select numbers from 1-9.")

        except ValueError:
            print(
                "Please enter valid genre numbers separated by commas."
            )


def add_movie():
    """Add a new movie to the collection."""

    # Validate movie title
    while True:
        title = input("Enter movie title: ").strip()

        if 1 <= len(title) <= 300:
            break

        print("Movie title must be between 1 and 300 characters.")

    # Validate release year
    current_year = datetime.date.today().year

    while True:
        try:
            year = int(
                input(
                    f"Enter release year (1888-{current_year}): "
                )
            )

            if 1888 <= year <= current_year:
                break

            print(
                f"Please enter a year between 1888 and "
                f"{current_year}."
            )

        except ValueError:
            print("Please enter a whole number for the year.")

    # Get and validate genres
    genres = get_genres()

    # Validate rating
    while True:
        try:
            rating = float(input("Enter rating (0-10): "))

            if 0 <= rating <= 10:
                break

            print("Rating must be between 0 and 10.")

        except ValueError:
            print("Please enter a numeric rating.")

    # Create movie dictionary
    movie = create_movie(
        title,
        year,
        genres,
        rating
    )

    # Add movie to collection
    movie_collection.append(movie)
# Sort movie by year
    movie_collection.sort(
        key=lambda movie: movie["year"]
    )

    print(f'"{title}" was added to your collection.')


def display_movies(movies, heading="MOVIE COLLECTION"):
    """Display all movies in the collection."""

    if not movies:
        print("\nYour movie collection is empty.")
        return

    print("\n" + "=" * 60)
    print(heading)
    print("=" * 60)

    for number, movie in enumerate(movies, start=1):
        genres = ", ".join(movie["genres"])

        print(f"\nMovie #{number}")
        print(f"Title:  {movie['title']}")
        print(f"Year:   {movie['year']}")
        print(f"Genres: {genres}")
        print(f"Rating: {movie['rating']:.1f}/10")


def search_movies():
    """Search for movies by title."""

    if not movie_collection:
        print("\nYour movie collection is empty.")
        return

    search_term = input(
        "Enter a movie title to search for: "
    ).lower()

    found_movies = []

    for movie in movie_collection:
        if search_term in movie["title"].lower():
            found_movies.append(movie)

    if found_movies:
        print("\nMovies Found:")

        for movie in found_movies:
            genres = ", ".join(movie["genres"])

            print(
                f"- {movie['title']} "
                f"({movie['year']}) | "
                f"{genres} | "
                f"Rating: {movie['rating']:.1f}/10"
            )
    else:
        print("No movies matched your search.")

# Calculates avg movie ratings
def calculate_average_rating():
    """Calculate the average rating of all movies."""

    if not movie_collection:
        print("\nThere are no movies to analyze.")
        return

    total_rating = 0

    for movie in movie_collection:
        total_rating += movie["rating"]

    average = total_rating / len(movie_collection)

    print(f"\nAverage movie rating: {average:.2f}/10")


def highest_rated_movie():
    """Find and display the highest-rated movie."""

    if not movie_collection:
        print("\nThere are no movies to analyze.")
        return

    highest = movie_collection[0]

    for movie in movie_collection:
        if movie["rating"] > highest["rating"]:
            highest = movie

    print("\nHighest-Rated Movie")
    print("-" * 30)
    print(f"Title:  {highest['title']}")
    print(f"Year:   {highest['year']}")
    print(f"Genres: {', '.join(highest['genres'])}")
    print(f"Rating: {highest['rating']:.1f}/10")

# Defines top rated movies
def find_top_rated(movies, count):
    """Return the top-rated movies."""

    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True
    )

    return sorted_movies[:count]

# Display selection menu for user choices
def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 40)
    print("MOVIE COLLECTION MANAGER")
    print("=" * 40)
    print("1. Add a movie")
    print("2. Display all movies")
    print("3. Search for a movie")
    print("4. Calculate average rating")
    print("5. Find highest-rated movie")
    print("6. Exit")
    print("=" * 40)


# ============================================================
# Main Program
# ============================================================

# 1. Define the five-movie starter list
movie_collection = [
    create_movie(
        "The Shawshank Redemption",
        1994,
        ["Drama"],
        9.3
    ),
    create_movie(
        "The Godfather",
        1972,
        ["Drama"],
        9.2
    ),
    create_movie(
        "The Dark Knight",
        2008,
        ["Action", "Drama"],
        9.0
    ),
    create_movie(
        "Back to the Future",
        1985,
        ["Comedy", "Science Fiction"],
        8.5
    ),
    create_movie(
        "The Matrix",
        1999,
        ["Action", "Science Fiction"],
        8.7
    )
]


# 2. Display the collection as loaded
display_movies(
    movie_collection,
    "Your Movie Collection"
)


# 3. Ask the user to add two new movies
for number in range(2):

    print(f"\nEnter information for new movie #{number + 1}")

    # Get title
    while True:
        title = input("Enter movie title: ").strip()

        if 1 <= len(title) <= 300:
            break

        print("Movie title must be between 1 and 300 characters.")

    # Get year
    current_year = datetime.date.today().year

    while True:
        try:
            year = int(input("Enter release year: "))

            if 1888 <= year <= current_year:
                break

            print(
                f"Please enter a year between 1888 and "
                f"{current_year}."
            )

        except ValueError:
            print("Please enter a whole number for the year.")

    # Get genres
    genres = get_genres()

    # Get rating
    while True:
        try:
            rating = float(input("Enter rating (0-10): "))

            if 0 <= rating <= 10:
                break

            print("Rating must be between 0 and 10.")

        except ValueError:
            print("Please enter a numeric rating.")

    # Call create_movie() to build the dictionary
    movie = create_movie(
        title,
        year,
        genres,
        rating
    )

    # Add the movie to the collection
    movie_collection.append(movie)


# 4. Sort the movies in-place by year
movie_collection.sort(
    key=lambda movie: movie["year"]
)


# Display the full collection sorted by year
display_movies(
    movie_collection,
    "All Movies Sorted by Year"
)


# Find the top 3 rated movies
top_movies = find_top_rated(
    movie_collection,
    3
)


# Display the top 3 rated movies
display_movies(
    top_movies,
    "Top 3 Rated Movies"
)


# ============================================================
# Menu
# ============================================================

while True:

    display_menu()

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_movie()

    elif choice == "2":
        display_movies(
            movie_collection,
            "MOVIE COLLECTION"
        )

    elif choice == "3":
        search_movies()

    elif choice == "4":
        calculate_average_rating()

    elif choice == "5":
        highest_rated_movie()

    elif choice == "6":
        print("\nThank you for using Movie Collection Manager!")
        break

    else:
        print("Invalid choice. Please select 1-6.")
