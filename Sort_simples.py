# -*- coding: utf-8 -*-

x = list(map(int, input().split(" ")))

t = []
for y in x:
    t.append(y)

x.sort()

for y in x:
    print(y)
print()

for u in t:
    print(u)
