# Find missing tweet ID using sum formula
# Expected sum of 1..n = n*(n+1)/2
# Missing ID = Expected sum - Actual sum of remaining IDs

n = int(input())  # Total number of tweets
ids = list(map(int, input().split()))  # Remaining tweet IDs
print(sum(range(1, n+1)) - sum(ids))  # Calculate and print missing ID
