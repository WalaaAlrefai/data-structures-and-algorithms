from merge_sort.merge_sort import merge_sort


def test_empty_array():
    actual = merge_sort([])
    expected = []
    actual == expected


def test_positive_numbers():
    actual = merge_sort([5, 7, 9, 6, 1, 7, 4])
    expected = [1, 4, 5, 5, 6, 7, 7, 9]
    actual == expected


def test_negative_numbers():
    actual = merge_sort([-1, -5, -9, -7])
    expected = [-9, -7, -5, -1]
    actual == expected


def test_mixed_numbers():
    actual = merge_sort([0, 5, 2, -1, 7, 1000])
    expected = [-1, 0, 2, 5, 7, 1000]
    actual == expected