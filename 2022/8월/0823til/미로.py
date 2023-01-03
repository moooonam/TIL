# 구글링함..
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input()))for _ in range(N)]
    x = 0
    y = 0
    result = 0
    move = [(1,0),(-1,0),(0,1),(0,-1)] # 하 상 우 좌
    for i in range(N): #출발점 찾기
        for j in range(N):
            if arr[i][j] == 2:
                x = i
                y = j
                break
    stack = [(x,y)]
    while stack:
        x, y = stack.pop()
        arr[x][y] = 1
        for x2, y2 in move:
            dx = x + x2
            dy = y + y2
            if dx < 0 or dx >=N or dy <0 or dy>= N:
                continue
            if arr[dx][dy] == 3:
                result = 1
                break
            elif arr[dx][dy] == 0:
                stack.append((dx,dy))
        else:
            continue
        break
    print(f"#{tc} {result}")    