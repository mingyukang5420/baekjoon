import sys
from copy import deepcopy


def read_input_filestream() -> None:
    """테스트를 위해 파일에서 입력을 읽어옵니다.

    현재 파일명에서 문제 번호를 추출하여 input_{번호}.txt 파일을 엽니다.
    """
    QNUM = __file__.split(".")[0].split("_")[-1]
    sys.stdin = open(f"input_{QNUM}.txt")


def get_board() -> list[list[int]]:
    # 보드 크기 입력
    n = int(sys.stdin.readline())

    # 보드 입력
    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))

    return board


def move_left(board: list[list[int]]) -> list[list[int]]:
    # 결과로 쓸 보드 생성
    new_board = deepcopy(board)
    # 보드 길이
    n = len(board)

    for i in range(n):
        # 0이 아닌 숫자 모으기
        nums = [num for num in new_board[i] if num != 0]

        # 합치기
        merged = []
        skip = False
        for j in range(len(nums)):
            if skip:
                skip = False
                continue

            # 현재가 다음과 같고, 경계를 넘지 않았다면
            if j + 1 < len(nums) and nums[j] == nums[j + 1]:
                merged.append(nums[j] * 2)
                skip = True  # 다음 칸은 이미 합쳐짐
            else:
                merged.append(nums[j])

        # 좌로 밀착하고 나머지 0으로 채우기
        new_board[i] = merged + ([0] * (n - len(merged)))

    return new_board


def rotate_90(board: list[list[int]]) -> list[list[int]]:
    """시계방향 90도 회전하기
    기존 row는 순방향 그대로 new_col로 보내고
    기존 col은 역방향으로 new_row로 보내기
    """
    n = len(board)
    return [[board[n - 1 - j][i] for j in range(n)] for i in range(n)]


def move_right(board: list[list[int]]) -> list[list[int]]:
    board = rotate_90(rotate_90(board))  # 180도
    board = move_left(board)
    board = rotate_90(rotate_90(board))  # 다시 180도
    return board


def move_up(board: list[list[int]]) -> list[list[int]]:
    board = rotate_90(rotate_90(rotate_90(board)))  # 반시계 90도
    board = move_left(board)
    board = rotate_90(board)  # 시계 90도로 원위치
    return board


def move_down(board: list[list[int]]) -> list[list[int]]:
    board = rotate_90(board)  # 시계 90도
    board = move_left(board)
    board = rotate_90(rotate_90(rotate_90(board)))  # 반시계 90도로 원위치
    return board


def get_max(board):
    return max(max(row) for row in board)


def dfs(board, depth):
    global answer

    if depth > 5:
        answer = max(answer, get_max(board))
        return

    # 4방향 모두 시도
    for move in [move_up, move_down, move_left, move_right]:
        new_board = move(board)
        dfs(new_board, depth + 1)


def main(board):
    global answer

    # DFS 실행
    dfs(board, 1)

    # 결과 출력
    print(answer)


if __name__ == '__main__':
    # read_input_filestream()
    arr = get_board()
    answer = 0  # 전역변수 초기화
    main(arr)
