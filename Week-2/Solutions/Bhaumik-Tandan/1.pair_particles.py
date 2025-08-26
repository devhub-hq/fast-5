def sol(arr:list[int])->int:
    ans=0
    for i in arr:
        ans^=i
    return ans


assert sol([101, 7, 42, 101, 42]) == 7
assert sol([5]) == 5
assert sol([2, 3, 2]) == 3
assert sol([9, 1, 9, 1, 8]) == 8
assert sol([0, 4, 4]) == 0
assert sol([0, 0, 11]) == 11
assert sol([-5, 10, -5]) == 10
assert sol([-1, -1, -2]) == -2
assert sol([7, -3, 7, -3, -99]) == -99
assert sol([42, 13, 42, 99, 100, 99, 13, 100, 77]) == 77
assert sol([101, 202, 303, 202, 404, 404, 101]) == 303
assert sol([10**9, 123456, 10**9, 123456, -777]) == -777