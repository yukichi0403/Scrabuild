#順列の列挙
from itertools import permutations
A=[1,2,3,4]

for i in permutations(A,2):
    print(i,end=' ')
#(1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3) 
