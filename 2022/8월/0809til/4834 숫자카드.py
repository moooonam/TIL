T = int(input())
for i in range(1,T+1):
    n = int(input())
    a = list(map(int,input()))
    vinlist=[0]*10
    maxvindo=0
    for j in a:
        vinlist[j]+=1
    for k in range(len(vinlist)):
        if vinlist[k]>= maxvindo:
            maxvindo=vinlist[k]
            maxvindonum=k
    print(f'#{i} {maxvindonum} {maxvindo}')