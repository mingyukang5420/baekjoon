def solution(wallpaper):
    row_set = set()
    col_set = set()
    
    rows = len(wallpaper)
    cols = len(wallpaper[0])
    
    for r in range(rows):
        for c in range(cols):
            if wallpaper[r][c] == "#":
                row_set.add(r)
                col_set.add(c)
                
    lux = min(row_set)
    luy = min(col_set)
    rdx = max(row_set) + 1
    rdy = max(col_set) + 1
    
    answer = [lux, luy, rdx, rdy]
    return answer