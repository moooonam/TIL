def get_prime(n):# n까지의 숫자중에서 소수를 구한다.
    arr = [True]*(n+1)
    for i in range(2, int(n*(1/2))):
        if arr[i]: # 만약 i번째 수가 소수다
            # 소수의 배수를 모두 소사가 아니라고 체크
            for j in range(i+i, n+1, i):
                arr[j] =False
    return [i for i in range(2, n+1) if arr[i]==True]

all_list=get_prime(1000000)
T = int(input())
for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    my_list=[]
    count=0
    for p in range(len(all_list)):
        if all_list[p]>B:
            break
        elif all_list[p]>=A:
            my_list.append(all_list[p])

    for q in my_list:
        if str(D) in str(q):
            count+=1
    # print(all_list)
    print(f'#{tc} {count}')

