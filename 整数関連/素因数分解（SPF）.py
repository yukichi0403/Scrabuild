def spf(n):
  spf = [_ for _ in range(n+1)]; i = 2
  while i*i <= n:
    if spf[i] == i:
      j = 2*i
      while j <=n:
        if spf[j] == j:
          spf[j] = i
        j += i
    i += 1
  return spf


def PrimeFactorization(n):
  spf_table = spf(n)
  while n > 1:
    print(spf_table[n])
    n //= spf_table[n]

