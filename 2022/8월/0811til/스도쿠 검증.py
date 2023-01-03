T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split()))for _ in range(9)]
    result=0
    for i in range(9):
        ysum=0
        xsum=0
        for j in range(9):
            xsum+=arr[i][j]
            ysum+=arr[j][i]
        if ysum==45:
            result+=1
        if xsum==45:
            result+=1
  
    for x in range(3):
        x=x*3
        for y in range(3):
            y=y*3
            nemosum=0
            for x1 in range(3):
                for y1 in range(3):
                    nemosum+=arr[x+x1][y+y1]
            if nemosum==45:
                result+=1
    if result==27:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')                





                
    
    
        
        
        