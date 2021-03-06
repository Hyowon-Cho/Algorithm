"""
큐 자료구조

먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조

삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) -삽입(4) - 삭제()

"""

from collections import deque

queue = deque()

# If we use the example that I wrote

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)


"""

deque([3, 7, 1, 4])
deque([4, 1, 7, 3])
