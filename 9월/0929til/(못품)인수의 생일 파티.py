
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # N번까지 M개 도로
    arr = [[1000000000]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        arr[i][i]=0
    for _ in range(M):
        x,y,w = map(int, input().split())
        arr[x][y] =w
    print(arr)
    
#