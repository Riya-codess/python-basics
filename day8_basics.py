l = [12,7,45,1,2,4,6,1,1]
print(l)
l.append(7)
l.sort()
l.sort(reverse=True)
l.reverse()
print(l.index(1))
print(l.count(1))
m = l.copy()
m[1]=100
l.insert(1, 899)
m= [900, 1000, 1100]
l.extend(m)
k = l+m
print(k)
print(l)
