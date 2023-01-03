T = int(input())
for tc in range(1, T+1):
    sik = list(input().split())
    result = 0
    stack = []
    for i in range(len(sik)-1):
        if sik[i] == ".":
            break
        elif sik[i].isdigit() :
            stack.append(sik[i])

        elif len(stack) < 2:
            result = 'error'
            break
        
        else:
            right = int(stack.pop())
            left = int(stack.pop())

            if sik[i] == "+":
                result = right + left
            elif sik[i] == "*":
                result = right * left
            elif sik[i] == "/":
                result = left // right
            elif sik[i] == "-":
                result = left - right
            
            stack.append(result)
    if len(stack) > 1:
        result = 'error'
    
    print(f"#{tc} {result}")