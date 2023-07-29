#仮に、1～10000までの階乗を全て求める場合

#MODなしfactorial、実行時間PyPyにて4000ms以上
import math
fact = [1]
for n in range(1,10001):
    fact.append(math.factorial(n))

# Modなし 150ms程度
fact = [1]
for n in range(1,10001):
    fact.append(fact[-1]*n)

#MODありfactorial、実行時間PyPyにて4000ms以上
MOD = 10**9+7
fact = [1]
for n in range(1,10001):
    fact.append(math.factorial(n)%MOD)

#MODあり　100msを切る
MOD = 10**9+7
fact = [1]
for n in range(1,10001):
    fact.append(fact[-1]*n%MOD)
