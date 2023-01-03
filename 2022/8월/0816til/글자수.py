T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    my_max=0
    for i in str1:
        result=0
        for j in str2:
            if i==j:
                result+=1
        if my_max<result:
            my_max=result
    print(f'#{tc} {my_max}')