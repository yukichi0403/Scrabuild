#da[i][j]:(0,0)~(i,j)の長方形の和
def da_generate(h,w,a):
    da = [[0]*w for j in range(h)]
    
    #da[0][0] には、元の配列 a の (0,0) の要素の値をそのままコピー
    da[0][0] = a[0][0]

    #行0に対して、1列目から最後の列までの累積和を計算して da[0][i] に格納
    for i in range(1,w):
        da[0][i] = da[0][i-1]+a[0][i]

    #行２について、１行ごとにその行における累積和を計算し、１つ上の行の値に加算する
    for i in range(1,h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i-1][j]+cnt_w
    return da
 
#da_calc(p,q,x,y):(p,q)~(x,y)の長方形の和
def da_calc(p,q,x,y):
    if p > x or q > y:
        return 0
    if p == 0 and q == 0:
        return da[x][y]
    if p == 0:
        return da[x][y]-da[x][q-1]
    if q == 0:
        return da[x][y]-da[p-1][y]
    return da[x][y]-da[p-1][y]-da[x][q-1]+da[p-1][q-1]


"""
#いもす法の場合の例
imos = [[0] * 1001 for _ in range(1001)]

#左上、左下の座標はプラス、右上、右下の座標はマイナス（マイナス座標についてプラス１は不要）
for _ in range(N):
    lx,ly,rx,ry = map(int,input().split())
    imos[lx][ly] += 1
    imos[rx][ry] += 1
    imos[lx][ry] -= 1
    imos[rx][ly] -= 1

da = da_generate(1001,1001,imos)
"""
