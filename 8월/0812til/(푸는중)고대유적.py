T = int(input())
for tc in range(1, T+1):
    N, M= map(int, (input().split()))
    arr = [list(map(int, input())) for _ in range(M)]

    for i in range(N):
        count=0
        for j in range(M-1):
            if my[i][j]==1:
                while my[i][j+1]==1:
                    count+=1
                    j
                    if i == len(my)-1:
                        break
            if my_max< count:
                my_max= count
        print(f'#{tc} {my_max}')
