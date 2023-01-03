def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V는 마지막 노드 번호 E는 간선수
    edge=[]
    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append([w,v,u]) # sort쓰려고 w를 제일 앞에
    edge.sort()
    rep = [i for i in range(V+1)]
    N = V+1 # N은 정점 개수
    cnt = 0
    total =0
    for w, v , u in edge:
        if find_set(v) != find_set(u):
            cnt+=1
            union(u, v)
            total += w
            if cnt == N-1:
                break
    print(f'#{tc} {total}')