def divide_two(start, end):
    if start == end:
        return start  # 한명 남았다는 의미이므로 가위바위보를 위해 리턴
    else:
        a = divide_two(start, (start + end) // 2)
        b = divide_two((start + end) // 2 + 1, end)
        return winner(a, b)

def winner(x,y):
    if arr[x] == arr[y]:
        return x
    elif arr[x] - arr[y] == 1 or arr[x] - arr[y] == -2:
        return x
    return y 

#구글의 힘을 빌림...
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f"#{tc} {divide_two(0, N-1)+1}")

