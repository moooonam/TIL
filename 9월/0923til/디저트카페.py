# 다른분꺼 참고함

dx=[1,1,-1,-1]#i
dy=[1,-1,-1,1]#j
def disert(i,j,visit,turn,start):
    if turn == 3 and (i,j)==start:
        disert_list.append(len(visit)-1)
        return
    for m in range(turn,turn+2):
        if m <=3:
            nx=i+dx[m]
            ny=j+dy[m]
        
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] not in visit[1:]:
                if m==turn:     
                    disert(nx,ny,visit+[arr[nx][ny]],turn,start)
                else:
                    disert(nx,ny,visit+[arr[nx][ny]],turn+1,start)
                
            
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    disert_list=[]
    ans = -1
    for i in range(N):
        for j in range(N):
            disert(i,j,[arr[i][j]],0,(i,j))
    if disert_list:
        ans = max(disert_list)
    print(f'#{tc} {ans}')

