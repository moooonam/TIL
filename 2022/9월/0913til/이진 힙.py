def enq(n):
    global last
    last +=1
    heap[last] = n
    # 만약 새로 추가된 원소가 부모 노드보다 더 작은 경우 자리를 바꿔야함
    c = last # 새로 추가된 노드(자식노드)
    p = c//2 # 부모노드
    # 부모가 존재하고, 부모보다 자식이 더 작으면 자리 바꾸기
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0]*1000001
    last = 0
    my_sum = 0
    my = list(map(int, input().split()))
    for i in my:
        enq(i)
    while N >=1:
        my_sum += heap[N//2]
        N = N//2
    print(f'#{tc} {my_sum}')

    
