# 구글링함

def tree(n):
    global num
    if n <= N:
        tree(n*2)
        my_tree[n] =num
        num+=1
        tree(n*2+1)
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    my_tree = [0]*(N+1)
    num=1
    tree(1)
    
    print(f'#{tc} {my_tree[1]} {my_tree[N//2]}')
        


        

            
