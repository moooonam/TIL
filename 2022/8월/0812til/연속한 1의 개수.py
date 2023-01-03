T = int(input())
for tc in range(1, T+1):
    N = int(input())
    my = input()
    my_max=0
    for i in range(N-1):
        count=1
        if my[i]=='1':
            while my[i+1]=='1':
                count+=1
                i+=1
                if i == len(my)-1:
                    break
        if my_max< count:
            my_max= count
    print(f'#{tc} {my_max}')
