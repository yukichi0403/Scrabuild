from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] 
def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


# itertools groupby
'''
import itertools
l = [0, 0, 0, 1, 1, 2, 0, 0]
print([(k, list(g)) for k, g in itertools.groupby(l)])
'''
# [(0, [0, 0, 0]), (1, [1, 1]), (2, [2]), (0, [0, 0])]


