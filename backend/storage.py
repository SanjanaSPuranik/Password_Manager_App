import json
import os

FILE = "passwords.json"

def load_data():

    if os.path.exists(FILE):

        with open(FILE, "r") as f:
            return json.load(f)

    return {}

def save_data(data):

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def save_password(site, username, password):

    data = load_data()

    # CHECK DUPLICATE
    if site in data:
        return False

    data[site] = {
        "username": username,
        "password": password
    }

    save_data(data)

    return True

def get_password(site):

    data = load_data()

    if site in data:
        return data[site]["username"], data[site]["password"]

    return None

def delete_password(site):

    data = load_data()

    if site in data:

        del data[site]

        save_data(data)

        return True

    return False