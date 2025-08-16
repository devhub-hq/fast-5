def canPowerup(n):
    # A number is a power of 2 if it has only one bit set in binary
    return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    n = int(input())
    if canPowerup(n):
        print("Yes")
    else:
        print("No")
