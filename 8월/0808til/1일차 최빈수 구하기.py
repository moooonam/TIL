T = int(input())
maxindex=0
for i in range(1,T+1):
    c = [0]*(101)
    case_number=int(input())
    case=list(map(int,input().split()))
    for j in range (0, len(case)):
        c[case[j]]+=1
    # print(c)
    # max1=max(c)  #max 쓰고 풀기
    # for k in range(0,101):
    #     if c[k]==max1:
    #         maxindex=k
    #     else:
    #         continue
    # print(f'#{i} {maxindex}')

             #max 없이 풀기
    for k in range(0,101):
        if c[maxindex]<=c[k]:
            maxindex=k
    print(f'#{i} {maxindex}')