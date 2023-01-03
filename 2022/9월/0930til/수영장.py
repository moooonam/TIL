inf=9999999999999
T = int(input())
for tc in range(1, T+1):
    day_1, month_1, month_3, year = map(int, input().split())
    swimming = list(map(int, input().split()))
    swimming.insert(0, 0)
    sum_list=[]
    swimming.append(0)
    min_list=[inf]*100
    q=[(0,0)]
    while q:
        x, s = q.pop(0)
        if s>min_list[x]:
            continue
        min_list[x]=s
        if x>12:
            sum_list.append(s)
            continue
        if swimming[x] ==0:
            q.append((x+1,s))
        else:
            q.append((x+1,s+swimming[x]*day_1))
            q.append((x+1,s+month_1))
            q.append((x+3,s+month_3))

    print(f'#{tc} {min(min(sum_list),year)}')
    
            