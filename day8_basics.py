# List Examples & Methods
l = [12,7,45,1,2,4,6,1,1]
print(l)
l.append(7)  # add element at end
l.sort() # sort ascending
l.sort(reverse=True) # sort descending
l.reverse() # reverse list
print(l.index(1)) # first index of 1
print(l.count(1))
m = l.copy()
m[1]=100
l.insert(1, 899) # insert element at index 1
m= [900, 1000, 1100]
l.extend(m)   # add multiple elements
k = l+m
print(k)
print(l)
