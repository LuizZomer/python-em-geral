from itertools import count

c1 = count(step=8,start=10)
# c1 = count(8,8)

print('c1', hasattr(c1,'__iter__'))

for i in c1:
    if i >= 100:
        break
    print(i)