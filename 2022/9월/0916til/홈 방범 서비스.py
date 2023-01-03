# 구글링 했다... 너무 어렵다...

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    home =[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==1:
                home.append((i,j))
    max_profit = len(home)*M
