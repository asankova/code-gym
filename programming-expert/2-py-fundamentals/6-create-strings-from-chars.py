#!/usr/bin/env python3
"""
Create Strings From Characters
Source: ProgrammingExpert - Fundamentals Assessment

Given a dictionary of character frequencies and two strings, determine
whether the available characters are sufficient to create both strings,
only one, or neither — without reusing characters.

Returns:
    2 - both strings can be created together
    1 - either string can be created individually
    0 - neither string can be created

Example:
    frequencies = {"h": 2, "e": 1, "l": 1, "o": 2, "w": 1, "r": 1, "d": 1}
    create_strings_from_characters(frequencies, "hello", "world") -> 1
"""

from collections import Counter


def create_strings_from_characters(
    frequencies: dict[str, int], string1: str, string2: str
) -> int:
    """Check if frequency of characters can build one or both strings."""
    needed1: Counter = Counter(string1)
    needed2: Counter = Counter(string2)

    def can_build(needed: Counter) -> bool:
        for char, count in needed.items():
            if frequencies.get(char, 0) < count:
                return False
        return True

    if can_build(needed1 + needed2):
        return 2
    if can_build(needed1) or can_build(needed2):
        return 1
    return 0


def main() -> None:
    """Test the create_strings_from_characters function."""
    assert create_strings_from_characters(
        {"h": 2, "e": 1, "l": 1, "o": 2, "w": 1, "r": 1, "d": 1},
        "hello", "world"
    ) == 1
    assert create_strings_from_characters(
        {"h": 2, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1},
        "hello", "world"
    ) == 2
    assert create_strings_from_characters(
        {"a": 1},
        "hello", "world"
    ) == 0
    assert create_strings_from_characters(
        {}, "hello", "world"
    ) == 0
    assert create_strings_from_characters(
        {"h": 1, "e": 1, "l": 2, "o": 1},
        "hello", "world"
    ) == 1
    print("All tests passed!")


if __name__ == "__main__":
    main()