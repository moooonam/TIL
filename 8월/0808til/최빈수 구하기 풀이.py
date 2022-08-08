T = int(input())

for t in range(1, T+1):
    case=int(input())

    scores = list(map(int, input().split())) #점수들이 들어가있는 리스트

    max_count = 0 #최대 빈도수
    counts=[0]*101 # 점수 개수 세기 점수의 범위는 0부터 100까지

    for score in scores:
        #score = 점수
        #counts[score]=score 점수가 몇번 출현했는지 나타내는 값(빈도수)
        counts[score] +=1
        max_count = counts[score] if max_count < counts[score] else max_count # 최대빈도수 구하기


    #최대 점수 구하기
    # 빈도수가 같을 때 해당 점수가 1개 있든 2개 있든 다 구해주면 된다.
    max_score =0 #최대 빈도수 (제일 많이 등장한 점수)중에 제일 큰 점수
    for score in range(len(counts)):
        if max_count == counts[score]: #두 값이 같으면 현재 score는 최대 빈도 점수
            max_score = score