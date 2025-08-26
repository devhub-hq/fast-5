def sol(a:int,b:int)->int:
    distance=abs(a-b)
    return distance//10+(distance%10!=0)


assert sol(5, 15) == 1
assert sol(20, 4) == 2
assert sol(30, 30) == 0

assert sol(0, 0) == 0
assert sol(5, 6) == 1
assert sol(5, 15) == 1
assert sol(5, 16) == 2
assert sol(10, 20) == 1
assert sol(10, 21) == 2

assert sol(15, 5) == 1
assert sol(-5, 5) == 1
assert sol(-5, 16) == 3
assert sol(-10, -35) == 3

assert sol(7, 28) == 3
assert sol(7, 16) == 1
assert sol(100, 109) == 1
assert sol(100, 181) == 9
assert sol(100, 189) == 9
