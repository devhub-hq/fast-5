# Problem 2: Power Gauntlet

## Problem Statement
Check if a number is a power of 2 (1, 2, 4, 8, 16, ...).

## Approach
**Bit Manipulation Trick**
- Powers of 2 have exactly one bit set in binary
- Use the property: `n & (n-1) == 0` for powers of 2

## Logic
```
Power of 2 examples:
8  = 1000 (binary)
7  = 0111 (binary)
8 & 7 = 0000 = 0 ✓

Non-power of 2:
9  = 1001 (binary)  
8  = 1000 (binary)
9 & 8 = 1000 ≠ 0 ✗
```

## Time Complexity: O(1)
## Space Complexity: O(1)

## Edge Case
- Must check `n > 0` to exclude 0