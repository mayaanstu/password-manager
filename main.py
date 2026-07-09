print("_________________________")
print("    PASSWORD MANAGER")
print("_________________________")

print("1. Add Password")
print("2. View Passwords")
print("3. Search")
print("4. Exit")
choice = input("\nChoose an option (1-4): ")
print("You chose:", choice)
if choice == "1":
    print("You chose to add a password.")
    website = input("Website: ")
    username = input("Username: ") 
    password = input("\nEnter your password (3-20 characters): ")
    if len(password) < 3 or len(password) > 20:
        print("Password must be between 3 and 20 characters.")
        repeat_password = input("Please re-enter your password: ")
        if password != repeat_password:
            print("Passwords do not match. Please try again.")
            password = input("Enter your password (3-20 characters): ") 
    else:
        print("Adding password...")
    with open("passwords.txt", "a") as file:
        file.write(f"{website},{username},{password}\n")

    print("Password saved successfully!")
elif choice == "2":
    print("You chose to view passwords.")
elif choice == "3":
    print("You chose to search for a password.")
elif choice == "4":
    print("Exiting the program.")
else:
    print("Invalid choice. Please select a valid option.")
