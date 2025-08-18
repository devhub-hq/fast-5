def can_make_funny_total(prices, x):
    total_sum = sum(prices)
    if x % 2 == 1:
        return any(price % 2 == 1 for price in prices)
    else:
        odd_count = sum(1 for price in prices if price % 2 == 1)
        return odd_count >= 1 and odd_count != len(prices)

prices = [1, 2, 3, 4]
x = 3
print("YES" if can_make_funny_total(prices, x) else "NO")