T = int(input())
for tc in range(1,T+1):
    N= int(input())
    vinlist = [[0]*10 for _ in range(10)] #빈칸 만들기
    count=0
    for p in range(N):
        my_list=list(map(int, input().split()))
        if my_list[4]==1:
            for i in range(my_list[0],my_list[2]+1):
                for j in range(my_list[1],my_list[3]+1):
                    vinlist[i][j]+=1
        elif my_list[4]==2:
            for i in range(my_list[0],my_list[2]+1):
                for j in range(my_list[1],my_list[3]+1):
                    vinlist[i][j]+=2
    for x in range(10):
        for y in range(10):
            if vinlist[x][y]==3:
                count+=1
    print(f'#{tc} {count}')