def solution(s):
    
    length = len(s)
    stack = []
    
    for idx in range(length):
        current = s[idx]
        
        if current == ")":
            try: prev = stack.pop()
            except: return False
            
            if prev != "(":
                return False
            
        else:
            stack.append(current)
    
    if len(stack) > 0:
        return False

    return True