# Maximum Depth of Binary Tree


from collections import deque

def mdbt(root):
    level = 0
    if root is None:
        return 0
    q = deque()
    q.append((root, 1))
    while q:
        cur_node, cur_depth = q.popleft()
        level = cur_depth
        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth + 1))

    return level

def mdbt_post(root):

    if root is None:
        return 0

    left_depth = mdbt_post(root.left)
    right_depth = mdbt_post(root.right)
    return max(left_depth, right_depth) + 1