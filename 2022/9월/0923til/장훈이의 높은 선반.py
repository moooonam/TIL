def nCr(n,r,s):
    if r ==0:
        sum_list.append(sum(comb))
    else:
        for i in range(s, n-r+1):
            comb[r-1] = jumone[i]
            nCr(n, r-1, i+1)

T = int(input())
for tc in range(1, T+1):
    n,b = map(int,input().split())
    jumone=list(map(int, input().split()))
    ans=sum(jumone)
    n = len(jumone)
    for k in range(1,n+1):
        sum_list=[]
        comb = [0]*k
        nCr(n,k,0)
        for p in range(len(sum_list)):
            cha=sum_list[p]-b
            if cha>=0 and cha<=ans:
                ans=cha
    print(f'#{tc} {ans}')
    