n = int(input("Enter total number of tweets before loss: "))
ids = list(map(int, input("Enter remaining tweet IDs separated by space: ").split()))
expected_sum = n * (n + 1) // 2
actual_sum = sum(ids)
missing_id = expected_sum - actual_sum
print("The missing tweet ID is:", missing_id)
