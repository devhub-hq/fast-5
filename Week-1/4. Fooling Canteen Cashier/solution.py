from itertools import combinations

def can_buy_funny(N, X, prices):
    # Check all combinations of exactly X snacks
    for combo in combinations(prices, X):
        if sum(combo) % 2 == 1:  # Odd total
            return True
    return False

if __name__ == "__main__":
    # Read inputs
    N, X = map(int, input().split())
    prices = list(map(int, input().split()))
    
    if can_buy_funny(N, X, prices):
        print("YES")
    else:
        print("NO")
