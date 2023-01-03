def find_set(x):
    while x!=p[x]:
        x = p[x]
    return x
def union(x,y):
    x= find_set(x)
    y= find_set(y)
    if x == y :
        return
    # x,y중에 누구를 대표로 할것인가?
    # 깊이가 큰 (rank) 가 더 큰 사람을 대표로 할것이다.
    # 깊이가 깊은 집합을 x라고 하도록
    if rank[y]> rank[x]:
        x,y = y,x
    p[y] = x 
    if rank[x] == rank[y]:
        rank[x] += 1
T = int(input())
for tc in range(1, T+1):
    N ,M = map(int, input().split())
    pair =list(map(int, input().split()))
    p = [i for i in range(N+1)]
    rank = [0]*(N+1)

    for i in range(M):
        x= pair[i*2]
        y= pair[i*2 +1]
        union(x,y)
    reps= set()
   
