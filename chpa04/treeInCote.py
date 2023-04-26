# Lowest Common Ancestor of a Binary Tree

# 문제에서 이진트리 하나와 해당 트리에 속한 두 개의 노드가 주어진다.
# 이 때 두 노드의 공통 조상 중 가장 낮은 node를 찾아라

def lowestCommonAncestor(root, p, q):
    if root is None:
        return None

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right

lowestCommonAncestor(root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], p = 5, q = 1)