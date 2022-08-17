import random
import sys
import csv
import os
from tabulate import tabulate
from cryptography.fernet import Fernet

applications = {}
rows = []


def main():
    random.seed()
    if not os.path.exists("secret.key") or os.stat("secret.key").st_size == 0:
        generate_key()
    else:
        pass
    global key
    key = load_key()
    global f
    f = Fernet(key)
    try:
        load_passwords()
    except:
        pass
    display_start_screen()
    while True:
        display_options()
        action = int(input("What would you like to do? "))
        print()
        match action:
            case 1:
                display_passwords()
            case 2:
                create_new_passwd()
            case 3:
                wipe()
            case 4:
                sys.exit()


def display_start_screen():
    print("##################################################################################")
    print("###############################  Password Manager   ##############################")
    print("##################################################################################")
    print()


def display_options():
    print("----------------------------------------------------------------------------------")
    print("1. Display all your passwords.")
    print("2. Create new entry.")
    print("3. Wipe all entries")
    print("4. Exit")
    print("----------------------------------------------------------------------------------")
    print()


def load_passwords():
    with open('passwords.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            applications[row[0]] = {"username": row[1],
                                    "password": row[2]}
            tmp = row[2].encode()
            pwE = f.decrypt(tmp)
            pw = pwE.decode()
            applications[row[0]]["password"] = pw


def decrypt_passwords():
    for row in rows:
        tmp = row[2].encode()
        pw = f.decrypt(tmp)
        print(pw)


def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()


def display_passwords():
    col_names = ["App", "Username", "Password"]
    values = [[name, *inner.values()] for name, inner in applications.items()]
    print(tabulate(values, headers=col_names, tablefmt="grid", showindex="always"))


def create_new_passwd():
    appName = input(
        "What is the name of the application for which your are creating this password?")
    print()

    if input("Would you like to enter a password manually?[y/n] ").lower() == "y":
        passwd = input("Enter Password: ")
    else:
        specs = get_passwd_specifications()
        print()
        print_specs(specs)
        print()
        passwd = generate_random_password(specs)

    if input("Would you like to specify a username for this password?[y/n]").lower() == "y":
        userName = input("Enter username: ")
    else:
        userName = ""

    encodedPW = passwd.encode()
    enryptedPasswd = f.encrypt(encodedPW).decode()

    pw = f.decrypt(enryptedPasswd.encode())
    print(pw)

    applications[appName] = {"username": userName, "password": passwd}
    values = [appName, userName, enryptedPasswd]
    with open('passwords.csv', 'a',  newline='\n', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(values)


def get_passwd_specifications():
    specs = {}
    if input("Do you want your Password to contain numbers?[y/n] ").lower() == "y":
        specs["num"] = True
    else:
        specs["num"] = False
    if input("Do you want your Password to contain lowercase letters?[y/n] ").lower() == "y":
        specs["lower"] = True
    else:
        specs["lower"] = False
    if input("Do you want your Password to contain uppercase letters?[y/n] ").lower() == "y":
        specs["upper"] = True
    else:
        specs["upper"] = False
    if input("Do you want your Password to contain special characters?[y/n] ").lower() == "y":
        specs["special"] = True
    else:
        specs["special"] = False

    while True:
        len = int(input(
            "What length should your password have (maximal length is 100 characters)? "))
        try:
            if len < 1 or len > 100:
                print("Invalid length!")
            else:
                specs["len"] = len
                break
        except:
            print("Please enter a number!")

    return specs


def print_specs(specs):
    print("These are your chosen specifications:")
    print(f'Lowercase letters: {specs["lower"]}')
    print(f'Uppercase letters: {specs["upper"]}')
    print(f'Numbers: {specs["num"]}')
    print(f'Special Characters: {specs["special"]}')
    print(f'Length: {specs["len"]}')


def generate_random_password(specs):
    upperLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowerLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    specials = ["#", "!", "&", "$", "?", "§", "%", "/", "(", ")", "="]

    apply = []
    if specs["lower"]:
        apply.append(lowerLetters)
    if specs["upper"]:
        apply.append(upperLetters)
    if specs["num"]:
        apply.append(numbers)
    if specs["special"]:
        apply.append(specials)

    passwd = ""
    for _ in range(specs["len"]):
        typeChoice = random.choice(apply)
        c = random.choice(typeChoice)
        passwd = passwd + str(c)

    return passwd


def wipe():
    with open('passwords.csv', 'w',  newline='\n', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow('')
    applications.clear()


if __name__ == '__main__':
    main()
