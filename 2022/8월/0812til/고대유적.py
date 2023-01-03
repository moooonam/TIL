#정답 봄...ㅠㅠ
t = int(input())
for tc in range(1, t + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    answer = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt = 0
            else:
                cnt += 1
            if cnt > answer:
                answer = cnt
        cnt = 0
 
    cnt = 0
    for j in range(M):
        for i in range(N):
            if arr[i][j] == 0:
                cnt = 0
            else:
                cnt += 1
            if cnt > answer:
                answer = cnt
        cnt = 0
 
    print(f"#{tc} {answer}")
