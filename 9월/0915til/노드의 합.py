#이건 내힘으로함 굳
def nodesum(n):
    if n<=N:
        nodesum(n*2)
        nodesum(n*2+1)
        my_tree[n//2]= my_tree[(n//2)*2]+my_tree[(n//2)*2+1]


T = int(input())
for tc in range(1, T+1):
    N,M,L = map(int, input().split())
    my_tree = [0]*(N+2)
    for i in range(M):
        a,b = map(int, input().split())
        my_tree[a]=b
    nodesum(1)
    print(f'#{tc} {my_tree[L]}')