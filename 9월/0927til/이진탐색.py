# import sys
# sys.stdin = open("input.txt")

def bi(arr, n, direc):
    global cnt
    if len(arr)==1 and arr[0] !=n:
        return 
    elif len(arr)==0:
        return
    l=0
    r=len(arr)-1
    m =(l+r)//2
    
    if arr[m]<n:
        if direc=='right':
            return 
        else:
            return bi(arr[m+1:],n,'right')
    elif arr[m]>n:
        if direc=='left':
            return 
        else:
            return bi(arr[:m],n, 'left') 
    else:
        cnt+=1
        return
    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_A.sort()
    list_B = list(map(int, input().split()))
    cnt=0
    
    for i in list_B:
        # print(i)
        bi(list_A, i, '')
    print(f'#{tc} {cnt}')
    
