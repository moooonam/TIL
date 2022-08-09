T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    new_list=[0]*(N-M+1)
    for j in range(N-M+1):
        smallsum=0
        for k in range(j,j+M):
            smallsum+=num_list[k] #부분합을 갯수에 맞춰서 구해준다
        new_list[j]=smallsum # 여기까지가 부분합 다 구한거
    maxnum=0
    minnum=new_list[0] # 최소값은 뉴리스트의 첫번째 값부터 시작하도록
    for l in range(len(new_list)): # 부분합중 최대 최소를 구한다
        if new_list[l]>maxnum:
            maxnum = new_list[l]
        if new_list[l]<minnum:
            minnum = new_list[l]
    print(f'#{i} {maxnum-minnum}')


