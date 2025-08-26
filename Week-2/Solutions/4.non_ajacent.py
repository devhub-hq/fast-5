def maxSum(arr:list[int],index:int,sum:int,memo)->int:
    if index>=len(arr):
      return sum
    key=(index,sum)
    if memo.get(key):
        return memo.get(key)

    memo[key]=max(maxSum(arr,index+2,arr[index]+sum,memo),maxSum(arr,index+1,sum,memo))
    return memo[key]

def sol(arr:list[int])->int:
    return maxSum(arr,0,0,dict())



assert sol([5, 5, 10, 100, 10, 5]) == 110
assert sol([3, 2, 7, 10]) == 13
assert sol([3, 2, 5, 10, 7]) == 15
assert sol([]) == 0
assert sol([7]) == 7
assert sol([2, 1]) == 2
assert sol([2, 3]) == 3
assert sol([10, 1, 2, 10]) == 20
assert sol([1, 2, 3, 1]) == 4
assert sol([100, 1, 1, 100]) == 200
