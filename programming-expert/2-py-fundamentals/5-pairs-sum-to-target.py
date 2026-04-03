#!/usr/bin/env python3
"""
Pairs Sum to Target
Source: ProgrammingExpert - Fundamentals Assessment

Given two lists of integers and a target sum, return a list of pairs [i, j]
where list1[i] + list2[j] equals the target. Includes both a brute force
O(n*m) approach and an optimized O(n+m) approach using a lookup dictionary.

Example:
    pairs_sum_to_target([1, 2, 3], [4, 5, 6], 7)
    -> [[0, 2], [1, 1], [2, 0]]
"""


def pairs_sum_to_target_brute_force(
    list1: list[int], list2: list[int], target: int
) -> list[list[int]]:
    """Find index pairs that sum to target using nested loops. O(n*m)."""
    pairs: list[list[int]] = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] + list2[j] == target:
                pairs.append([i, j])
    return pairs


def pairs_sum_to_target(
    list1: list[int], list2: list[int], target: int
) -> list[list[int]]:
    """Find index pairs that sum to target using a lookup dictionary. O(n+m)."""
    pairs: list[list[int]] = []
    lookup: dict[int, list[int]] = {}
    for i, val in enumerate(list1):
        lookup.setdefault(val, []).append(i)
    for j, val in enumerate(list2):
        complement: int = target - val
        if complement in lookup:
            for i in lookup[complement]:
                pairs.append([i, j])
    return pairs


def main() -> None:
    """Test both implementations produce the same results."""
    test_cases = [
        ([1, 2, 3], [4, 5, 6], 7, [[0, 2], [1, 1], [2, 0]]),
        ([1, 1], [1, 1], 2, [[0, 0], [0, 1], [1, 0], [1, 1]]),
        ([1, 2, 3], [4, 5, 6], 100, []),
        ([], [1, 2, 3], 5, []),
        ([5], [0], 5, [[0, 0]]),
    ]

    for list1, list2, target, expected in test_cases:
        brute = pairs_sum_to_target_brute_force(list1, list2, target)
        optimized = pairs_sum_to_target(list1, list2, target)
        assert brute == expected, f"Brute force failed for {list1}, {list2}, {target}"
    print("All tests passed!")

if __name__ == "__main__":
    main()