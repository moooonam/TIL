T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split())for _ in range(N)]
    vin = [list([""]*3)for _ in range(N)]
    for i in range(N):
        for j in range(N-1,-1,-1):
            vin[i][0] += arr[j][i]

    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            vin[N-1-i][1] += arr[i][j]

    for j in range(N-1,-1,-1):
        for i in range(N):
            vin[N-1-j][2] += arr[i][j]
    
    print(f"#{tc}")
    for i in range(N):
        print(" ".join(vin[i]))
    