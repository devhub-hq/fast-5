def sol(arr:list[int])->int:
    n=len(arr)
    if n==0:return 0
    if n==1:return arr[0]
    dp=[0]*n
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+arr[i])
    return dp[-1]


assert sol([5,5,10,100,10,5])==110
assert sol([3,2,7,10])==13
assert sol([3,2,5,10,7])==15
assert sol([])==0
assert sol([7])==7
assert sol([2,1])==2
assert sol([2,3])==3
assert sol([10,1,2,10])==20
assert sol([1,2,3,1])==4
assert sol([100,1,1,100])==200
