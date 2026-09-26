# CODINGPRACTICE
HackerRank coding practice for CSE placement preparation
# Collections.Counter() – Shoe Shop

## Platform
HackerRank

## Topic
Python Collections – Counter

## Problem
Calculate the total amount earned by a shoe shop owner based on
available shoe sizes and customer purchases.

## Concepts Learned
- `collections.Counter`
- Frequency counting
- Dictionary-style access
- Updating inventory
- Loops and conditions

## Approach
1. Store the available shoe sizes using `Counter`.
2. Read each customer's requested shoe size and price.
3. Check whether the requested shoe size is available.
4. If available, add the price to the total earnings.
5. Decrease the stock of that shoe size by 1.

## Key Code Pattern

```python
from collections import Counter

stock = Counter(sizes)

if stock[size] > 0:
    money += price
    stock[size] -= 1
