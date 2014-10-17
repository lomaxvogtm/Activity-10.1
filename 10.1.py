__author__ = 'Madeleine'

m = [2, 4, 6, 8]

#1
print(m[2])

#2
fivem = []
for number in m:
    fivem.append(number*5)
print(fivem)

#3
m.append(10)
print(m)

#4
m.append(6)
print(m)

#5
print(m.index(8))

#6
m.remove(8)
print(m)
