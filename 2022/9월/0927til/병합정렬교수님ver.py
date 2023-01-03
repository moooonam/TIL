def merge_sort(m):
    if len(m) ==1:
        return m
    
    left = right =[]
    mid = len(m)//2
    
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
def merge(left, right):
    ln = len(left)
    rn = len(right)
    li=ri=0
    retult=[]
    while li < ln or ri<rn:
        if li < ln and ri < rn:
            if left[li] <= right[ri]:
                result.append(left[li])
                li +=1
            else:
                result.append(right[ri])
                ri+=1
        elif li < ln:
            result.append(left[li])
            li +=1
        elif ri < rn:
            result.append(right[ri])
            ri+=1
    return result
