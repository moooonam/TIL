dx=[1,0,-1,0]
dy=[0,1,0,-1]

def gogo():
    q=[(0,0)]
    while q:
        x,y= q.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < N and 0<= ny < N:
                if arr[x][y] >= arr[nx][ny] and biyong[nx][ny] >biyong[x][y] +1:
                    biyong[nx][ny] = biyong[x][y]+1
                    q.append((nx,ny))
                elif arr[x][y] < arr[nx][ny] and biyong[nx][ny] > biyong[x][y]+1 +(arr[nx][ny]-arr[x][y]):
                    biyong[nx][ny] = biyong[x][y]+1 +(arr[nx][ny]-arr[x][y])
                    q.append((nx,ny))
                # print(biyong)
    return biyong[N-1][N-1]
   
    
T = int(input())
for tc in range(1, T+1):
    N= int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    biyong = [[100000000]*(N) for _ in range(N)]
    biyong[0][0]=0
    print(f'#{tc} {gogo()}')
   
