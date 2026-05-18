import hashlib
import os

PASS_FILE = "master.hash"

def set_master_password():
    password = input("Set your master password: ")
    hashed = hashlib.sha256(password.encode()).hexdigest()
    with open(PASS_FILE, "w") as f:
        f.write(hashed)
    print("Master password set successfully!")

def login():
    if not os.path.exists(PASS_FILE):
        print("No master password found. Please set it first.")
        set_master_password()

    hashed_correct = open(PASS_FILE, "r").read()
    password = input("Enter master password: ")
    hashed_input = hashlib.sha256(password.encode()).hexdigest()

    if hashed_input == hashed_correct:
        print("Login successful!")
        return True
    else:
        print("Access Denied!")
        return False