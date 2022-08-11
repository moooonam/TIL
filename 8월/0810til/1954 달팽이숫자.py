# 넘 어려운거 아닌교
T= int(input())

for tc in range(1, T+1):
    n= int(input())

    di = [0,1,0,-1] # 우 하 좌 상
    dj = [1,0,-1,0]
    d = 0 # 현재 채우고 있는 방향

    snail = [[0]*n for _ in range(n)] #0으로 채워진 2차원 배열
    
    # 맨 첫칸 (0,0)에 값을 채워놓고 시작
    value = 1
    ci, cj = 0,0 

    snail[ci][cj] = value

    # 반복을 통해 달팽이를 채워 나갈껀데 언제까지 채워 나가야할까
    # value가 n*n이 될때까지 계속 반복하면 된다.
    while value < n*n:

        ni= ci +di[d]
        nj= cj +dj[d] #일단 출발함 현재 방향은 d에 저장 되어있음
        # 인덱스 범위를 벗어났거나 내가 이미 채웠던 곳이라면 방향을 바꿔야함
        # 상하좌우가 막혀있다 => 값채우기가 끝났다.
        for i in range(4):
            d= (d+i)%4
            ni = ci +di[d]
            nj = cj +dj[d]
            #만약 갈수 있는 방향이없다면 방향 바꾸기 종료
            if 0<=ni<n and 0<=nj<n and snail[ni][nj] == 0:
                ci=ni
                cj=nj
                break
        value += 1
        snail[ci][cj]= value
    print(f"#{tc}")
    for i in range(n):
        for j in range(n):
            
            
   

   
