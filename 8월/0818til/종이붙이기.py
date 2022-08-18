T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = [1, 1, 5, 11, 21]
    for i in range(5, 30):
        ans.append(ans[i-1] + ans[i-2]*2)
    a = int(N//10)
    print(f"#{tc} {ans[a-1]}")












