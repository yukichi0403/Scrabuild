from functools import lru_cache

#maxsizeには、直近の何回分を記憶しておくかを指定する　Noneの場合は、制限なく記憶
@lru_cache(maxsize=1000)

#例としてフィボナッチ数列の場合
def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
