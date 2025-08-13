# Problem 5: Late Night Pizza Party

## Problem Statement
Count ways to climb n steps taking 1 or 2 steps at a time.

## Approach
**Dynamic Programming (Fibonacci Pattern)**
- Each step can be reached from (step-1) or (step-2)
- Ways[n] = Ways[n-1] + Ways[n-2]

## Logic
```
Base cases:
- 1 step: 1 way (1)
- 2 steps: 2 ways (1+1, 2)

For n ≥ 3:
- To reach step n: come from (n-1) or (n-2)
- Total ways = ways(n-1) + ways(n-2)

Example n=3:
- From step 2: take 1 step
- From step 1: take 2 steps  
- Total: 2 + 1 = 3 ways
```

## Time Complexity: O(n)
## Space Complexity: O(1)

## Optimization
- Use two variables instead of array
- Classic Fibonacci optimization