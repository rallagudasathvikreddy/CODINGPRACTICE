# Find the Runner-Up Score

## Platform
HackerRank

## Topic
Python Lists

## Concepts Learned
- Lists
- `for` loops
- Finding maximum value
- Finding second maximum value
- Conditional statements

## Approach

1. Store the scores in a list.
2. Find the highest score.
3. Traverse the list again.
4. Find the largest score that is smaller than the highest score.
5. Print the runner-up score.

## Key Pattern

```python
highest = scores[0]

for x in scores:
    if x > highest:
        highest = x

runner_up = -1

for x in scores:
    if x < highest and x > runner_up:
        runner_up = x
