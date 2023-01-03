T = int(input()) #교수님 힌트 보고 풀었음
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    result = ""
    for i in range(N): # 가로는 완성
        for j in range(N-M+1):
            word = arr[i][j:j+M]
            revers_word = ""
            for k in range(M-1,-1,-1):
                revers_word += word[k]
            if word == revers_word:
                result = word
                break
        if result!="":
            break
    for j in range(N):
        for i in range(N-M+1):
            word2=""
            revers_word2=""
            for p in range(i,i+M):
                word2+=arr[p][j]
            for q in range(M-1,-1,-1):
                revers_word2+=word2[q]
            if word2 == revers_word2:
                result = word2
                break
        if result!="":
            break
    print(f'#{tc} {result}')























    #         if arr[i][j]==arr[i][M-1-j]:
    #             while arr[i][j]==arr[i][M-1-j]:
    #                 count+=1
    #                 if j==(M-1)//2:
    #                     break
    #                 j+=1
    #     if count==(M+1)//2:
    #         j-=(M-1)//2
    #         result=arr[i][j:j+M]
    #         break
    # print(result) # 안돼................





