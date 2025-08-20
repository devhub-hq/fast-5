from itertools import combinations

def is_funny_total(N, X, prices):
    for combo in combinations(prices, X):
        total = sum(combo)
        if total % 2 != 0:
            return True
    return False

if __name__ == "__main__":
    N = 4
    X = 3
    prices = [1, 2, 3, 4]
    result = is_funny_total(N, X, prices)
    print("YES" if result else "NO")
