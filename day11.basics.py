cities = {"tokyo", "madrid", "berlin", "delhi"}
print("org: ", cities)

cities.add("roorkee")
print("after add:", cities)

cities.remove("tokyo")
print("after removal: ", cities)

cities.discard("paris")
print("after discrad:", cities)

cities.pop()
print("after pop: ", cities)

print("length :", len(cities))
