T= int(input())
for tc in range(1,T+1):
    N=float(input())
    nanu=0.5
    ans=[]
    cnt=0
    start=N
    my_sum=0
    while True:
        if cnt>12:
            ans='overflow'
            break
        if N//nanu==1:
            ans.append(1)
            my_sum+=nanu
            N-=nanu
            nanu=nanu/2
            cnt+=1
            
        else:
            nanu=nanu/2
            cnt+=1
            ans.append(0)
        if my_sum== start:
            break
    if cnt<=12:
        ans="".join(map(str,ans))
    print(f'#{tc} {ans}')



