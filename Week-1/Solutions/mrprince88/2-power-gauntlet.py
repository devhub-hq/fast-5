def solution(n):
    return "Yes" if n &(n-1)==0 and n != 0 else "No"