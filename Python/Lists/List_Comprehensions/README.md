# List Comprehensions

## Platform
HackerRank

## Topic
Python Lists – List Comprehensions

## Concepts Learned
- List comprehensions
- Nested loops
- Conditional filtering
- 3D coordinates
- `range()`

## Approach

Generate all possible `[i, j, k]` coordinates using three
`for` clauses inside a list comprehension.

Only keep coordinates where:

`i + j + k != n`

## Key Pattern

```python
result = [
    [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n
]
