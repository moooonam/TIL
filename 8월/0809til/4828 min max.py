T = int(input())
for i in range(T):
    N = int(input())
    num_list= list(map(int, input().split()))
    my_max=0
    my_min=1000000
    for j in range(len(num_list)):
        if num_list[j]>my_max:
            my_max = num_list[j]
        if num_list[j]<my_min:
            my_min = num_list[j]
    print(f'#{i+1} {my_max-my_min}')    

