T = int(input())
for tc in range(1, T+1):
    stack = []
    my_str = input()
    stack.append(my_str[0])
    for i in range(1, len(my_str)):
        if len(stack) == 0:
            stack.append(my_str[i])
            continue
        if my_str[i] == stack[-1]:
            stack.pop(-1)
        else:
            stack += my_str[i]
    print(f"#{tc} {len(stack)}")


