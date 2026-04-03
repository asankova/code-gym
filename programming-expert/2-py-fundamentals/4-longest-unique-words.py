#!/usr/bin/env python3
"""
N Longest Unique Words
Source: ProgrammingExpert - Fundamentals Assessment

Given a list of words and an integer n, return the n longest words
that appear only once in the list, sorted by length in descending order.

Example:
    get_n_longest_unique_words(["apple", "hi", "banana", "apple", "cherry"], 2)
    -> ["banana", "cherry"]
"""


def get_n_longest_unique_words(words: list[str], n: int) -> list[str]:
    """Return the n longest words that appear exactly once in the list."""
    unique: list[str] = [x for x in words if words.count(x) == 1]
    sorted_unique: list[str] = sorted(unique, key=lambda x: len(x), reverse=True)
    return sorted_unique[:n]


def main() -> None:
    """Test the get_n_longest_unique_words function."""
    assert get_n_longest_unique_words(
        ["apple", "hi", "banana", "apple", "cherry"], 2
    ) == ["banana", "cherry"]
    assert get_n_longest_unique_words(
        ["hello", "hello", "world"], 1
    ) == ["world"]
    assert get_n_longest_unique_words(
        ["a", "b", "c"], 2
    ) == ["a", "b"]
    assert get_n_longest_unique_words(
        ["same", "same", "same"], 1
    ) == []
    assert get_n_longest_unique_words([], 3) == []
    print("All tests passed!")


if __name__ == "__main__":
    main()