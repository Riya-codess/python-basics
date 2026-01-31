def add(a, b):
    print("sum: ", a+b)


def greet(name = "students"):
    print("hello,", name)


def student_info(name,age,course):
    print("name: ", name)
    print("age: ", age)
    print("course: ", course)

# Calling functions
add(4,5)

greet()
greet("riya")

student_info("riya","19","btech")
