import collections

def prime_factorize(n):
  prime_factor = []
  #2で割れる限り割る
  while n % 2 == 0:
    prime_factor.append(2)
    n //= 2
  f = 3
  #fの2乗がn以下の限りfを増やしながら割り切れる数を探索
  while f * f <= n:
    if n % f == 0:
      prime_factor.append(f)
      n //= f
    #2で割り切れないことは既に確認ずみなので割り切れない場合は２を増やして奇数だけ探索
    else:
      f += 1
  #nが1でない場合はn自体を追加
  if n != 1:
    prime_factor.append(n)
  
  return prime_factor

print(prime_factorize(1))
# []

print(prime_factorize(36))
# [2, 2, 3, 3]

print(prime_factorize(840))
# [2, 2, 2, 3, 5, 7]

c = collections.Counter(prime_factorize(840))
print(c)
# Counter({2: 3, 3: 1, 5: 1, 7: 1})
