# List to store all student records
students = []
def add_student():
    # Taking input from user
    roll = int(input("enter roll num: "))
    name = input("enter name: ")
    marks = (input("enter marks: "))

    student ={
    "roll": roll,
    "name": name,
    "marks": marks
}
  # Adding student to the list
    students.append(student)
    print("student added successfully \n")

def view_student():
    if len(students) ==0:
        print("no student found/n")
    else:
        print("student list: ")
        for i in students:
            print("roll: ", i["roll"], "| name: ", i["name"], "|marks :", i["marks"])
        print()


def search_student():
    roll = int(input("enter roll num : "))
    found = False

    # Looping through student list
    for i in students: 
        if i["roll"] == roll: 
            print("student found ")
            print ("name: ", i["name"])
            print ("marks: " , i["marks"], "\n")
            found = True
            break
    if not found:
        print("student not found\n")

print(students)

def delete_student():
    roll = int(input("enter roll num: "))

    for i in students:
        if i["roll"] == roll:
            students.remove(i)
            print("student deleted successfully\n")
            return
    print("student not found\n")


while True:
    print("STUDENT MANAGEMENT SYSTEM")
    print("1. add student")
    print("2. view student")
    print("3. search student")
    print("4. delete student")
    print("5. exit")

    choice = input("enter your choice: ")

    if choice =='1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice =='5':
        print("exiting program")
        break
    else:
        print("invalid choice \n")
