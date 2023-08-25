#https://stnkien.hatenablog.com/entry/avl-tree

class Node:
    """ノード

    Attributes:
        key (any): ノードのキー。比較可能なものであれば良い。(1, 4)などタプルも可。
        val (any): ノードの値。
        lch (Node): 左の子ノード。
        rch (Node): 右の子ノード。
        bias (int): 平衡度。(左部分木の高さ)-(右部分木の高さ)。
        size (int): 自分を根とする部分木の大きさ

    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.lch = None
        self.rch = None
        self.bias = 0
        self.size = 1


class AVLTree:
    """非再帰AVL木

    Attributes:
        root (Node): 根ノード。初期値はNone。

    """

    def __init__(self):
        self.root = None

    def rotate_left(self, v):
        u = v.rch
        u.size = v.size
        v.size -= u.rch.size + 1 if u.rch is not None else 1
        v.rch = u.lch
        u.lch = v
        if u.bias == -1:
            u.bias = v.bias = 0
        else:
            u.bias = 1
            v.bias = -1
        return u

    def rotate_right(self, v):
        u = v.lch
        u.size = v.size
        v.size -= u.lch.size + 1 if u.lch is not None else 1
        v.lch = u.rch
        u.rch = v
        if u.bias == 1:
            u.bias = v.bias = 0
        else:
            u.bias = -1
            v.bias = 1
        return u

    def rotateLR(self, v):
        u = v.lch
        t = u.rch
        t.size = v.size
        v.size -= u.size - (t.rch.size if t.rch is not None else 0)
        u.size -= t.rch.size + 1 if t.rch is not None else 1
        u.rch = t.lch
        t.lch = u
        v.lch = t.rch
        t.rch = v
        self.update_bias_double(t)
        return t

    def rotateRL(self, v):
        u = v.rch
        t = u.lch
        t.size = v.size
        v.size -= u.size - (t.lch.size if t.lch is not None else 0)
        u.size -= t.lch.size + 1 if t.lch is not None else 1
        u.lch = t.rch
        t.rch = u
        v.rch = t.lch
        t.lch = v
        self.update_bias_double(t)
        return t

    def update_bias_double(self, v):
        if v.bias == 1:
            v.rch.bias = -1
            v.lch.bias = 0
        elif v.bias == -1:
            v.rch.bias = 0
            v.lch.bias = 1
        else:
            v.rch.bias = 0
            v.lch.bias = 0
        v.bias = 0

    def insert(self, key, val):
        """挿入

        指定したkeyに値valを挿入する。
        その後、平衡を保つように回転を行う。

        Args:
            key (any): キー。
            val (any): 値。

        Note:
            同じキーがあった場合に上書きする。

        """
        if self.root is None:
            self.root = Node(key, val)
            return

        v = self.root
        history = []
        while v is not None:
            if key < v.key:
                history.append((v, 1))
                v = v.lch
            elif v.key < key:
                history.append((v, -1))
                v = v.rch
            elif v.key == key:
                v.val = val
                return

        p, pdir = history[-1]
        if pdir == 1:
            p.lch = Node(key, val)
        else:
            p.rch = Node(key, val)

        while history:
            v, direction = history.pop()
            v.bias += direction
            v.size += 1

            new_v = None
            b = v.bias
            if b == 0:
                break

            if b == 2:
                u = v.lch
                if u.bias == -1:
                    new_v = self.rotateLR(v)
                else:
                    new_v = self.rotate_right(v)
                break
            if b == -2:
                u = v.rch
                if u.bias == 1:
                    new_v = self.rotateRL(v)
                else:
                    new_v = self.rotate_left(v)
                break

        if new_v is not None:
            if len(history) == 0:
                self.root = new_v
                return
            p, pdir = history.pop()
            p.size += 1
            if pdir == 1:
                p.lch = new_v
            else:
                p.rch = new_v

        while history:
            p, pdir = history.pop()
            p.size += 1

    def delete(self, key):
        """削除

        指定したkeyの要素を削除する。
        その後、平衡を保つように回転を行う。

        Args:
            key (any): キー。

        Return:
            bool: 指定したキーが存在するならTrue、しないならFalse。

        """
        v = self.root
        history = []
        while v is not None:
            if key < v.key:
                history.append((v, 1))
                v = v.lch
            elif v.key < key:
                history.append((v, -1))
                v = v.rch
            else:
                break
        else:
            return False

        if v.lch is not None:
            history.append((v, 1))
            lmax = v.lch
            while lmax.rch is not None:
                history.append((lmax, -1))
                lmax = lmax.rch

            v.key = lmax.key
            v.val = lmax.val

            v = lmax

        c = v.rch if v.lch is None else v.lch

        if history:
            p, pdir = history[-1]
            if pdir == 1:
                p.lch = c
            else:
                p.rch = c
        else:
            self.root = c
            return True

        while history:
            new_p = None

            p, pdir = history.pop()
            p.bias -= pdir
            p.size -= 1

            b = p.bias
            if b == 2:
                if p.lch.bias == -1:
                    new_p = self.rotateLR(p)
                else:
                    new_p = self.rotate_right(p)

            elif b == -2:
                if p.rch.bias == 1:
                    new_p = self.rotateRL(p)
                else:
                    new_p = self.rotate_left(p)

            elif b != 0:
                break

            if new_p is not None:
                if len(history) == 0:
                    self.root = new_p
                    return True
                gp, gpdir = history[-1]
                if gpdir == 1:
                    gp.lch = new_p
                else:
                    gp.rch = new_p
                if new_p.bias != 0:
                    break

        while history:
            p, pdir = history.pop()
            p.size -= 1

        return True

    def member(self, key):
        """キーの存在チェック

        指定したkeyがあるかどうか判定する。

        Args:
            key (any): キー。

        Return:
            bool: 指定したキーが存在するならTrue、しないならFalse。

        """
        v = self.root
        while v is not None:
            if key < v.key:
                v = v.lch
            elif v.key < key:
                v = v.rch
            else:
                return True
        return False

    def get(self, key):
        """値の取り出し

        指定したkeyの値を返す。
        keyが存在しない場合はNoneを返す。

        Args:
            key (any): キー。

        Return:
            any: 指定したキーが存在するならその値、存在しないならNone。

        """
        v = self.root
        while v is not None:
            if key < v.key:
                v = v.lch
            elif v.key < key:
                v = v.rch
            else:
                return v.val
        return None

    def lower_bound(self, key):
        """下限つき探索

        指定したkey以上で最小のキーを見つける。

        Args:
            key (any): キーの下限。

        Return:
            any: 条件を満たすようなキー。そのようなキーが一つも存在しないならNone。

        """
        #ret = float('inf')
        ret = None
        v = self.root
        while v is not None:
            if v.key >= key:
                if ret is None or ret > v.key:
                    ret = v.key
                v = v.lch
            else:
                v = v.rch
        return ret

    def upper_bound(self, key):
        """上限つき探索

        指定したkey未満で最大のキーを見つける。

        Args:
            key (any): キーの上限。

        Return:
            any: 条件を満たすようなキー。そのようなキーが一つも存在しないならNone。

        """
        #ret = -float('inf')
        ret = None
        v = self.root
        while v is not None:
            if v.key < key:
                if ret is None or ret < v.key:
                    ret = v.key
                v = v.rch
            else:
                v = v.lch
        return ret

    def find_kth_element(self, k):
        """小さい方からk番目の要素を見つける

        Args:
            k (int): 何番目の要素か(0オリジン)。
        """
        v = self.root
        s = 0
        while v is not None:
            t = s+v.lch.size if v.lch is not None else s
            if t == k:
                return v.key
            elif t < k:
                s = t+1
                v = v.rch
            else:
                v = v.lch
        return None

    def __contains__(self, key): return self.member(key)
    def __getitem__(self, key): return self.get(key)
    def __setitem__(self, key, val): return self.insert(key, val)
    def __delitem__(self, key): return self.delete(key)
    def __bool__(self): return self.root is not None
    def __len__(self): return self.root.size if self.root is not None else 0
