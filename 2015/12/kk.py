import sys
import json

l = sys.stdin.readline()
tree = json.loads(l)

def val(t):
    if type(t) == unicode :
        return 0
    if type(t) == int :
        return t
    if type(t) == list :
        s = 0
        for l in t:
            s += val(l)
        return s
    if type(t) == dict :
        s = 0
        for i in t:
            if t[i] == u'red':
                return 0
            s += val(t[i])
        return s
    print type(t)
    print t

print val(tree)
