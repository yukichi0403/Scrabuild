#シェーカーソート
def shaker_sort(seq):
    right = len(seq) - 1
    left = 0
    swapped = 0
    count = 0
    while left < right:
        for i in range(left,right):
            if seq[i + 1] < seq[i]:
                seq[i],seq[i + 1] = seq[i + 1],seq[i]
                swapped = i
        right = swapped
    
        for i in range(right,left,-1):
            if seq[i] < seq[i - 1]:
                seq[i],seq[i - 1] = seq[i - 1],seq[i]
                swapped = i
        left = swapped
        count += 1

    return count

n = int(input())
input_list = list(map(int,input().split()))

print(shaker_sort(input_list))
print(*input_list)