# A good C++ version using unordered_multiset
# https://github.com/kdungs/codecon/blob/master/src/gloves.cc
import sys
import collections

def matching_gloves(arr):
    res = 0
    d = dict()
    for a in arr:
        u = a[::-1]
        if a == u:
            continue
        if u in d:
            d[u]-=1
            if d[u] == 0:
                d.pop(u)
            res += 1
        else:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
    if len(d)==0:
        return res
    else:
        return -1

def matching_gloves1(arr):
    res = 0
    d = collections.defaultdict(int)
    for a in arr:
        u = a[::-1]
        if a == u:
            continue
        if u in d:
            d[u]-=1
            if d[u] == 0:
                d.pop(u)
            res += 1
        else:
            d[a]+=1
    if len(d)==0:
        return res
    else:
        return -1


# data = sys.stdin.read().splitlines()
# sz = None
# arr = []
# for line in data :
#     if not sz:
#         sz = int(line)
#     else:
#         arr.append(line)

arr = ['bcd', 'erty', 'ytre', 'opipo', 'dcb']
# arr = ['abcde', 'edcba', 'abcde']
# arr = ['ioi', 'ertre', 'ghhg']
print(matching_gloves1(arr))