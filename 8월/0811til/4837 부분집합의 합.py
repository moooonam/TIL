T=int(input())
arr = list[1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(1,T+1):
    n, k = map(int, input().split())
    ans = 0 
    for i in range(1<<12): #시작 지점을 1로 바꿔 공집합을 제외함
        sum=0
        count=0
        for j in range(12):
            if i & (1<<j):
                sum += arr[j]
                count += 1
        if count==n and sum==k:
            ans+=1

                

    print(f'#{tc} {ans}')
