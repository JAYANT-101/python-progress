l =[1,23,4,5,6]
print(l)
l.append(7)
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(1))
# m=l in this any chane in m will change m
m=l.copy()
m[0]=0
print(l)
l.insert(1,33)
print(l)
m=[12,34,54]
k=l+m#make a nwe with both l and m
l.extend(m)
print(l)
print(l)