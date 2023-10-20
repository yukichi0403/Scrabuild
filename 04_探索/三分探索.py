#(1)最小にしたい関数fを定義する
def f(x):
    return sum((x + a) - min(a,x * 2) for a in A) / N


#(2)関数fの最小値を探したい閉区間の両端をl,rと置く(left <= right)
left,right=0,max(A)
limit = pow(10, -6) #誤差の範囲の設定

#(3)誤差が10^-8を下回るまでwhile文を回す
while left + limit < right:
    #(4)オーバーフローしないように以下のように三等分点を置く
    c1 = left + (right - left)/3
    c2 = right - (right - left)/3
    #(5)更新を行う
    if f(c1) < f(c2):
        right = c2
    else:
        left = c1

#(6)最終的に出力するのはl,rのどちらでも良い
print(f(left))
