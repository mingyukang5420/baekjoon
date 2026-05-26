def solution(n):
    
    idx = 0
    former = 1
    latter = 2
    
    if n == 1:
        answer = 1
        return answer
        
    elif n == 2:
        answer = 2
        return answer
        
    while(idx < n-2):
        idx += 1
        _next = former + latter

        former = latter
        latter = _next
            
    
    answer = _next % 1234567
    
    return answer