from calculator import Calculator

def display_menu():
    print("Welcome to the Calculator App!")
    print("------------------------------")
    print("1.) Use Simple Calculator")
    print("2.) Exit")

def main():
    display_menu()
    while True:
        choice = int(input("Enter a menu option: "))
        if choice == 1:
            Calculator.menu()
            Calculator.choice()
        elif choice == 2:
            print("Exiting program...")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()