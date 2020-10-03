import random
import os

database = []

def print_divider():
    print("+----+" + "-" *20 + "+-----+" + "-" * 25 + "+")

def create():
    global database

    name = input("Enter name of student: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    newId = len(database)+1
    database.append([newId,name, age])
    print("Student added!")

    #add it into a text file as well
    #check if the file exsists
    if os.path.isfile('Users.text')==False:
        f= open("Users.txt","w+")
        for i in range(len(database)):
            f.write("The name is: ")
            f.write(name)
            f.write("\n")
            f.write("The name is: ")            
            f.write(email)
            f.write("\n")
            f.write("*"*10)
        f.close()
    else:
        f=open("Users.txt","a+")
        for i in range(len(database)):
            f.write("The name is: ")
            f.write(name)
            f.write("\n")
            f.write("The email is: ")
            f.write(email)
            f.write("\n")
            f.write("*"*10)
        f.close()
        print("Information Captured")
def view():
    print("=== View Students ===")
    print_divider()
    print("| ID |        NAME        | AGE |          EMAIL          |")
    print_divider()
    if os.path.isfile('Users.text')==False:
        f=open("Users.txt","r")
    for row in database:
        userId = str(row[0])
        chance = random.randint(0, 100)
        if chance >= 70:
            userId = str(random.randint(1, 100))

        name = row[1]
        age = int(row[2])
        email = row[3]

        print("|", end="")
        print(userId.center(3), "|", end="")
        print(name.center(19), "|", end="")
        print(age.center(4), "|", end="")
        print(email.center(24), "|")
        print_divider()

def edit():
    view()
    print()
    userInput = input("Enter the id of the student you want to edit: ")
    global database

    name = input("Enter name of student: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")
    
    database[userInput-1] = [userInput, name, age, email]

    print("Student successfully edited!")

def delete():
    view()
    print()
    userInput = int(input("Please Enter the ID of the student you want to delete: "))

    global database
    database.remove(userInput-1)

    print("Student removed!")

def print_error():
    print("Invalid choice!")

def main_menu():
    while True:
        print()
        print("=== SUNWAY TECH CLUB MANAGEMENT SOFTWARE ===")
        print("1. Create member")
        print("2. View member")
        print("3. Edit member")
        print("4. Delete member")
        print("5. Exit")
        
        choice = int(input("Please choose an option: "))
        if choice>5:
            print("Invalid option")
        if choice == 5:
            print()
            print("Have a nice day!Goodbye")
            break

        switcher = {
            1: create,
            2: view,
            3: edit,
            4: delete,
        }

        func = switcher.get(choice, print_error)
        print("\n")
        func()

def main():
    main_menu()

if __name__ == "__main__":
    main()