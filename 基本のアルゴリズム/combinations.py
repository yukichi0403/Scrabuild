#組み合わせの列挙
from itertools import combinations
A=[1,2,3,4]

for i in combinations(A,2):
    print(i, end=' ')
#(1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4) 
