#拡張ユーグリッドの互徐法
def ext_gcd(a,b):
    #基底であるbが0になったら再帰が返る
    if b == 0:
        return a, 1, 0
    
    #qx + y = s, x = t → x = t, y = s - qt
    else:
        d, x, y = ext_gcd(b, a % b)
        return d, y, x - (a // b) * y