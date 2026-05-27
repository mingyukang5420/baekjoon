def solution(board):
    
    length = len(board)
    
    is_safe = [[True for _ in range(length)] for _ in range(length)]
    
    # directions 본인, 12시부터 시계방향
    dr = [0, -1, -1, 0, 1, 1,  1,  0, -1]
    dc = [0,  0,  1, 1, 1, 0, -1, -1, -1]
    
    
    for r in range(length):
        for c in range(length):
            
            if board[r][c] == 1:
                for _dir in range(9):
                    nr = r + dr[_dir]
                    nc = c + dc[_dir]
                    
                    if 0 <= nr < length and 0 <= nc < length:
                        is_safe[nr][nc] = False
                        
    answer = 0
            
    for r in range(length):
        for c in range(length):
            
            if is_safe[r][c] == True:
                answer += 1
    
    return answer