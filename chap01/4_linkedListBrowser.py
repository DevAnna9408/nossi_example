# 인터넷 브라우저에서 방문기록과 동일한 작동을 하는 브라우저를 구현 할 것이다. 구현할 브라우저는 home에서 시작하고, 이후 다른 url에 방문 할 수 있다.

# BrowserHistory를 호출하면 브라우저는 home에서 시작이 된다.
# visit를 호출하면 현재 page뒤에 있는 페이지 기록은 다 삭제가 되고 url로 방문한다.
# back을 호출하면 steps 수만큼 뒤로가기를 한다.
# forward를 호출하면 steps 수만큼 앞으로가기를 한다.

class Node:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = Node(homepage)

    def visit(self, url):
        self.current.next = Node(value=url, prev=self.current)
        self.current = self.current.next
        return None

    def back(self, idx):
        while idx > 0 and self.current.prev is not None:
            idx -= 1
            self.current = self.current.prev
        return self.current.value

    def forward(self, idx):
        while idx > 0 and self.current.next is not None:
            idx -= 1
            self.current = self.current.next

        return self.current.value
