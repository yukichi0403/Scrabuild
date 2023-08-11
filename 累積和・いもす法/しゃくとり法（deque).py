q = deque()
for c in a:
    q.append(c)  ## dequeの右端に要素を一つ追加する。
    (追加した要素に応じて何らかの処理を行う)

    while not (満たすべき条件):
        rm = q.popleft() ## 条件を満たさないのでdequeの左端から要素を取り除く
        (取り除いた要素に応じて何らかの処理を行う)

    (何らかの処理を行う。whileがbreakしたので、dequeに入っている連続部分列は条件を満たしている。特に右端の要素から左に延ばせる最大の長さになっている。)




#例（長さnの整数列の連続部分列で、その要素の積が以下となるものの長さの最大値を求める問題）
## 入力の受け取り
n, k = map(int, input().split())
a = [int(input()) for i in range(n)]

## コーナーケースの処理
if 0 in a:
    print(n)
    exit()

ans = 0
q = deque()
p = 1  ## 今、見ている区間の要素の積をpで管理する。
for c in a:
    q.append(c)  ## dequeの"右端"に要素を一つ追加する。
    p *= c

    while q and p > k: ## 要素の積がKを超えているか？
        rm = q.popleft() ## 条件を満たさないのでdequeの"左端"から要素を取り除く
        p //= rm ## 取り除いた値に応じて要素の積を更新する

    ans = max(ans, len(q)) ## dequeに入っている要素の積がK以下になるまで区間を縮めた。

print(ans)


