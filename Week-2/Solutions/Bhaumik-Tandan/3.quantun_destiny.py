def sum_of_square_of_digits(n:int)->int:
    return sum(int(d)**2 for d in str(n))

def sol(n:int)->bool:
    slow=n
    fast=n
    while True:
        slow=sum_of_square_of_digits(slow)
        fast=sum_of_square_of_digits(sum_of_square_of_digits(fast))
        if fast==1:
            return 1
        if slow==fast:
            return 0
        


    


assert sol(0) == False
assert sol(1) == True
assert sol(10) == True
assert sol(1000) == True

assert sol(4) == False
assert sol(20) == False
assert sol(89) == False

assert sol(19) == True
assert sol(23) == True
assert sol(7) == True
assert sol(28) == True

assert sol(11) == False
assert sol(32) == True
assert sol(68) == True
assert sol(94) == True
assert sol(116) == False
assert sol(203) == True
assert sol(9999) == False

assert sol(1000000) == True
assert sol(44444444) == False
