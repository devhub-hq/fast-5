def canPowerup(n):
    return n > 0 and (n & (n - 1)) == 0

print("Yes" if canPowerup(8) else "No")
print("Yes" if canPowerup(9) else "No")