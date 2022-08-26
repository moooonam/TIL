class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 전위순회 V L R
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

v = int(input())
tree = [Node(i) for i in range(v+1)]

edge_list = list((map(int, input().split())))
# 입력을 두개씩 잘라서 확인
# 앞 => 부모 p
# 뒤 => 자식 c
while edge_list:
    p = edge_list.pop(0) # 부모
    c = edge_list.pop(0) # 자식

    if tree[p].left:
        tree[p].right = tree[c]
    else:
        tree[p].left = tree[c]

#전위순회 시작
preorder(tree[1])
print()
