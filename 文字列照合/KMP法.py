#KMP法
#完全一致する文字列の一番左のインデックスを出力
def create_table(pattern):
    skip = [0] * (len(pattern) + 1)
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            j += 1
            skip[i + 1] = j
        else:
            j = 0
            skip[i + 1] = j #一つ後ろに移動
    return skip


def kmp(text, zpattern):
    t_len = len(text)
    p_len = len(pattern)

    #スキップテーブル作る
    skip = create_table(pattern)
    t_i = p_i = 0

    #照合を行うループ
    while t_i < t_len and p_i < p_len:
            #一致している場合は両方のカーソルを進める
            if text[t_i] == pattern[p_i]:
                t_i += 1
                p_i += 1
            
            #照合パターンの１文字目で失敗した場合はテキスト側のカーソルを１つ進める
            elif p_i == 0:
                t_i += 1
            
            #２文字目以降で照合失敗した場合はスキップテーブルを参照
            else:   
                p_i = skip[p_i]

    if p_i == p_len:
        return t_i - p_i
    else:
        return -1
        

text = input()
pattern = input()

print(kmp(text,pattern))

    
