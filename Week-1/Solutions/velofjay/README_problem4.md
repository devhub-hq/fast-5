# Problem 4: Fooling Canteen Cashier

## Problem Statement
Check if we can select exactly X items with an odd total sum ("funny" total).

## Approach
**Odd/Even Mathematics**
- Odd sum requires odd count of odd numbers
- Analyze based on X being odd or even

## Logic
```
Key insight: Sum is odd ⟺ odd count of odd numbers

Case 1: X is odd
- Need odd count of odd prices (1, 3, 5, ...)
- Possible if at least 1 odd price exists

Case 2: X is even  
- Need odd count of odd prices (1, 3, 5, ...)
- Possible if: 1 ≤ odd_count < total_items
```

## Time Complexity: O(n)
## Space Complexity: O(1)

## Example
- Prices: [1, 2, 3, 4], X = 3
- Odd prices: 2 (positions 0, 2)
- X is odd, odd prices exist → YES