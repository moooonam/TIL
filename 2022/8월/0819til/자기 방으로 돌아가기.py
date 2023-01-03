T = int(input())
for tc in range(1, T+1):
    N = int(input())
    go_list= []
    for i in range(N):
        go_list.append(list(map(int, input().split())))
    vin=[0]*201
    for i in go_list:
        a = i[0]
        b = i[1]
        if a< b:
            for j in range((a+1)//2, (b+1)//2 +1):
                vin[j] += 1
        else:
            for j in range((b+1)//2, (a+1)//2+1):
                vin[j] += 1
    ans=0
    for i in range(len(vin)):
        if ans< vin[i]:
            ans = vin[i]
  
    print(f"#{tc} {ans}")