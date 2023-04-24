# 물리적 비연속적, 논리적 연속적을 가진 데이터의 집합
# 각 node는 value와 next 주소값을 가지고 있기 때문에
# 총 메모리 할당량은 늘어나지만, 메모리 저장 시 유연성을 가지고 있다.

# LinkedList 클래스를 만들 때 첫 번째 노드를 head로 해서 반드시 가져야 한다.
# get, insert_back, insert_front, insert_at, remove_back, remove_front, remove_at 등등을 구현 해 본다.

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def append_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def insert_at(self, idx, value):

        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(idx - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

# 파이썬에서는 참조하는 대상이 없으면 garbage collector가 알아서 삭제 해 준다고 한다.
    def remove_at(self, idx):
        if idx == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(idx - 1):
                current = current.next

            current.next = current.next.next

li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.append(4)

print(li.get(1))

#linked list의 코테 적용 방법
# 선형 자료구조 + 중간에 데이터를 추가 / 삭제하는 것이 용이하다.
# Tree or Graph에 활용


















