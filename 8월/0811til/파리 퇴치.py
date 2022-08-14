T = int(input())
for tc in range(1,T+1):
    n,m =map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sum_list=[] #귀찮으니 append쓰자..
    max_num=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sub_sum=0   
            for k1 in range(m):
                for k2 in range(m):
                    sub_sum+=arr[i+k1][j+k2]
            sum_list.append(sub_sum)

                
    max_num=max(sum_list)
    print(f'#{tc} {max_num}')        
