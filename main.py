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
    password = input("Enter your password (3-20 characters): ")
    if len(password) < 3 or len(password) > 20:
        print("Password must be between 3 and 20 characters.")
    else:
        print("Adding password...")
        with open("passwords.txt", "a") as file:
            file.write(f"{website},{username},{password}\n")
        print("Password saved successfully!")

elif choice == "2":
    print("Saved Passwords:\n")
    with open("passwords.txt", "r") as file:
        for line in file:
            line = line.strip()
            website, username, password = line.split(",")
            print(f"Website : {website}")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print("_________________________")

elif choice == "3":
    print("You chose to search for a password.")
    websiteinp = input("Enter the website you want to search for: ").lower()
    found = False
    with open("passwords.txt", "r") as file:
        for line in file:
            line = line.strip()
            website, username, password = line.split(",")
            if websiteinp == website.lower():
                found = True
                print("Password found!:")
                print(f"Website : {website}")
                print(f"Username: {username}")
                print(f"Password: {password}")
                print("_________________________")
    if not found:
        print("No password found for the specified website.")

elif choice == "4":
    print("Exiting the program.")

else:
    print("Invalid choice. Please select a valid option.")