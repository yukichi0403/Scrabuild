import bisect

N,T = map(int,input().split()) 
A = list(map(int,input().split()))

#偶数番目の和の全パターンのリスト
gusu = [0]
#奇数番目の和の全パターンのリスト
kisu = [0]

for i in range(N):
    #偶数番目の和の全パターンを格納
    if i % 2 == 0:
        for j in range(len(gusu)):
            gusu.append(A[i] + gusu[j])
    #偶数番目の和の全パターンを格納
    else:
        for k in range(len(kisu)):
            kisu.append(A[i] + kisu[k])

gusu.sort()
kisu.sort()

ans = 0
for g in gusu:
    #求めている数を超えた場合は即終了
    if g > T:
        break
    #bisect_right-1でT-g以下で最も大きい値を特定
    ind = bisect.bisect_right(kisu,T - g) - 1
    k = kisu[ind]
    ans = max(ans, g + k)

print(ans)
