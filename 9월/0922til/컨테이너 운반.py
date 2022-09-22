T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())# N= 컨테이너수 # M=트럭수
    mass = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    mass.sort(reverse=True)
    truck.sort(reverse=True)
    full_truck=[0]*100
    for i in range(N): # 컨테이너 돌자
        for j in range(M): # 트럭돌기
            if full_truck[j]==0 and mass[i]<=truck[j]:
                full_truck[i]=mass[i]
                break
    print(f'#{tc} {sum(full_truck)}')

