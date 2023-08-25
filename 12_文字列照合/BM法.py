#BM法
def bm_search(text, pattern): 
    t_len = len(text)
    p_len = len(pattern)
    
    # アルファベット小文字のみの想定 
    # 照合パターンの⻑さで初期化
    skip = [p_len]*26

    # スキップテーブルの作成・照合パターン最後の文字は飛ばす.
    # 先頭から見ていって一番最後に現れるのは末尾になる場合，対応するskipの値はp_lenになる.
    for i in range(p_len - 1): 
        skip[ord(pattern[i]) - 97] = p_len - i - 1
    
    # 照合対象側のカーソルを予め進める 
    t_i = p_len - 1

    # 照合対象の文字列全てをチェック 
    while t_i < t_len:
        # パターンのカーソルを一番最後にする
        p_i = p_len - 1
        t_i = p_len - 1 
        
        while t_i < t_len:
            p_i = p_len - 1
            # パターンの後ろから一致を確認するループ
            while text[t_i] == pattern[p_i]: 
                if p_i == 0: 
                    return t_i
                t_i -= 1; p_i -= 1
            t_i += max(skip[ord(text[t_i]) - 97], p_len - p_i)
    
    return -1
