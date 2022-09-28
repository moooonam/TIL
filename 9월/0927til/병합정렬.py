def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    merged_arr=[]

    if low_arr[-1] >high_arr[-1]:
        cnt+=1
        
    l = h = 0
    while l <len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l+=1
        else:
            merged_arr.append(high_arr[h])
            h+=1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

T = int(input())
for tc in range(1, T+1):
    N =int(input())
    arr = list(map(int, input().split()))
    cnt=0
    merged_arr = merge_sort(arr)
    ans = merged_arr[N//2]
    print(f'#{tc} {ans} {cnt}')