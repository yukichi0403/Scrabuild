class CombinationCalculator:
    """
    modを考慮したPermutation, Combinationを計算するためのクラス
    """    
    def __init__(self, size, mod):
        self.mod = mod
        self.factorial = [0] * (size + 1)
        self.factorial[0] = 1
        for i in range(1, size + 1):
            self.factorial[i] = (i * self.factorial[i - 1]) % self.mod
        
        self.inv_factorial = [0] * (size + 1)
        self.inv_factorial[size] = pow(self.factorial[size], self.mod - 2, self.mod)

        for i in reversed(range(size)):
            self.inv_factorial[i] = ((i + 1) * self.inv_factorial[i + 1]) % self.mod

    def calc_combination(self, n, r):
        if n < 0 or n < r:
            return 0

        if r == 0 or n == r:
            return 1
        
        ans = self.inv_factorial[n - r] * self.inv_factorial[r]
        ans %= self.mod
        ans *= self.factorial[n]
        ans %= self.mod
        return ans
    
    def calc_permutation(self, n, r):
        if n < 0 or n < r:
            return 0

        ans = self.inv_factorial[n - r]
        ans *= self.factorial[n]
        ans %= self.mod
        return ans




#桁が小さくMODを取る必要がない時
from math import factorial
print(factorial(n) // factorial(r) // factorial(n - r))




"""pypyのアップデートによるMLEするので使えないかも。。
#桁が大きくMODを取る必要がある時
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10 ** 9 + 7
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

print(cmb(n, r, p))
"""


