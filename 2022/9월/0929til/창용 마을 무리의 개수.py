def find(x):
    while x !=p[x]:
        x= p[x]
    return x

def union(x,y):
    p[find(y)]=find(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    for _ in range(M):
        a, b = map(int,input().split())
        union(a,b)
    cnt = [0]*(N+1)
    ans=0
    for i in range(1, N+1):
        cnt[find(i)]+=1
    for k in range(1, N+1):
        if cnt[k] != 0:
            ans+=1
    print(f'#{tc} {ans}')