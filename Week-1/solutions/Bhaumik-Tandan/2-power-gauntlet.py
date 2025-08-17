
def canPowerup(n:int)->bool:
    return not (n & (n-1))

assert canPowerup(9)==False
assert canPowerup(16)==True
