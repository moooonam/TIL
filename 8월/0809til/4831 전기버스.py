# T = int(input())
# for i in range(T):
#     k, n, m = map(int, input().split()) 
#     jung_list= list(map(int, input().split()))
#     jung_list.insert(0, 0) # 충전기 리스트 제일 앞에 0 추가 (출발점에서 충전을 했으니까)
#     jung_list.append(n)
#     count=0
#     tank=k # 연료통 처음에 풀충 상태
#     for j in range(len(jung_list)-1):
#         if tank+k <jung_list[j+1]-jung_list[j]: #도착 못할경우
#             count=0
#             break
#         elif tank<jung_list[j+1]-jung_list[j]: # 연료가 거리보다 부족하면 충전
#             tank+=k
#             count+=1
#             tank-=jung_list[j+1]-jung_list[j]
#         else:
#             tank-=jung_list[j+1]-jung_list[j] # 연료가 거리보다 많으면 연료 소모
            
#     print(f'#{i+1} {count}')
#-----------------------------------------------------------------------------
# 나는 연료가 남는다고 생각했는데 걍 다음 정류장 까지만 가면 되는거였음
# T = int(input())
# for i in range(T):
#     k, n, m = map(int, input().split()) 
#     jung_list= list(map(int, input().split()))
#     jung_list.insert(0, 0)
#     jung_list.append(n)
#     count =0
#     for j in range(len(jung_list)-1):
#         if jung_list[j+1]-jung_list[j]>k:
#             count=0
#             break
#         for l in range(len(jung_list)-2):
#             if jung_list[l+2]-jung_list[l]>k:
#                 count+=1

#     print(f'#{i+1} {count/(len(jung_list)-1)}')
# 두칸씩 띄어서 비교하는 생각을 했는데 반례가 너무 많음
#---------------------------------------------------------------------------------
# 결국 구글의 힘을 빌림
T = int(input())
for i in range(T):
    k, n, m = map(int, input().split()) 
    jung_list= list(map(int, input().split()))
    count =0
    my_position=0
    while my_position+k<n:
        for s in range(k,0,-1):
            if (my_position+s) in jung_list:
                my_position+=s
                count+=1
                break
        else:
            count=0
            break
    print(f'#{i+1} {count}')
#--------------------------------------------------------------------------
#교수님 풀이
def drive(K, N): # 버스를 운행하는 함수
    #return=0 :충전소가 제대로 배치되어있지 않아서 완주 불가능
    #return>0 : 충전소가 제대로 배치되어있다.
    last = 0 #마지막 충전했던 위치
    next = k #버스가 최대로 이동한 위치(초기값은 한번 이동한 상태로)
    count=0 #충전한 횟수
    while next<N:
        #버스가 이동한 위치에 충전기가 있나 없나 검사, 충전기가 없다면 뒤로 한칸씩 돌아가면서 찾을때까지 뒤로간다
        #만약 뒤로 갔는데 내가 마지막으로 충전한 위치까지 와버렸다면 0을출력
        while stop[next]==0:
            next-= 1 # 한칸씩 뒤로 이동
            if next == last:
                return 0
            last = next
            next+= K
            count+=1
    return count
T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    stop= [0]*N #정류장리스트(1:충전소가 있는 정류장, 0:충전소가 없는 정류장)
    for x in charge: #x는 충전소가 있는 정류장의 위치
        stop[x]=1
    answer = drive(K, N)
    print(f'#{tc} {answer}')

    
        
