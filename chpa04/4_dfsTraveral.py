# DFS의 전위순회, 중위순회, 후위순회

# preorder: 전위순회

# 방문을 먼저 한 다음 다음 노드에 접근
def preorder(cur_node):
    if cur_node is None:
        return

    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

# 하나를 접근 한 다음 방문하고 다음 노드에 접근, 나 자신을 방문하는건 가운데
def inorder(cur_node):
    if cur_node is None:
        return

    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)

# 자식 노드를 전부 방문 한 다음 자기 자신에게 접근
def postorder(cur_node):
    if cur_node is None:
        return

    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)
