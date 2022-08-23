def hahaha(x):
    global part_sum, min_sum
    if part_sum > min_sum:
        return
    if x == N:
        if part_sum < min_sum:
            min_sum = part_sum
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            part_sum += arr[x][i]
            hahaha(x+1)
            visited[i] = False
            part_sum -= arr[x][i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    min_sum = 1000
    visited = [False]*N
    part_sum = 0
    hahaha(0)
    print(f"#{tc} {min_sum}")