#バケットソート
# 0からmax_valueまでの整数値のみと想定 
def countsort(seq, max_value):
    count = [0] * (max_value + 1) # バケツ 
    sorted = [] # ソート済み配列

    # 出現回数をカウント 
    for i in range(len(seq)):
        count[seq[i]] += 1
    
    # 出現回数からソート済み配列を生成 
    for i in range(len(count)):
        for j in range(count[i]): 
            sorted.append(i)
    
    return sorted