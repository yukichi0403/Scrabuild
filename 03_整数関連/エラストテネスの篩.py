#エラストテネスの篩
N = int(input())

def sieve_of_eratosthenes(n):
    #素数かどうかを格納するリストを全でTrueで初期化
    primes = [True] * (n + 1)

    #0,1は素数ではないのでFalseに変更
    primes[0] = primes[1] = False

    #2からスタート
    p = 2

    #2乗がn以下の値までループでチェック
    while p * p <= n:
        #pが素数の場合に
        if primes[p]:
            #pの倍数でn以下の値は全て素数でないと記録
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    #素数のものだけ＝Trueのものだけをリストに追加
    result = []
    for i in range(2, n + 1):
        if primes[i]:
            result.append(i)

    return result
