T = int(input())
for tc in range(1, T+1):
    N=int(input())
    arr = list(map(int, input().split()))
    for i in range(N-1,0,-1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    arr = ' '.join(str(k) for k in arr)


    print(f'#{tc} {arr}')
    
