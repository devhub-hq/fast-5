def count_ways(n):
    """
    Count the number of ways to climb n stairs taking 1 or 2 steps at a time.
    
    This is a classic dynamic programming problem equivalent to finding the nth Fibonacci number.
    The recurrence relation is: ways(n) = ways(n-1) + ways(n-2)
    
    Args:
        n (int): Number of stairs to climb
        
    Returns:
        int: Number of distinct ways to climb the stairs
    """
    # Handle edge cases
    if n <= 0:
        return 0
    
    # Initialize base cases
    # ways(1) = 1 (only one way: single step)
    # ways(2) = 2 (two ways: 1+1 or 2)
    a, b = 1, 1
    
    # Iterate from 3 to n, building up the solution
    # a and b represent ways(i-2) and ways(i-1) respectively
    for _ in range(n-1):
        a, b = b, a + b
    
    # b now contains ways(n)
    return b

# Read input from stdin
n = int(input())

# Calculate and print the result
print(count_ways(n))
