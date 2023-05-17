s1 = set()
s1.add('Luiz')
s1.add(1)

print(s1)

s1.update(('Zomito',1,2))
print(s1)
# s1.clear()
s1.discard('Zomito')
print(s1)