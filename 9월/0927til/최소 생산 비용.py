
def make_some(x,now_sum):
    global min_sum

    if x==N:
        if now_sum<min_sum:
            min_sum=now_sum
        return
    if now_sum>min_sum:
        return

    for j in range(N):
        if visited[j]==0:
            visited[j]=1

            make_some(x+1,now_sum+arr[x][j])
            visited[j]=0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    visited=[0]*N
    min_sum=100*N
    make_some(0, 0)
    print(f'#{tc} {min_sum}')