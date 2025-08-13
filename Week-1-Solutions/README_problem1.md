# Problem 1: Why Yacine Got Fired

## Problem Statement
Find the missing tweet ID from a sequence of consecutive integers starting from 1.

## Approach
**Mathematical Sum Formula**
- Use the formula for sum of first n natural numbers: `n * (n + 1) / 2`
- Calculate expected sum and actual sum
- The difference is the missing number

## Logic
```
Expected sum = 1 + 2 + 3 + ... + n = n * (n + 1) / 2
Actual sum = sum of remaining IDs
Missing ID = Expected sum - Actual sum
```

## Time Complexity: O(n)
## Space Complexity: O(1)

## Example
- Total tweets: 5, Remaining: [1, 2, 5, 3]
- Expected: 5 * 6 / 2 = 15
- Actual: 1 + 2 + 5 + 3 = 11
- Missing: 15 - 11 = 4