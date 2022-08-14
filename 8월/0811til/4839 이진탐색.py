T = int(input())
for tc in range(1,T+1):
    p, pa, pb=map(int,input().split())
    ac, bc = 1,1 #카운트
    l=1 
    r=p
    c=int((l+r)/2)
    while c!=pa:
        if c <pa:
            l=c
        elif c>pa:
            r=c
        c=int((l+r)/2)
        ac += 1
    l=1 
    r=p
    c=int((l+r)/2)
    while c!=pb:
        if c <pb:
            l=c
        elif c>pb:
            r=c
        c=int((l+r)/2)
        bc += 1
    if ac<bc:
        print(f'#{tc} A')
    elif ac>bc:    
        print(f'#{tc} B')
    else:    
        print(f'#{tc} 0')
        
            


         