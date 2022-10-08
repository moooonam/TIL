def nCr(n,r,s):
    if r ==0:
        half.append(comb[:])
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)


T = int(input())
for tc in range(1, T+1):
    N= int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A =[i for i in range(N)] # 그냥 0부터 N-1까지 저장 
    comb = [0]*(N//2)
    half=[]
    nCr(N,N//2,0)
    half_A=[]
    half_B=[]
    cha_list=[]
    for i in range(len(half)//2):
        half_A.append(half[i])
        half_B.append(half[(len(half)-i-1)])
    for k in range(len(half)//2):
        sum_A=0
        sum_B=0
        for i in range(N//2):
            for j in range(N//2):
                sum_A+=arr[half_A[k][i]][half_A[k][j]]
                sum_B+=arr[half_B[k][i]][half_B[k][j]]
        cha_list.append(abs(sum_A-sum_B))
    print(half_A)
    print(half_B)
    print(f'#{tc} {min(cha_list)}')

