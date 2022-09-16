list_3=[]
for i in range(1, 1000001):
    list_3.append(i**3) 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans =-1
    for j in range(len(list_3)):
        if list_3[j]==N:
            ans= j+1
            break
    print(f'#{tc} {ans}')









    # ans =-1
    # if N== 1:
    #     ans=1 
    # else:
    #     for i in range(N,N//3+1):
    #         if i**3==N:
    #             ans = i
    #             break
    # print(f'#{tc} {ans}')