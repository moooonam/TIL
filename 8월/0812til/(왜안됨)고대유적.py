T = int(input())
for tc in range(1, T+1):
    N, M= map(int, (input().split()))
    arr = [list(map(int, input().split())) for _ in range(M)]
    my_max=0
    for i in range(N):
        for j in range(M-1):
            count1=1    
            if arr[i][j]==1:
                while arr[i][j+1]==1:
                    count1+=1
                    if j==M-2:
                        break
                    j+=1
            if my_max< count1:
                my_max= count1
    for p in range(N-1):
        for q in range(M):
            count2=1
            if arr[p][q]==1:
                while arr[p+1][q]==1:
                    count2+=1
                    if p==N-2:
                        break
                    p+=1
            if my_max< count2:
                my_max= count2
    print(f'#{tc} {my_max}')
