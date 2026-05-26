def solution(s):
    numbers = list(map(int, s.split(" ")))
    # print(f"[DEBUG] numbers: {numbers}")
    maximum = max(numbers)
    minimum = min(numbers)
    
    answer = ' '.join([str(minimum),str(maximum)])
    
    return answer