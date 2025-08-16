def recSol(index:int,running_sum:int,left_count:int,prices:list[int])->bool:
    if left_count==0:
      if running_sum%2==1:
        return True
      else:
         return False
    if left_count>len(prices)-index:
        return False
    
    picked=recSol(index+1,running_sum+prices[index],left_count-1,prices)
    if picked:
        return True
    not_picked=recSol(index+1,running_sum,left_count,prices)
    return not_picked

def sol(n:int,x:int,prices:list[int])->bool:
    return recSol(0,0,x,prices)

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
