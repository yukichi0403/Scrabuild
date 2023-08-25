N = int(input())
*A, = map(int, input().split())

# BIT
# 0indexは使わないのでN+1
BIT = [0] * (N+1)
def add(k, x):
    while k <= N:
      BIT[k] += x
    　　　#ビット演算にあたりkが０以下の場合は無限ループの陥るので注意
      k += k & -k
        
def get(k):
    ans = 0
    while k:
        ans += BIT[k]
        #ビット演算にあたりkが０以下の場合は無限ループの陥るので注意
        k -= k & -k
    return ans

#答えを求める
ans = 0
for i, a in enumerate(A):
    # 自分より小さい要素がいくつ存在するかを計算
    ans += (N-1-i) - get(a)
    add(a, 1)
print(ans)
