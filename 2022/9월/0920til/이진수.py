T = int(input())
for tc in range(1, T+1):
    N, num_16 = input().split()
    my_dict={
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111'
        }
    ans=[]
    for i in range(int(N)):
        ans.append(my_dict[num_16[i]])
    print(f'#{tc} {"".join(ans)}')


# 교수님 풀이
T = int(input())
for tc in range(1, T+1):
    n, hex_num = input().split()
    print(f'#{tc}', end="")
    for i in range(int(n)):
        num = int(hex_num[i], 16) # i번째 있는 문자열을 16진수로 바꾼다.
        for j in range(3,-1,-1):
            if num&(2**j)== 0:
                print("0", end="")
            else:
                print("1", end="")
    print()
