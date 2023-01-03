T = 10
for tc in range(1, 11):
    a, my_str = input().split()
    a = int(a)
    stack = [my_str[0]]
    for i in range(1, len(my_str)):
        if len(stack) == 0:
            stack.append(my_str[i])
            continue
        if my_str[i] == stack[-1]:
            stack.pop(-1)
        else:
            stack += my_str[i]
        b = ''.join(stack)
    print(f"#{tc} {b}")