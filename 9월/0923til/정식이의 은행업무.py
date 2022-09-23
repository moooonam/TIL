def twototen(n):#n은 리스트 형태로, 2진수를 10진수로
    num=0
    gob=1
    for i in range(len(n)-1,-1,-1):
        num+=n[i]*gob
        gob*=2
    return num

def threetoten(n):#n은 리스트 형태로, 3진수를 10진수로
    num=0
    gob=1
    for i in range(len(n)-1,-1,-1):
        num+=n[i]*gob
        gob*=3
    return num

T = int(input())
for tc in range(1,T+1):
    num_2=list(input())
    num_3=list(input())
    ans=0

    for i in range(len(num_2)):# 정수로 바꾸기
        num_2[i]=int(num_2[i])
    for i in range(len(num_3)):
        num_3[i]=int(num_3[i])
    start_3=num_3[:] # 3진수 초기값

    for i in range(len(num_2)-1,-1,-1):
        if num_2[i]==1: # 한자리 바꾸기
            num_2[i]=0
        else:
            num_2[i]=1
        if i <len(num_2)-1:#전에 바꾼거 초기화 하기
            if num_2[i+1]==1:
                num_2[i+1]=0
            else:
                num_2[i+1]=1
        for j in range(len(num_3)-1,-1,-1):
            for k in range(3):
                num_3[j]=k
                # print(num_2,num_3)
                if twototen(num_2)==threetoten(num_3) and num_3!=start_3:
                    ans = twototen(num_2)
                    break
            num_3[j]=start_3[j]
            if ans!=0:
                break
        if ans!=0:
            break
            
    print(f'#{tc} {ans}')


