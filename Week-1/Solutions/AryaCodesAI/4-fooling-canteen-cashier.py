# Fooling Canteen Cashier - Check if we can buy exactly X snacks with odd total
n, x = map(int, input().split())
prices = list(map(int, input().split()))

# Count odd and even prices
odd = sum(1 for p in prices if p % 2)
even = n - odd

# Can make odd sum with exactly X snacks if:
# 1. We have at least one odd price
# 2. We can select odd number of odd prices (1, 3, 5...) within X items
if odd > 0 and (x <= n) and (odd >= 1 if x % 2 == 1 else odd >= 1 and even >= 1):
    print("YES")
else:
    print("NO")
