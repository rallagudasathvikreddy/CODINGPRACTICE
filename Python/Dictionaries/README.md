# Finding the Percentage

## Problem

Given the names and marks of several students, store the information in a dictionary and calculate the average marks of a student whose name is provided as a query.

The average should be printed with exactly **2 decimal places**.

## Approach

1. Read the number of students.
2. Create a dictionary to store each student's name and marks.
3. Read the student's name and marks.
4. Store the marks as a list of floating-point numbers.
5. Read the `query_name`.
6. Retrieve the marks of the requested student.
7. Calculate the average using:

   `Average = Sum of Marks / Number of Marks`

8. Print the result using `:.2f` to display exactly two decimal places.

## Python Concepts Used

- Dictionary
- Lists
- `input()`
- `split()`
- `map()`
- `float()`
- `sum()`
- `len()`
- f-string formatting
- List unpacking using `*`

## Code

```python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    marks = student_marks[query_name]
    average = sum(marks) / len(marks)

    print(f"{average:.2f}")
