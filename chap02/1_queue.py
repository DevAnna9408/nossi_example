# queue: 선입선출의 트성을 가진 구조
# 큐의 앞에 데이터를 저장하는 것을 dequeue, 뒤에 저장 하는 것을 enqueue

# queue를 list 형태로 선언하면 아래와 같다.

q = []

# queue의 enqueue와 같다
q.append(1)
q.append(2)
q.append(3)
q.append(4)

# queue의 dequeue와 같다
q.pop(0)
q.pop(0)
q.pop(0)

# 하지만 이 경우에 시간 복잡도는 O(n)이 되기 때문에 list 형태로 구현하지 않고 파이썬에서 지원하는 queue의 형태로 만들어 준다.

from collections import deque

# deque는 양방향으로 en / dequeue를 할 수 있다.
queue = deque

# enque
queue.append(1)
queue.append(2)
queue.append(3)

# dequeue
queue.popleft()
queue.popleft()
queue.popleft()

