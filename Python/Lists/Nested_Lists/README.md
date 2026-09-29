# Nested Lists

## Platform
HackerRank

## Topic
Python Lists – Nested Lists

## Concepts Learned
- Nested lists
- `for` loops
- `float()`
- `set()`
- `sorted()`
- List comprehensions
- Filtering data

## Approach

1. Store each student's name and grade in a nested list.
2. Extract the grades.
3. Remove duplicate grades using `set()`.
4. Sort the grades.
5. Select the second-lowest grade.
6. Find all students having the second-lowest grade.
7. Sort their names alphabetically.
8. Print each name on a new line.

## Key Pattern

```python
grades = sorted(set(grade for name, grade in students))
second_lowest = grades[1]

names = sorted(
    name for name, grade in students
    if grade == second_lowest
)
