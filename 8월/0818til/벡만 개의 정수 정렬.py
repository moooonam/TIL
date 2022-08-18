def counting_sort(array, max):
 
    #counting array 생성
    counting_array = [0]*(max+1)
 
    #counting array에 input array내 원소의 빈도수 담기
    for i in array:
        counting_array[i] += 1
 
    #counting array 업데이트.
    for i in range(max):
        counting_array[i+1] += counting_array[i]
 
    #output array 생성
    output_array = [-1]*len(array)
 
    #output array에 정렬하기(counting array를 참조)
    for i in array:
        output_array[counting_array[i] -1] = i
        counting_array[i] -= 1
    return output_array
arr = list(map(int ,input().split()))
counting_array(arr, 1000000)
print(arr[500000])



# 계속 시간초과 뜸..ㅎㅎ
# 포기 ㅎㅎ