def read_parameters():
    N, M, T = map(int, sys.stdin.readline().split())
    K, a, b = map(int, sys.stdin.readline().split())

    return N, M, T, K, a, b


def read_input(N, M):
    arr = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        given_row = sys.stdin.readline().strip()
        for j in range(M):
            if given_row[j] == '*':
                arr[i][j] = True

    return arr


def count_surround_area(row, col, arr):
    """
    타겟 row, col 주변 K 만큼의 정사각형에서 생존 타일 갯수를 센다
    Args:
        row (int): 타겟 행
        col (int): 타겟 열
        arr (int): 현재 생명 상황

    Returns:
        cnt (int): 주변 생존 타일 수

    """

    global N, M, K
    cnt = 0
    for searching_row in range(row - K, row + (K + 1)):
        if 0 <= searching_row < N:

            for searching_col in range(col - K, col + (K + 1)):
                if 0 <= searching_col < M:

                    if arr[searching_row][searching_col] is True \
                            and not (searching_row == row and searching_col == col):
                        cnt += 1

    return cnt


def get_summation_matrix(N, M, arr):
    result = [[0 for _ in range(M)] for _ in range(N)]

    for r in range(N):
        for c in range(M):
            result[r][c] = count_surround_area(r, c, arr)

    return result


def check_next_status(row, col, arr, accumulated_arr):
    """
    확인을 원하는 row, col을 입력하고 현재 arr 상태를 입력하면 다음 상황에서 살아남을지 여부를 반환

    Args:
        row (int): 확인을 원하는 행
        col (int): 확인을 원하는 열
        arr (list[list[bool]]): 현재 생명상태

    Return:
        is_alive (bool): 다음 시간에서 생존 여부

    """
    global a, b

    cnt = accumulated_arr[row][col]
    live_state = arr[row][col]

    is_alive = True if live_state else False

    if live_state:
        if a <= cnt and cnt <= b:
            is_alive = True
        else:
            is_alive = False

    else:
        if a < cnt and cnt <= b:
            is_alive = True

    return is_alive


def print_output(arr):
    global N, M

    for r in range(N):
        output_row = ""
        for c in range(M):
            if arr[r][c]:
                output_row = output_row + "*"
            else:
                output_row = output_row + "."

        print(output_row)


def main(N, M, T, K, a, b, arr):
    """
    T시점 마다 생명 상태를 판단하고 관측 완료 시점의 생명 상태를 반환
    Args:
        N (int): 배열 가로 크기, 1 <= N <= 100
        M (int): 배열 세로 크기, 1 <= M <= 100
        T (int): 관측할 시간, 1 <= T <= 300
        K (int): 주변 범위, 1 <= K <= max(N, M)
        a (int): 생명 판단 하계, 1 <= a < (2K + 1) ^ 2
        b (int): 생명 판단 상계, 1 <= b < (2K + 1) ^ 2
        arr (list[list[bool]]): 초기 생명 상태

    Returns:
        T시간 이후 생명 상태 반환

    """

    from copy import deepcopy

    next_arr = deepcopy(arr)
    for time in range(1, T + 1):
        accumulated_arr = get_summation_matrix(N, M, arr)

        for row in range(N):
            for col in range(M):
                next_arr[row][col] = check_next_status(row, col, arr, accumulated_arr)

        arr = deepcopy(next_arr)

    return arr


if __name__ == "__main__":
    import sys
    N, M, T, K, a, b = read_parameters()
    given_arr = read_input(N, M)
    ans = main(N, M, T, K, a, b, given_arr)
    print_output(ans)
