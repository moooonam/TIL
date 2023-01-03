arr =[-1,3,-9,6,7,-6,1,5,4,-2]
n = len(arr)
check=[]
cnt=0
for i in range(1<<n):
    for j in range(n):
        if i&(1<<j):
           check.append(arr[j])
    if sum(check)==0:
        print(*check)# *언펙 기능함 
        check=[]
        cnt+=1
    else:
        check=[]
print(cnt)