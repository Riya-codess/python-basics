name = "riya choudhary"
friend = "sneha"

#slicing

print("hello, " + name)

print(name[0])
print(name[1])
print(name[2])
print(name[3])

print("lets use a for loop here \n")
for character in name:
    print(character)

print(name[0:8])
print(name[:-3])
print(name[8:])
print(name[-2:])
print(name[-4:-2])

#string methods

a = "riya !!!! !!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("riya", "sneha"))
print(a.split(" "))
print(a.startswith("ri"))
print(a.endswith("!!"))
