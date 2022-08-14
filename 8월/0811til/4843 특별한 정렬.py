T = int(input())
for tc in range(1,T+1):
    n=int(input())
    my_list= list(map(int, input().split()))
    s =len(my_list)
    vin_list=[0]*10
    indnum=0
    for j in range(5):
        my_max=0
        my_min=100
        for i in my_list:
            if i > my_max:
                my_max=i
            if i < my_min:
                my_min=i  
        vin_list[indnum]=my_max
        vin_list[indnum+1]=my_min 
        indnum+=2    
        my_list.remove(my_max)
        my_list.remove(my_min)
    print(f'#{tc} ',end='')
    for x in vin_list:
        print(x, end=' ')
    print()