#配列の要素を順番に後ろから⾒ていく場合のバブルソート
def bubblesort(seq):
  size = len(seq)
  for i in range(size):
    #うしろから逆にみていく
    for j in range(size-1, i, -1):
      #今⾒ている要素（j番⽬）が1つ前の要素（j-1番⽬）より⼩さい場合，場所を⼊れ替える．
      if seq[j] < seq[j-1]:
        seq[j], seq[j-1] = seq[j-1], seq[j]
