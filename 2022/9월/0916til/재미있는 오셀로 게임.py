dx=[-1,1,0,0,1,1,-1,-1]
dy=[0,0,-1,1,1,-1,1,-1]
def BW(a,b):
    if arr[a][b]==1:#놓은게 블랙일때
        for k in range(8):
            p=dx[k]
            q=dy[k]
            g=1
            while 1<=a+p*g <=N and 1<= b+q*g <=N:
                if arr[a+p*g][b+q*g]==0:
                    break
                if arr[a+p*g][b+q*g]==1:
                    for t in range(1,g):
                        arr[a+p*t][b+q*t]=1
                    g+=1
                    break
                else:
                    g+=1
    if arr[a][b]==2:#놓은게 화이트일때
        for k in range(8):
            p=dx[k]
            q=dy[k]
            g=1
            while 1<=a+p*g <=N and 1<= b+q*g <=N:
                if arr[a+p*g][b+q*g]==0:
                    break
                if arr[a+p*g][b+q*g]==2:
                    for t in range(1,g):
                        arr[a+p*t][b+q*t]=2
                    g+=1
                    break
                else:
                    g+=1
                    

T = int(input())
for tc in range (1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+2) for _ in range(N+2)]
    arr[N//2][N//2] =2
    arr[N//2+1][N//2] =1
    arr[N//2][N//2+1] =1
    arr[N//2+1][N//2+1] =2
    for _ in range(M):
        x,y,dol = map(int, input().split())
        arr[y][x]=dol
        BW(y,x)
    cnt_1=0
    cnt_2=0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j]==1:
                cnt_1+=1
            elif arr[i][j]==2:
                cnt_2+=1
    print(f'#{tc} {cnt_1} {cnt_2}')
    

                



