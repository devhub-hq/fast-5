# memomisation
def sol(n:int,memo=dict())->int:
    if n<0:
        return 0
    if n==0:
        return 1
    if memo.get(n):
        return memo[n]
    memo[n]=sol(n-1)+sol(n-2)
    return memo[n]


# tabutaion
def sol(n:int)->int:
    dp=[1,1]

    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]


assert sol(0) == 1
assert sol(1) == 1
assert sol(2) == 2
assert sol(3) == 3
assert sol(4) == 5
assert sol(5) == 8
assert sol(6) == 13
assert sol(7) == 21
assert sol(8) == 34
assert sol(9) == 55
assert sol(10) == 89
assert sol(11) == 144
assert sol(12) == 233
assert sol(13) == 377
assert sol(14) == 610
assert sol(15) == 987
assert sol(16) == 1597
assert sol(17) == 2584
assert sol(18) == 4181
assert sol(19) == 6765
assert sol(20) == 10946
assert sol(25) == 121393
assert sol(30) == 1346269
assert sol(35) == 14930352
assert sol(40) == 165580141
assert sol(45) == 1836311903
assert sol(50) == 20365011074
