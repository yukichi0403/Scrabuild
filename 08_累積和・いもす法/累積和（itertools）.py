from itertools import accumulate

L = list(range(1,7)) #[1,2,3,4,5,6]
AC = list(itertools.accumulate(L))+[0] #[1,3,6,10,15,21,0]


l,r=0,4
print(AC[r]-AC[l-1])# 15 (AC[4]：15 - AC[-1]:0 = 15)
#末尾に0をつけておけば１つ目の値単体の累積和もそのまま求められる

