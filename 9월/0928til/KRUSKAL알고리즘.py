def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())
edge=[]
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([w,v,u]) # sort쓰려고 w를 제일 앞에
edge.sort()
rep = [i for i in range(V+1)] # i의 대표는 i

# MST의 간선 개수 = 정점수-1
N = V+1 # N은 정점 개수

cnt = 0 # 지금까지 선택한 간선 개수

# 가중치의 합
total = 0

# edge를 모두 확인 하면서 하나씩 선택하고
# 만약 사이클이 생기면 다음거 확인해서 사이클이 안생기는것만 추가
for w, v, u in edge:
    if find_set(v) != find_set(u):
        cnt+=1
        union(u, v)
        total += w
        if cnt == N-1:
            break
print(total) 
