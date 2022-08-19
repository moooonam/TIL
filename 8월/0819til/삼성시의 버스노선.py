T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_list =[]
    for i in range(N):
        bus_list.append(list(map(int, input().split())))
    jung_list = []
    p = int(input())
    for y in range(p):
        jung_list.append(int(input()))
    ans_list = [0]*5000
    for k in bus_list:
        a = k[0]
        b = k[1]
        for q in range(a-1, b):
            ans_list[q] +=1
    print(f"#{tc}", end =' ' )
    for m in range(p-1):
        print(f"{ans_list[jung_list[m]-1]}",end=' ')
    print(f"{ans_list[jung_list[p-1]-1]}")

    
