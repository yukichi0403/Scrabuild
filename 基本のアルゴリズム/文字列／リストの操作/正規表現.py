#pythonの正規表現をチェックするサイト：https://pythex.org/
#正規表現まとめ：https://data-analysis-stats.jp/python/python%E3%81%A7%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE/

import re

s = input()
ans = re.match('^AAA.*$', s)
if ans:
    print('Yes')
else:
    print('No')
