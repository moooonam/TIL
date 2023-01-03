T= int(input())
for i in range(1,T+1):
    N, K = map(int, input().split())
    list1=list(map(int, input().split())) # 과제 제출한사람 번호
    list2=[0]*N # 모든 번호
    list3=[0]*(N-K) #안할사람 들어갈거
    for j in range(0,N):
        list2[j]=j+1
    s=0
    for l in range(0,N):
        if list2[l] not in list1:
            list3[s]=list2[l]
            s+=1
    print(f'#{i}', end=' ')
    for o in range(N-K):
        if o<N-K-1:
            print(f'{list3[o]}', end=' ')
        else:
            print(f'{list3[o]}')
