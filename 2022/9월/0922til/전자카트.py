def nPr(i, k):
    if i ==k: #인덱스 i == 원소의 개수
        a= p[:]
        road.append(a)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            nPr(i+1, k)
            p[i], p[j] = p[j], p[i]



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    p=[]
    for i in range(2,N+1):
        p.append(i)
    road =[]
    nPr(0, N-1)
    sum_list=[]
    for i in range(len(road)):
        road[i].append(1)
        road[i].insert(0,1)
    
    for i in range(len(road)):
        some_sum=0
        for j in range(len(road[i])-1):
            some_sum+=arr[road[i][j]-1][road[i][j+1]-1]
        sum_list.append(some_sum)
    print(f'#{tc} {min(sum_list)}')

    # i 가 출발 j 가 도착


