def bus(arr, n):
    global cnt
    jump=1
    max_index=0
    for i in range(n-2,-1,-1):
        if arr[i]>= jump:
            max_index=i
        jump+=1
    if max_index==0:
        return cnt
    cnt+=1
    bus(arr, max_index+1)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    arr.append(0)
    N = arr.pop(0)
    cnt=0
    bus(arr, N)
    print(f'#{tc} {cnt}')
        