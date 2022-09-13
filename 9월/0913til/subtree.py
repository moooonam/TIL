T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    my_list =[N]
    me =True
    k=0
    while me:
        k = len(my_list)
        for i in range(0,E*2,2):
            if arr[i] in my_list and arr[i+1] not in my_list:  
                my_list.append(arr[i+1])
        if k == len(my_list):
            me = False
    print(f'#{tc} {k}')
            