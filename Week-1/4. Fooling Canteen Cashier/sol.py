def sol(n:int,x:int,prices:list[int])->bool:
    odd_count=0
    even_count=0
    for i in prices:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    t=1

    while t<=odd_count and t<=x:
        if t+even_count>=x:
            return True
        t+=2
    return False
assert sol(4, 3, [1, 2, 3, 4]) == True
assert sol(4, 2, [2, 4, 6, 8]) == False
assert sol(1, 1, [5]) == True
assert sol(1, 1, [8]) == False
assert sol(5, 2, [2, 4, 6, 7, 9]) == True
assert sol(3, 3, [1, 2, 4]) == True
assert sol(3, 3, [2, 2, 4]) == False
assert sol(4, 3, [1, 3, 5, 7]) == True
assert sol(4, 2, [1, 3, 5, 7]) == False
assert sol(6, 4, [10, 20, 30, 5, 8, 12]) == True
