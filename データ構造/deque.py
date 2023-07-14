from collections import deque

l = [0,1,2,3]
q = deque(l)
q.append(4) # 後ろから4を挿入, l=deque([0,1,2,3,4])
q.appendleft(5)#前から5を挿入, l=deque([5,0,1,2,3,4])
x = q.pop() #後ろの要素を取り出す, x=4, l=deque([5,0,1,2,3])
y = q.popleft() # 前の要素を取り出す, y=5, l = deque([0,1,2,3])