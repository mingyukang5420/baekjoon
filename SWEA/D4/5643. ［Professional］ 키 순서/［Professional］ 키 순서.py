T = int(input())
outputs = []

for tc in range(1, T + 1):
    N = int(input())
    M = int(input())

    # 각 학생이 '자신보다 큰 학생들'을 비트마스크로 저장
    rows = [0] * N

    for _ in range(M):
        small, big = map(int, input().split())
        small -= 1
        big -= 1
        rows[small] |= 1 << big  # small행 big열 관계 기록

    # reach[i] : 학생 i가 도달할 수 있는 모든 학생들 (직접/간접 포함)
    reach = rows[:]

    # power : 이번 단계에서 새로 확장할 경로들, 행렬의 거듭제곰
    power = rows[:]

    # 최대 N-1번 곱하면 모든 경로를 탐색 가능
    for _ in range(N - 1):
        new_power = [0] * N
        for i in range(N):
            mask = power[i]
            if mask == 0:
                continue
            temp = 0
            # mask의 각 비트(=학생 j)에 대해
            while mask:
                # least significant bit, MSB와 반대
                lsb = mask & -mask  # 가장 낮은 1비트 추출
                j = (lsb.bit_length() - 1)  # j = 연결된 학생 번호
                temp |= rows[j]  # j가 도달하는 학생들을 추가
                mask ^= lsb  # 비트 제거, lsb가 mask & -mask기 때문에 여기선 xor연산이 빼기와 같음
            new_power[i] = temp

        # 새로 찾은 경로를 reach에 추가
        updated = False
        for i in range(N):
            new_bits = new_power[i] & (~reach[i])  # reach에 없고 new_power에 있는 애들
            if new_bits:
                reach[i] |= new_bits  # 새로 업뎃하고
                updated = True  # flag 갱신
        power = new_power  # 다음 거듭제곱하기
        if not updated:  # 더 이상 새로운 경로 없음
            break

    # 자기 자신도 도달 가능하도록 표시
    for i in range(N):
        reach[i] |= 1 << i

    # transpose 계산: 각 학생이 '자신보다 작은 학생들'을 비트마스크로 저장
    # (reach[i]는 i보다 큰 애들을 저장하고 있으므로, 열 단위로 모아야 역방향 정보가 생김)
    col_bits = [0] * N
    for i in range(N):
        mask = reach[i]
        while mask:
            lsb = mask & -mask
            j = (lsb.bit_length() - 1)
            col_bits[j] |= 1 << i  # j는 i보다 크므로, col_bits[j]에 i 추가
            mask ^= lsb

    # col_bits[j] : j보다 작은 학생들의 집합
    # reach[j]    : j보다 큰 학생들의 집합

    # 판정: 어떤 학생 i가 다른 모든 학생과 크기 비교가 가능하다면
    ans = 0
    full_mask = (1 << N) - 1  # 자기자신 포함시켰음
    for i in range(N):
        merged = reach[i] | col_bits[i]  # 행 인접(작은, 큰)과 열 인접(큰, 작은) 모두 고려
        if merged == full_mask:
            ans += 1

    outputs.append(f"#{tc} {ans}")

print("\n".join(outputs), end='')
