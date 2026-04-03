#!/usr/bin/env python3
"""
Caesar Cipher
Source: ProgrammingExpert - Fundamentals Assessment

Given a string and an offset, return a new string where each letter
is shifted backward in the alphabet by the offset amount. Non-letter
characters are left unchanged. The shift wraps around the alphabet.

Example:
    caesar_cipher("hello", 1) -> "gdkkn"
    caesar_cipher("ABC", 3) -> "XYZ"
"""


def caesar_cipher(string: str, offset: int) -> str:
    """Shift each letter in the string backward by the given offset."""
    result: str = ""
    for char in string:
        if char.isupper():
            result += chr((ord(char) - ord("A") - offset) % 26 + ord("A"))
        elif char.islower():
            result += chr((ord(char) - ord("a") - offset) % 26 + ord("a"))
        else:
            result += char
    return result


def main() -> None:
    """Test the caesar_cipher function."""
    assert caesar_cipher("hello", 1) == "gdkkn"
    assert caesar_cipher("ABC", 3) == "XYZ"
    assert caesar_cipher("abc", 26) == "abc"
    assert caesar_cipher("Hello, World!", 5) == "Czggj, Rjmgy!"
    assert caesar_cipher("", 10) == ""
    assert caesar_cipher("123!@#", 5) == "123!@#"
    print("All tests passed!")


if __name__ == "__main__":
    main()