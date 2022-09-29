def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    N ,M = map(int, input().split())
    rep = [i for i in range(N+1)]
    count=[0]*(N+1)
    cnt=0
    jo_list = list(map(int, input().split()))
    for i in range(M):
        a,b = jo_list[i*2], jo_list[i*2+1]
        union(a, b)
    print(rep)            
    for i in range(1,N+1):
        count[find_set(i)]+=1
    print(count)
    for k in range(1,N+1):
        if count[k] !=0:
            cnt+=1
    # print(rep)
    print(f'#{tc} {cnt}')
    

