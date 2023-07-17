import pytest
from sorting_comparison.sort_comparison import Movie, sort_by_recent_year, sort_alphabetically_ignore_articles

@pytest.fixture
def sample_movies():
    return [
        Movie("The Shawshank Redemption", 1994, ["Drama"]),
        Movie("Pulp Fiction", 1994, ["Crime", "Drama"]),
        Movie("A Clockwork Orange", 1971, ["Crime", "Drama", "Sci-Fi"]),
        Movie("Annie Hall", 1977, ["Comedy", "Romance"]),
        Movie("Fight Club", 1999, ["Drama"]),
        Movie("The Help", 2009, ["Drama"])
    ]

def test_sort_by_recent_year(sample_movies):
    sorted_movies = sort_by_recent_year(sample_movies)
    years = [movie.year for movie in sorted_movies]
    assert years == [2009, 1999, 1994, 1994, 1977, 1971]

def test_sort_alphabetically_ignore_articles(sample_movies):
    sorted_movies = sort_alphabetically_ignore_articles(sample_movies)
    titles = [movie.title for movie in sorted_movies]
    assert titles == ["Annie Hall","A Clockwork Orange","Fight Club","The Help", "Pulp Fiction", "The Shawshank Redemption"]