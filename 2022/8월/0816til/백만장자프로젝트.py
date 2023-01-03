T = int(input())
for tc in range(1, T+1):
    N=int(input())
    arr= list(map(int, input().split()))
    my_max=0
    ans=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>my_max:
            my_max=arr[i]
        else:
            ans+=my_max-arr[i]
    print(f'#{tc} {ans}')
