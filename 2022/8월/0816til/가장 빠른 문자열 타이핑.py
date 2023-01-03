# 풀이 1 


# T = int(input())
# for tc in range(1, T+1):
#     A, B = input().split()
#     A = list(A)
#     B = list(B)
#     n=len(B)
#     cnt=0

#     for i in range(len(A) - len(B) + 1):
#         if A[i:i+n] == B:
#             A[i]=1
#             for k in range(1,n):
#                 A[i+k]=0
#         elif A[i]!=0:
#             A[i]=1

#         elif i==len(A)-len(B): # 뒤 처리
#             for p in range(len(A)-len(B),len(A)):
#                 if A[p]!=0:
#                     A[p]=1 
#     for j in A:
#         if j==1:
#             cnt+=1

#     print(f'#{tc} {cnt}')
# 풀이2
# 풀이 1은 뒤처리가 잘못 돼있었음 
T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    A = list(A)
    B = list(B)
    n=len(B)
    cnt=0

    for i in range(len(A) - len(B) + 1):
        if A[i:i+n] == B:
            A[i]=1
            for k in range(1,n):
                A[i+k]=0
        elif i==len(A)-len(B): # 뒤 처리
            for p in range(len(A)-len(B),len(A)):
                if A[p]!=0:
                    A[p]=1 
        elif A[i]!=0:
            A[i]=1
    for j in A:
        if j==1:
            cnt+=1

    print(f'#{tc} {cnt}')