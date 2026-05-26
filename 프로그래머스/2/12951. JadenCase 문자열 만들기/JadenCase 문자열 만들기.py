def solution(s):
    
    length = len(s)
    was_blank = True
    result = ""
    
    for idx in range(length):
        current = s[idx]
        
        if current == " ":
            # if was_blank == False:
            result += current
            was_blank = True
            continue
            
        else:
            if was_blank:
                result += current.upper()
            else:
                result += current.lower()
                
            was_blank = False
    
    answer = result
    return answer