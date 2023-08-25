from heapq import heappop,heappush

L=[3,0,2,5,7,2]
H=[]

for l in L: #ここはH=heapq.heapify(L)でもいいです。
    heappush(H,l) 

print(H) #[0, 3, 2, 5, 7, 2]

print(heappop(H)) #0
print(heappop(H)) #2
print(heappop(H)) #2

