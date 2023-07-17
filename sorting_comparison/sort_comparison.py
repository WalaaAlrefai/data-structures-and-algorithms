class Movie:
    def __init__(self, title, year, genres):
        self.title = title
        self.year = year
        self.genres = genres

def sort_by_recent_year(movies):
    return sorted(movies, key=lambda movie: movie.year, reverse=True)

def remove_leading_articles(title):
    articles = ["A ", "An ", "The "]
    for article in articles:
        if title.startswith(article):
            return title[len(article):]
    return title

def sort_alphabetically_ignore_articles(movies):
    return sorted(movies, key=lambda movie: remove_leading_articles(movie.title))

# Test data
movies = [
    Movie("The Shawshank Redemption", 1994, ["Drama"]),
    Movie("Pulp Fiction", 1994, ["Crime", "Drama"]),
    Movie("A Clockwork Orange", 1971, ["Crime", "Drama", "Sci-Fi"]),
    Movie("Annie Hall", 1977, ["Comedy", "Romance"]),
    Movie("Fight Club", 1999, ["Drama"]),
    Movie("The Help", 2009, ["Drama"])
]

# Sort movies by recent year
recent_year_sorted = sort_by_recent_year(movies)
print("Sort movies by recent year")
for movie in recent_year_sorted:
    print(movie.title, movie.year)
print()

# Sort movies alphabetically ignoring leading articles
alphabetical_sorted = sort_alphabetically_ignore_articles(movies)
print("Sort movies alphabetically ignoring leading articles")
for movie in alphabetical_sorted:
    print(movie.title, movie.year)
