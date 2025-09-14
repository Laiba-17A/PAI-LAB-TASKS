def add_std(data, name, marks):
    data[name] = marks

def update(data, name, marks):
    if name in data:
        data[name] = marks
    else:
        print("Student not found.")

def delete(data, name):
    if name in data:
        del data[name]
    else:
        print("Student not found.")

def topper(data):
    if not data:
        print("No students available.")
        return
    topper_name = ""
    topper_marks = -1

    for name in data:
        if data[name] > topper_marks:
            topper_marks = data[name]
            topper_name = name

    print("Topper is:", topper_name, "with", topper_marks, "marks")


students = {}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Find Topper")
    print("5. Show All Students")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        add_std(students, name, marks)

    elif choice == '2':
        name = input("Enter student name to update: ")
        marks = int(input("Enter new marks: "))
        update(students, name, marks)

    elif choice == '3':
        name = input("Enter student name to delete: ")
        delete(students, name)

    elif choice == '4':
        topper(students)

    elif choice == '5':
        if not students:
            print("No student data available.")
        else:
            for name in students:
                print(name, ":", students[name])

    elif choice == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter 1 to 6.")
