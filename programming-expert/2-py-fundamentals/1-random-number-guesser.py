#!/usr/bin/env python3
"""
Random Number Guesser
Source: ProgrammingExpert - Fundamentals Assessment

The program asks the user to define a range (start and end),
generates a random number within that range, and then prompts
the user to guess the number. It tracks how many attempts it
takes to guess correctly.
"""

import random


def get_number(prompt: str) -> int:
    """Repeatedly prompt the user until they enter a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_start(prompt: str = "Enter the start of the range: ") -> int:
    """Get the start of the range from the user."""
    return get_number(prompt)


def get_end(start: int, prompt: str = "Enter the end of the range: ") -> int:
    """Get the end of the range from the user, must be greater than start."""
    while True:
        try:
            end = int(input(prompt))
            assert end > start
            return end
        except ValueError:
            print("Please enter a valid number.")
        except AssertionError:
            print("Please enter a valid number.")


def get_guess(prompt: str = "Guess a number: ") -> int:
    """Get a guess from the user."""
    return get_number(prompt)


def main() -> None:
    """Run the number guessing game."""
    start: int = get_start()
    end: int = get_end(start)
    number: int = random.randint(start, end)

    attempts: int = 1
    while True:
        guess: int = get_guess()
        if guess == number:
            break
        attempts += 1

    print(f"You guessed the number in {attempts} {'attempt' if attempts == 1 else 'attempts'}")


if __name__ == "__main__":
    main()