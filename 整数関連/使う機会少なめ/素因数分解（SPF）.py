#pythonだとTLEするのであまり使えないかも

def spf(n):
  #0からnまでの各数値に対してその最小の素因数を保持する
  spf = [_ for _ in range(n+1)]; i = 2
  while i*i <= n:
    #iがまだ他の数値によって最小素因数として更新されていない場合は
    if spf[i] == i:
      #j を i の倍数として2から順番に増やしながら処理を行う
      j = 2*i
      while j <=n:
        #jはiの倍数なので、まだ他の最小素因数として更新されていない場合はiを最小の素因数として格納
        if spf[j] == j:
          #iは小さい数から順に増えていくので、一度でも更新されたらもう更新不要
          spf[j] = i
        j += i
    i += 1
  return spf


def PrimeFactorization(n):
  spf_table = spf(n)
  insu = []
  while n > 1:
    insu.append(spf_table[n])
    n //= spf_table[n]
  return insu

