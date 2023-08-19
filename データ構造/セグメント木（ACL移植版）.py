#使い方：https://github.com/shakayami/ACL-for-python/wiki/segtree

class Segtree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
  
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        #セグ木のノードの数は元データ以上の数になる最小の２の冪乗（これを2Nとする）-1
        #葉ノードはNなので葉ノード以外の部分の長さはN-1
        #これをbit_length(ビット表示した場合の長さ、８の場合は1000で４）を使って求めている
        self.log=(self.n-1).bit_length()
        #葉ノード以外の部分の長さ＝self.size
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)
            
    #p番目の値をxに変えることができる。
    def set(self,p,x):
        assert 0<=p and p<self.n
        #葉ノードにアクセスして値をxに更新
        p+=self.size
        self.d[p]=x
        #親ノードに登っていき値を更新
        for i in range(1,self.log+1):
            self.update(p>>i)

    #p番目の値が返ってくる
    def get(self,p):
        assert 0<=p and p<self.n
        return self.d[p+self.size]

    #[l,r)の範囲内での演算を求めた結果が返ってくる。 
    #ただし、範囲はl ~ r-1であり、rが含まれていない点に注意！！！！
    #例えばセグ木関数がmaxだった場合max(A_l,...,A_{r-1})が返ってくる。 
    #セグ木関数が足し算だった場合A_l+...+A_{r-1}が返ってくる。
    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        sml=self.e
        smr=self.e
        l+=self.size
        r+=self.size
        while(l<r):
            if (l&1):
                sml=self.op(sml,self.d[l])
                l+=1
            if (r&1):
                smr=self.op(self.d[r-1],smr)
                r-=1
            l>>=1
            r>>=1
        return self.op(sml,smr)

    #全区間での演算結果を求める
    def all_prod(self):
        return self.d[1]

    #二分探索をする。ここで、始点はlであり、単調性のある関数fの実行結果が変わる切れ目を求める。
    def max_right(self,l,f):
        assert 0<=l and l<=self.n
        assert f(self.e)
        if l==self.n:
            return self.n
        l+=self.size
        sm=self.e
        while(1):
            while(l%2==0):
                l>>=1
            if not(f(self.op(sm,self.d[l]))):
                while(l<self.size):
                    l=2*l
                    if f(self.op(sm,self.d[l])):
                        sm=self.op(sm,self.d[l])
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l+=1
            if (l&-l)==l:
                break
        return self.n

    #二分探索をする。ここで、終点はrであり、単調性のある関数fの実行結果が変わる切れ目を求める。
    def min_left(self,r,f):
        assert 0<=r and r<=self.n
        assert f(self.e)
        if r==0:
            return 0
        r+=self.size
        sm=self.e
        while(1):
            r-=1
            while(r>1 and (r%2)):
                r>>=1
            if not(f(self.op(self.d[r],sm))):
                while(r<self.size):
                    r=(2*r+1)
                    if f(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r& -r)==r:
                break
        return 0

    #内部処理用の関数なので使うことはあまりないかも
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])

    #print関数を使うことでデバッグすることができる
    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


#使用例
#add
G=segtree(LIST,(lambda x,y:x+y),0)

#addの書き方その2
def add(x,y):
    return x+y
G=segtree(LIST,add,0)


#times
G=segtree(LIST,(lambda x,y:x*y),1)

#min
G=segtree(LIST,min,INF)

#max
G=segtree(LIST,max,-INF)

#gcd
from math import gcd
G=segtree(LIST,gcd,0)

#lcm
from math import gcd
def lcm(x,y):
    return (x*y)//gcd(x,y)
G=segtree(LIST,lcm,1)

# xor
G=segtree(LIST,(lambda x,y:x^y),0)

# or
G=segtree(LIST,(lambda x,y:x|y),0)

# and
N=30
G=segtree(LIST,(lambda x,y:x&y),(1<<N)-1)
