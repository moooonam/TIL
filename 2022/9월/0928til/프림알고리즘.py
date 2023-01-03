
def prim(r, V):
    MST = [0]*(V+1) # MST포함여부
    key = [10000] *(V+1) # 가중치를 최대값으로 초기화
    # key[v] => v가 MST에 속한 정점과 연결될 때의 최소 가중치
    key[r] = 0 # 시작점의 key
    
    for i in range(V): #정점중에 선택
        #MST에 포함되지 않은 정점 중에 key 가 최소인 것 찾기
        # MST[i]==0 ==> MST에 포함되지 않은 정점
        u = 0
        minV = 10000
        for j in range(V+1):
            if MST[j] == 0 and key[j] <minV:
                u = j
                minV = key[i]
        MST[u] = 1 # 정점 u를 MST에 추가
        # u에 인접한 정점들 v에 대해서 MST에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] >0:
                key[v] = min(key[v], adjM[u][v])
                # 를 통해서 MST에 포함되는 비용과 기존 비용을 비교해서 최고값을 사용
    
    return sum(key) # 가중치의 합

V , E = map(int, input().split()) # E는 간선수
adjM = [[0]*(V+1) for _ in range(V+1)] # 인접행렬
adjL = [[] for _ in range(V+1)] # 인접리스트

for _ in range(E):
    u, v, w = map(int, input().split()) # u에서 v로 w 가중치
    adjM[u][v] = w
    adjM[v][u] = w #가중치가 있는 무방향 그래프,
    adjL[u].append((v,w))
    adjL[v].append((u,w))

print(adjM)
print(adjL)
print(prim(0,V))