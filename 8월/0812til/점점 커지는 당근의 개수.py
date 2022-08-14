T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 1
    my_max = 1
    my_list = list(map(int, input().split()))
    for i in range(len(my_list)):
        # if my_list[i]==1 and i!=len(my_list)-1:
        ans = 1
        if i <= len(my_list)-3:
            while my_list[i]+1==my_list[i+1]:
                i+=1
                ans += 1
                if i == len(my_list)-1:
                    break
        if my_max <ans:
            my_max= ans
    print(f'#{tc} {my_max}')
        