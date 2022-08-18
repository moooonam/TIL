T = int(input())
for tc in range(1, T+1):
    my_str = input()
    ans = 1
    stack = []
    for i in my_str:
        if i == "(":
            stack.append(i)
        elif i == "{":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0 or stack[-1] == "{":
                ans = 0
                break
            stack.pop(-1)
        elif i == "}":
            if len(stack) == 0 or stack[-1] == "(":
                ans = 0
                break
            stack.pop(-1)
    if len(stack) > 0:
        ans = 0
    print(f"#{tc} {ans}")













    # a = 0
    # b = 0
    # ans = 0
    # my_str = input()
    # for i in range(len(my_str)):
    #     if a < 0 or b < 0:
    #         ans = 0
    #         break
    #     if my_str[i] == "(":
    #         a += 1
    #     elif my_str[i] == ")":
    #         a -= 1
    #     if my_str[i] == "{":
    #         b += 1
    #     elif my_str[i] == "}":
    #         b -= 1
    # if a == 0 and b == 0:
    #     ans = 1
    # print(f"#{tc} {ans}")
# 스택 없이 하려했는데 {(}) 이런 반례가 있음
