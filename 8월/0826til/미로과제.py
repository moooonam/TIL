# bfs 미로문제 (swea) (2차원 탐색)
def bfs(i, j , N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:# 3번(도착점)인가???
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            if maze[ni][nj]!=1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
    return 0 #반복문 안에서 못찾고 끝나고 나오면 못찾음


for tc in range(1, 11):
    t = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    print(f"#{tc} {bfs(sti,stj,N)}")