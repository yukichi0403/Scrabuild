#クイックソート
n = int(input())
input_list = list(map(int, input().split()))

def qsort(seq, l, r):
    global n
    if l >= r:
        return
    pivot = seq[r]
    cur_index = l
    for i in range(l, r):
        if seq[i] <= pivot:
            seq[cur_index], seq[i] = seq[i], seq[cur_index]
            cur_index += 1
            
    seq[cur_index], seq[r] = seq[r], seq[cur_index]
    if r - l == n - 1:
        print(*seq)

    qsort(seq, l, cur_index - 1)
    qsort(seq, cur_index + 1, r)

qsort(input_list, 0, n - 1)
print(*input_list)