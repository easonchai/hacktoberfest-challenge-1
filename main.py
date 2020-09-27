
def main_menu():
    print("=== SUNWAY TECH CLUB MANAGEMENT SOFTWARE ===")
    print("1. Create member")
    print("2. View member")
    print("3. Delete member")
    print("4. Exit")
    
    choice = int(input("Please choose an option: "))

    if choice == 4:
        print()
        print("Have a nice day!")

def main():
    main_menu()

if __name__ == "__main__":
    main()