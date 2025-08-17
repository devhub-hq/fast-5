def solution(str):
    seen=set()
    
    for char in str:
        if char in seen:
            return "No"
        
        seen.add(char)
        
    return "Yes"