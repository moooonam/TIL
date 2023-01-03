T = int(input())
for tc in range(1, T+1):
    N = int(input())
    submit_list=[]
    max_dok=0
    for i in range(N):
        submit_list.append(list(map(int,input().split())))
    for i in range(N):
        submit_list[i][1], submit_list[i][0] = submit_list[i][0], submit_list[i][1]
    submit_list.sort()
    for i in range(len(submit_list)):
        cnt=1
        time=[0]*25
        for k in range(submit_list[i][1], submit_list[i][0]):#첫번째꺼 칠하기
            time[k]=1
        for j in range(i+1, len(submit_list)):
            for p in range(submit_list[j][1],submit_list[j][0]):
                if time[p] ==1:
                    break
            else:
                for p in range(submit_list[j][1],submit_list[j][0]):
                    time[p]=1
                cnt+=1
        # print(time)
        if cnt>=max_dok:
            max_dok=cnt
            
    # print(submit_list)
    print(f'#{tc} {max_dok}')