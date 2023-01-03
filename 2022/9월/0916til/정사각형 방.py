dx=[-1,1,0,0,]
dy=[0,0,-1,1,]

        
T= int(input())
for tc in range(1, T+1):
    N= int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_position=0
    max_jump=0
    for i in range(N):
        for j in range(N):
            cnt=1
            me =True
            a,b=i,j
            while me:
                for k in range(4):
                    p=a+dx[k]
                    q=b+dy[k]
                    if 0<=p<N and 0<=q <N:
                        if arr[p][q]==arr[a][b]+1:
                            cnt+=1
                            a,b = p,q
                            break
                else:
                    if cnt>max_jump:
                        max_jump=cnt
                        max_position=arr[i][j]
                    elif cnt==max_jump and max_position>arr[i][j]:
                        max_position=arr[i][j]
                    me=False
    print(f'#{tc} {max_position} {max_jump}')
          