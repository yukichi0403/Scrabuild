w_limit= 15
weight = [11, 2, 3, 4, 1, 5]
value = [15, 3, 1, 4, 2, 8]
note = [[-1] * (w_limit+1) for _ in range(len(weight))]

def knapsack_rec(cur_i, cur_w):
    # すべての品物を考慮したあとは価値が増えることはない
    if cur_i < 0: 
        return 0
    # メモがあれば，すぐさまそれを使う
    if note[cur_i][cur_w] > -1:
        return note[cur_i][cur_w]
    
    # 今考えているアイテムが現在の入れられる残りの重さを超えている場合は，入れずに1つ前に.
    if w_limit - cur_w < weight[cur_i]:
        note[cur_i][cur_w] = knapsack_rec(cur_i - 1, cur_w) 
        return note[cur_i][cur_w]
    
    else: #not_inは入れない，is_inは入れる場合
        not_in = knapsack_rec(cur_i, cur_w)
        is_in = knapsack_rec(cur_i - 1, cur_w - weight[cur_i])+ value[cur_i] # より大きい方をメモに残す
        note[cur_i][cur_w] = max(not_in, is_in)
        return note[cur_i][cur_w]