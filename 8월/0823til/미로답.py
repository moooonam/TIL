def dfs(i, j, N):

    stack = []
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    while True:
        if arr[i][j] == 3:
            return 1

        arr[i][j] = 1 # 지나온곳은 벽으로 만들거임

        for d in range(4):
            ni = di[d] +i
            nj = dj[d] +j

            if 0<= ni <N and 0<= nj <N and arr[ni][nj] != 1:

                stack.append((i, j))
                i, j = ni, nj
                break
        else:
            # 갈수있는 칸이 없으면?
            if stack:
                i, j = stack.pop()
            else:
                break
    #반복문에서 중간에 return 문을 만나서 종료하지 못하고 여기까지 와버린경우 길이 없다는 뜻
        return 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)] # 미로
    si = sj = 0 # 시작 행, 열 =0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                si = i
                sj = j
    print(f"#{tc} {dfs(si, sj, n)}")