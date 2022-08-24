# 미리 풀었음
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    a = M%N
    ans = arr[a]
    print(f"#{tc} {ans}")