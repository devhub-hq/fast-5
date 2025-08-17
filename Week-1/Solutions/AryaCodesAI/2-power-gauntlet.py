# Check if n crystals can power up the gauntlet
# Power crystals must be exactly 1, 2, 4, 8, 16... (powers of 2)

n = int(input())

# A number is a power of 2 if it has exactly one bit set in binary
# Using bitwise operation: n & (n-1) == 0 for powers of 2
if n > 0 and (n & (n - 1)) == 0:
    print("Yes")
else:
    print("No")
