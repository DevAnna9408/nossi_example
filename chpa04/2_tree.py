# Tree는 서로 연결된 Node의 계층형 자료구조로서, root와 부모 - 자식간의 subtree로 구성되어 있다.

# Node: 트리는 보통 노트로 구성된다.
# Edge: 노드간에 연결된 간선
# Root: 트리는 항상 루트에서 시작
# Leef: 더 이상 뻗을 수 없는 마지막 노드
# Child, Patent, Sibling 노드
# degree: 각 노드가 갖는 자식의 수 == 차수. 모든 노드의 차수가 n개 이하인 트리를 n진 트리라고 한다.
# ancestor: 위쪽으로 간선을 따라가면 만나는 모든 노드 == 조상
# descendant: 아래쪽으로 간선을 따라가면 만나는 모든 노드 == 자손
# height: 루트노드에서 가장 멀리 있는 리프노드 까지의 거리, 즉 리프노트중 최대 레벨 값
# subtree: 트리의 어떤 노드를 루트로 하고, 그 자손으로 구성된 트리를 subtree라고 한다.

# 이진트리(Binary Tree)를 중점으로 트리를 공부하면 된다.

# ex)

class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

bt = BinaryTree()
bt.root = Node(value=1)
bt.root.left = Node(value=2)
bt.root.right = Node(value=3)
bt.root.left.left = Node(value=4)

