def sol(a:int,b:int)->int:
    even_a=a//2
    even_b=b//2
    return even_a*even_b+(a-even_a)*(b-even_b)


assert sol(1,1)==1
assert sol(2,3)==3
assert sol(4,6)==12
assert sol(8,9)==36
assert sol(2,2)==2
assert sol(3,3)==5
assert sol(5,5)==13
assert sol(10,10)==50
assert sol(1,10)==5
assert sol(7,8)==28
