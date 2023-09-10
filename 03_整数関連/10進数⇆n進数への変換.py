"""パターン１"""
def basen_to_10(num_n, n):  # n進数→10進数に変換
    if num_n == 0:
        return 0
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

def base10_to_n(num_10, n):  # 10進数→n進数に変換
    if num_10 == 0:
        return 0
    str_n = ''
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return int(str_n[::-1])



"""パターン2"""
#10進数の整数Xをn進数に変換する関数
def Base_10_to_n(X, n):
    if (int(X / n)):
        return Base_10_to_n(int(X / n), n) + str(X % n)
    return str(X % n)

#n進数を10進数の整数Xに変換する関数
def Base_n_to_10(X, n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i]) * (n ** (i - 1))
    return out #int out
