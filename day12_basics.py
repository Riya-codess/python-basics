# Creating a dictionary to store student details
students = {
    "name": "riya choudhary",
    "age": 19,
    "branch": "cse"
}

# Updating existing value
students["age"]= 20
students["college"] = "abc college"

# Accessing values using dictionary methods
print(students.get("branch"))
print(students.keys())
print(students.values())
print(students.items())
print (students)
