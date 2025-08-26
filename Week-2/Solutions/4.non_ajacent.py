def maxSum(arr:list[int],index:int,sum:int)->int:
    if index>=len(arr):
        return sum
    return max(maxSum(arr,index+2,arr[index]+sum),maxSum(arr,index+1,sum))

def sol(arr:list[int])->int:
    return maxSum(arr,0,0)



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
