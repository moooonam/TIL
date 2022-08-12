for tc in range(1, 11):
    t= int(input())
    my=input() #찾을거
    word=input() #전체문자
    m=len(my) 
    n=len(word)
    count=0
    for i in range(n):
        if word[i:i+m]==my:
            count+=1
            i+=1
        else:
            i+=1
    print(f'#{t} {count}')

    
