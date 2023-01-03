T = int(input())
for tc in range(1, T+1):
    N = int(input())
    busstop = [0]*1001
    for i in range(N):
        bus, st, en = map(int, input().split())
        if bus == 1:
            for j in range(st, en+1):
                busstop[j] +=1
        elif bus == 2:
            if st%2 == 0: # 짝수면
                for j in range(st, en+1, 2):
                    busstop[j] += 1
            else: #홀수면
                for j in range(st, en+1, 2):
                    busstop[j] += 1
        elif bus == 3:
            if st%2 == 0: # 짝수면
                for j in range(st, en+1):
                    if j%4 == 0:
                        busstop[j] += 1
            else: #홀수면
                for j in range(st, en+1):
                    if j%3 == 0 and j%10 !=0:
                        busstop[j] +=1
    ans = max(busstop)
    print(f"#{tc} {ans}")