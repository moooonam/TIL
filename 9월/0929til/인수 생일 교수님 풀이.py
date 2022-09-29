INF=1000000000

def di(s): # s는 시작지점
    q = [s]
    D[s][s] = 0
    head = -1
    tail = 0

    while head != tail:
        head += 1
        now = q[head]
        # 인접 리스트에서 now에서 갈 수 있는 정점 가져와서 계산
        for e, cost in adl[now]:
            # 이 전에 해논거 보다 덜 걸리면 추가
            if D[s][e]> D[s][now] + cost:
                D[s][e] = D[s][now] + cost
                q.append(e)
                tail+=1
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # N번까지 M개 도로
    adl = [[] for _ in range(N+1)] # 인접 리스트 ex) adl[2]= 2번 집에서 출발해서 갈 수 있는 정점, 가중치의 리스트
    for i in range(M):
        s, e, w = map(int, input().split())
        adl[s].append((e,w)) # 출발:s 도착:e 그때 가중치 :w
    # D[i]: i번 집에서 출발해서 나미지 각 집까지 가는데 걸리는 최소 비용 리스트
    # D[i][j]: i에서 출발해 j 까지 가는데 걸리는 최소 비용
    D = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        di(i)
    maxv=0
    for i in range(1, N+1):
        if X==i:
            continue
        distance = D[X][i] + D[i][X]
        maxv= max(maxv, distance)
    print(f"#{tc} {maxv}")    
