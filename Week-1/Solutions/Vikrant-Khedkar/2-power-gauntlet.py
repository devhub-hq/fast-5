def can_powerup(n):
    return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    n = 9
    result = can_powerup(n)
    print("Yes" if result else "No")
