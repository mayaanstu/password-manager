from getpass import getpass
master_password = "" 
while True and master_password == "":
    print("_________________________")
    print("    PASSWORD MANAGER")
    print("_________________________")

    print("1. Add Password")
    print("2. View All Passwords")
    print("3. Search For Password")
    print("4. Delete a Website Entry")
    print("5. Change Password")
    print("6. Generate Password")
    print("7. Change Master Password")
    print("8. Exit The Program")

    def add_password():
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


    def view_passwords():
        print("You chose to view saved passwords.")
        print("Saved Passwords:\n")
        with open("passwords.txt", "r") as file:
            for line in file:
                line = line.strip()
                website, username, password = line.split(",")
                print(f"Website : {website}")
                print(f"Username: {username}")
                print(f"Password: {password}")
                print("_________________________")


    def search_password():
        print("You chose to search for a password.")
        website_to_search = input("Enter the website you want to search for: ").lower()
        found = False
        with open("passwords.txt", "r") as file:
            for line in file:
                line = line.strip()
                website, username, password = line.split(",")
                if website_to_search == website.lower():
                    found = True
                    print("Password found!")
                    print(f"Website : {website}")
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                    print("_________________________")
            if not found:
                print("No password found for the specified website.")


    def delete_password():
        print("You chose to delete a website entry.")
        website_to_delete = input("Enter the website entry you want to delete: ").lower()
        found = False
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
        with open("passwords.txt", "w") as file:
            for line in lines:
                line = line.strip()
                website, username, password = line.split(",")
                if website_to_delete != website.lower():
                    file.write(line + "\n")
                else:
                    found = True
                    print(f"Website entry for {website} deleted successfully.")
        if not found:
            print("No website entry found for the specified website.")


    def change_password():
        print("You chose to change a password.")
        website_to_change = input("Enter the website for which you want to change the password: ").lower()
        found = False
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
        with open("passwords.txt", "w") as file:
            for line in lines:
                line = line.strip()
                website, username, password = line.split(",")
                if website_to_change == website.lower():
                    found = True
                    new_password = getpass("Enter the new password (3-20 characters): ")
                    if len(new_password) < 3 or len(new_password) > 20:
                        print("Password must be between 3 and 20 characters.")
                        file.write(line + "\n")  
                    else:
                        file.write(f"{website},{username},{new_password}\n")
                        print(f"Password for {website} changed successfully.")
                else:
                    file.write(line + "\n")
        if not found:
            print("No website entry found for the specified website.")

    def generate_password():
        print("You chose to generate a password.")
        import random
        import string

        length = int(input("Enter the desired password length (3-20): "))
        if length < 3 or length > 20:
            print("Password length must be between 3 and 20 characters.")
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            print("Generated password:", password)
    

    def change_master_password():
                print("You chose to change/add the master password.")
                if master_password == "":
                    new_master_password = getpass("Enter the new master password (3-20 characters): ")
                    if len(new_master_password) < 3 or len(new_master_password) > 20:
                        print("Master password must be between 3 and 20 characters.")
                    else:
                        global master_password
                        master_password = new_master_password
                        print("Master password set successfully.")
                else:
                    current_master_password = getpass("Enter the current master password: ")
                    new_master_password = getpass("Enter the new master password (3-20 characters): ")
                    if len(new_master_password) < 3 or len(new_master_password) > 20:
                        print("Master password must be between 3 and 20 characters.")
                    else:
                        global master_password
                        master_password = new_master_password
                        print("Master password changed successfully.")    


    choice = input("\nChoose an option (1-7): ")
    print("You chose:", choice)

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        search_password()

    elif choice == "4":
        delete_password()
    
    elif choice == "5":
        change_password()
    
    elif choice == "6":
        generate_password()

    elif choice == "7":
        change_master_password()

    elif choice == "8":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please select a valid option.")

