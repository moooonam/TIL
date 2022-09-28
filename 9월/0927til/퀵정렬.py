def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr)//2]
    l_arr, c_arr, r_arr = [],[],[]
    
    for num in arr:
        if num < pivot:
            l_arr.append(num)
        elif num >pivot:
            r_arr.append(num)
        else:
            c_arr.append(num)
    merged_arr= quick_sort(l_arr) + c_arr + quick_sort(r_arr)
    return merged_arr
T= int(input())
for tc in range(1, T+1):
    N =int(input())
    arr = list(map(int, input().split()))
    merged_arr = quick_sort(arr)
    ans = merged_arr[N//2]
    print(f'#{tc} {ans}')