T = int(input())
for tc in range(1,T+1):
    n,k =map(int,input().split())
    expend_list=[[0]*(n+2)for _ in range(n+2)]
    arr = [list(map(int,input().split()))for _ in range(n)]
    count=0
    anslist=[0]
    for w in range(k):
        anslist.append(1)
    anslist.append(0)
  
    for i in range(1,n+1):
        for j in range(1,n+1):
            expend_list[i][j]=arr[i-1][j-1] #테두리 추가
 
    for x in range(1,n+1): # 가로 만족하는거 갯수 세기
        for y in range(1,n-k+2):
            if expend_list[x][y-1:y+k+1]==anslist:
                count+=1
    
    for x1 in range(1,n-k+2): # 세로 만족하는거 갯수 세기
        for y1 in range(1,n+1):
            serolist=[]
            for b in range(k+2):
                serolist.append(expend_list[x1-1+b][y1])
            if serolist==anslist:
                count+=1
    print(f'#{tc} {count}')
    