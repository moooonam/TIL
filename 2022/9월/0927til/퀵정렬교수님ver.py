def quicksort(A, l, r):
    if l <r :
        s = partition(A, l, r)
        quicksort(A, l, s-1)
        quicksort(A, r, s-1)

def partition(A, l, r):
    p =A[l]
    while i <= j :
        while i<=j and A[i]<=p:
            i+=1
        while i<=j and A[j]>=p:
            j-=1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j
T= int(input())
for tc in range(1, T+1):
    N =int(input())
    arr = list(map(int, input().split()))