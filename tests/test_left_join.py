import pytest
from hashmap_left_join.hashmap_left_join import left_join


def test_exists():
    assert left_join


def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }
    actual = left_join(synonyms, antonyms)
    expected = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", "None"],
        ["wrath", "anger", "delight"],

    ]

    assert actual == expected