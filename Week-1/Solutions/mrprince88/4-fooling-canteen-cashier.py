def solution(n,x,arr):
    even, odd = 0, 0
    
    for i in range(n):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
        
    if odd == 0:
        return "No"
    
    else:
        if odd % 2 == 0:
            odd -= 1
        if x % 2 == 0 and even == 0:
            return "No"
        elif even + odd >= x:
            return "Yes"
        else:
            return "No"