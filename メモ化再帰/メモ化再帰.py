from functools import lru_cache

#maxsizeには、直近の何回分を記憶しておくかを指定する　Noneの場合は、制限なく記憶
@lru_cache(maxsize=1000)

#例としてフィボナッチ数列の場合
def fib_memoized(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
