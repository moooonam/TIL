# 재귀를 안쓴 선택정렬
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 재귀 써서 선택정렬
def selection_sort2(arr, i):
    if i >= len(arr):
        return
    min_idx = i #최소 원소의 위치
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    #i 다음 위치로 가서 그 위치에 맞는 최소값을 찾아 바꾸는 일을 한다.
    selection_sort2(arr,i+1)
    
        

        
    

arr = [9,5,7,6,8,1,4,3,2,0,10]