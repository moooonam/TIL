# 시간초과
def nPr(i, k):
    if i ==k: #인덱스 i == 원소의 개수
        if p not in cal:
            cal.append(p[:])
    
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            nPr(i+1, k)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus, minus, gob, nanugi = map(int, input().split()) ## 1,2,3,4
    num_list=list(map(int, input().split()))
    p = [1 for _ in range(plus)]
    for i in range(minus):
        p.append(2)
    for i in range(gob):
        p.append(3)
    for i in range(nanugi):
        p.append(4)
    cal=[]#연산 순서 순열
    nPr(0,len(p))
    sum_list=[] #연산 결과 담을 리스트
    
    for i in range(len(cal)):
        cal_sum=num_list[0]
        x=1
        for j in range(N-1):
            if cal[i][j]==1:
                cal_sum+=num_list[x]
                x+=1
            elif cal[i][j]==2:
                cal_sum-=num_list[x]
                x+=1
            elif cal[i][j]==3:
                cal_sum*=num_list[x]
                x+=1
            elif cal[i][j]==4:
                cal_sum= int(cal_sum/num_list[x])
                x+=1
        sum_list.append(cal_sum)
    # print(sum_list)
    ans = max(sum_list)-min(sum_list)
    print(f'#{tc} {ans}')        
                

        
