from encryption import encrypt_password, decrypt_password
from storage import save_data, load_data
from auth import login, set_master_password

if not login():
    exit()

data = load_data()

while True:
    print("\n1. Add Password")
    print("2. View Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        site = input("Enter site/app name: ")
        username = input("Enter username/email: ")
        password = input("Enter password: ")

        encrypted = encrypt_password(password)
        data[site] = {"username": username, "password": encrypted}
        save_data(data)
        print(f"Password for '{site}' saved successfully!")

    elif choice == "2":
        site = input("Enter site/app name to view: ")
        if site in data:
            decrypted = decrypt_password(data[site]["password"])
            print(f"Username: {data[site]['username']}")
            print(f"Password: {decrypted}")
        else:
            print(f"No data found for '{site}'")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again!")