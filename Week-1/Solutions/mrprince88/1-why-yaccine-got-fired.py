def solution(arr,n):
        
    xor=0
    
    for i in range(1,n+1):
        xor ^= i
        
    for num in arr:
        xor ^= num
        
    return xor
