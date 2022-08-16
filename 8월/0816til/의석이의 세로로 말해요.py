# 아이디어 생각이 안나서 구글링+ 코드보기 함
T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    ans=""
    maxlen=0
    for i in arr:
        if len(i)>maxlen:
            maxlen=len(i)
    for p in range(maxlen):
        for q in arr:
            if p < len(q):
                ans+=q[p]
    print(f'#{tc} {ans}')



