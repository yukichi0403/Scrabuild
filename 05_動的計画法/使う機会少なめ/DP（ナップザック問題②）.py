#動的計画法（ナップザック問題②）
n,s = map(int,input().split())
A = list(map(int,input().split()))

#初期化
dp = [['No'] * (s + 1) for _ in range(n + 1)]
#初期化の続き。0個の重りを使い0gの重さを表現することは可能なので'Yes'
dp[0][0] = 'Yes'

for i in range(n):
    for j in range(s + 1):
        if j >= A[i]:
            #真上か斜め上のどちらかが'Yes'だったら'Yes
            if dp[i][j] == 'Yes' or dp[i][j - A[i]] == 'Yes':
                dp[i + 1][j] = 'Yes'
        #こちらは自動的に真上の答えをそのまま持ってくるしかない
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[n][s])
