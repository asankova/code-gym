#!/usr/bin/env python3
"""
Sort Employees
Source: ProgrammingExpert - Fundamentals Assessment

Given a list of employee tuples (name, age, salary) and a sort_by
parameter, return a new list sorted by the specified field.
Valid sort_by values are "name", "age", or "salary".

Example:
    sort_employees([("Alice", 30, 50000), ("Bob", 25, 60000)], "age")
    -> [("Bob", 25, 60000), ("Alice", 30, 50000)]
"""


def sort_employees(employees: list[tuple], sort_by: str) -> list[tuple]:
    """Sort a list of employee tuples by the specified field."""
    if sort_by == "name":
        return sorted(employees, key=lambda x: x[0])
    elif sort_by == "age":
        return sorted(employees, key=lambda x: x[1])
    else:
        return sorted(employees, key=lambda x: x[2])


def main() -> None:
    """Test the sort_employees function."""
    employees = [
        ("Alice", 30, 50000),
        ("Charlie", 20, 70000),
        ("Bob", 25, 60000),
    ]

    assert sort_employees(employees, "name") == [
        ("Alice", 30, 50000),
        ("Bob", 25, 60000),
        ("Charlie", 20, 70000),
    ]
    assert sort_employees(employees, "age") == [
        ("Charlie", 20, 70000),
        ("Bob", 25, 60000),
        ("Alice", 30, 50000),
    ]
    assert sort_employees(employees, "salary") == [
        ("Alice", 30, 50000),
        ("Bob", 25, 60000),
        ("Charlie", 20, 70000),
    ]
    assert sort_employees([], "name") == []
    print("All tests passed!")


if __name__ == "__main__":
    main()