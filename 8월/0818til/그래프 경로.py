T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node_list = [list([0]*(V+1)) for _ in range(V+1)]
    for i in range(E):
        r, c = map(int, input().split())
        node_list[r][c] = 1
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    stack = []
    now = S
    visited[now] = 1
    ans=0
    me = True
    while me:
        for w in range(1, V+1):
            if node_list[now][w] == 1 and visited[w] == 0:
                stack.append(now)
                visited[w]=1
                now = w
                if now == G:
                    ans = 1
                    me = False
                break
        else:
            if stack:
                now = stack.pop()
            else:
                ans = 0
                break 
    print(f"#{tc} {ans}")
