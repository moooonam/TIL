# 힌트 받아서 품
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    max_num1 = 0
    max_num2 = 0
    ans =0
    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, 1, -1]
    di2 = [-1, 1, 1, -1]   # 1시 5시 7시 11시
    dj2 = [1, 1, -1, -1]
    for i in range(N):
        for j in range(N):
            vsum1 = arr[i][j]
            for d in range(4):
                for m in range(1, M):
                    if 0 <= i+m *di[d] < N and 0 <= j+m*dj[d] < N:
                        vsum1+= arr[i+m *di[d]][j+m*dj[d]]
            if vsum1 > max_num1:
                max_num1 = vsum1
    for i in range(N):
        for j in range(N):
            vsum2 = arr[i][j]
            for d in range(4):
                for m in range(1, M):
                    if 0 <=i+m *di2[d] < N and 0<=j+m*dj2[d] < N:
                        vsum2 += arr[i+m *di2[d]][j+m*dj2[d]]
            if vsum2>max_num2:
                max_num2 = vsum2
    if max_num1>max_num2:
        ans = max_num1
    else:
        ans = max_num2
    print(f"#{tc} {ans}")

