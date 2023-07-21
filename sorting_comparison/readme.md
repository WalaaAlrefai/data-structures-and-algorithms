# Sorting comparison.


## Challenge 28:  Code Challenge 

## [Code](./sort_comparison.py)
## [tests](../tests/test_sorting.py)


## -Assignment

write functions which sort domain objects. Your functions will receive an array of Movie objects. Each Movie object has a title (string), a year (number), and a list of genres (array of strings). One function will sort the movies by most recent year first. One function will sort the movies, alphabetical by title, but will ignore any leading “A”s, “An”s, or “The”s. Test outputs for these functions, and an array of sample data, have been provided in test and movies.

In the second half of the code challenge, you will write tests for your comparator functions. This may necessitate refactoring the code you wrote in part one. Your tests will need to call the comparator functions directly, and make assertions about the response values given test inputs.

## -Approach & Efficiency

>Big(O)
>>- Time  == O(n)
>>- Space == O(n)


## -Solution
- Algorithm
1. define Movie Class that have 3 properties " title ,year ,genre "
2. define 3 methods

   - sort_by_recent_year
   - remove_leading_articles
   - sort_alphabetically_ignore_articles

