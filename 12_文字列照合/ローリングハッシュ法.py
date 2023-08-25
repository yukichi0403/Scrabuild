#ローリングハッシュ法
def RollingHashMatch(text, pattern):
    base = 31  # 基数
    h = 998244353  # 除数
    ans_list = []

    t_len = len(text)
    p_len = len(pattern)
    t_hash = 0  # 照合対象側のハッシュ
    p_hash = 0  # 照合パターン側のハッシュ

    # textの最初からp_len文字目,patternのハッシュ値をそれぞれ計算
    for i in range(1,p_len + 1):
        t_hash = (t_hash + (base ** (p_len - i) * (ord(text[i - 1]) - 96))) % h
        p_hash = (p_hash + (base ** (p_len - i) * (ord(pattern[i - 1]) - 96))) % h

    # 最初の時点で一致したらindex:0を返す
    if t_hash == p_hash:
        print(0)

    al = 1
    for i in range(p_len):
        al = ( al * base ) % h 

    l = 0
    start = 0
    for start in range(1, t_len - p_len):
        t_hash = (t_hash * base - ((al * (ord(text[start-1]) - 96)) % h) + (ord(text[start + p_len - 1]) - 96)) % h
        if t_hash == p_hash:
            ans_list.append(start)
    
    for i in ans_list:
        print(i)

    # 見つからない場合は何も返さない
    return

text = input()
pattern = input()

RollingHashMatch(text, pattern)