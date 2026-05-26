def solution(n):
    count_list = [0] * 10001
    
    for c_count in range(1, 141):  # 연속하는 수들의 개수
        for k in range(1, 10000):
            
            summation = (c_count * k + (c_count - 1 ) * c_count // 2)
            if summation > 10000: 
                break
            
            count_list[summation] += 1
            
    
    answer = count_list[n]
    return answer