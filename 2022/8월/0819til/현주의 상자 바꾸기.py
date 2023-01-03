T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    vin = [0]*N
    for i in range(Q):
        l, r = map(int, input().split())
        for p in range(l-1,r):
            vin[p] = i+1
    ans = " ".join(map(str, vin))
    print(f"#{tc} {ans}") 
  
 