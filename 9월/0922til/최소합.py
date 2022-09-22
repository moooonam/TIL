def jump(arr,x,y,hap):
    global N
    if x==N-1 and y==N-1:
        hap+=arr[x][y]
        sum_list.append(hap)
        return
    
    if x==N-1:
        hap+=arr[x][y]
        jump(arr, x, y+1,hap)
    elif y==N-1:
        hap+=arr[x][y]
        jump(arr, x+1, y,hap)
    else:
        hap+=arr[x][y]
        jump(arr, x+1, y,hap)       
        jump(arr, x, y+1,hap)
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my_arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list=[]
    now_x=now_y=0
    jump(my_arr,0,0,0)
    print(f'#{tc} {min(sum_list)}')