# Nested If-Else
marks = int(input("enter yoiur marks: "))

if marks >= 0:
    if marks >= 90:
        print("grade = A+")
    elif marks >=80:
        print("grade = A")
    elif marks >=60:
        print("grade = B")
    elif marks >= 40:
        print("grade = C")
    else:
        print("FAIL")


#match statement:-

choice = int(input("enter a num(1-4): "))
match choice:
    case 1:
        print("selected c++ ")
    case 2:
        print("selected java ")
    case 3:
        print("selected python ")
    case 4: 
        print("selected html ")
    case _: #used for default
        print("invalid choice ")
