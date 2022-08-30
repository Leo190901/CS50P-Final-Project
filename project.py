import random
import sys
import csv
import os
from tabulate import tabulate
from cryptography.fernet import Fernet

applications = {}


def main():
    random.seed()

    if not os.path.exists("secret.key") or os.stat("secret.key").st_size == 0:
        generate_key()
    else:
        pass

    while True:
        display_start_screen()
        display_options()
        action = input("What would you like to do? ")
        print()
        match action:
            case '1':
                clear_view()
                load_passwords()
                clear_view()
            case '2':
                clear_view()
                display_passwords()
                while True:
                    if input("Press [q] to exit view.") == 'q':
                        clear_view()
                        break
                    else:
                        clear_view()
                        display_passwords()
                        pass
            case '3':
                clear_view()
                create_new_passwd()
                clear_view()
            case '4':
                clear_view()
                wipe()
                clear_view()
            case 'q':
                clear_view()
                sys.exit()
            case other:
                print("Invalid selection.")
                print()
                clear_view()


def clear_view():
    os.system('clear')
    os.system('cls')


def display_start_screen():
    print("##################################################################################")
    print("###############################  Password Manager   ##############################")
    print("##################################################################################")
    print()


def display_options():
    print("----------------------------------------------------------------------------------")
    print("[1] Load passwords from csv file")
    print("[2] Display all your passwords.")
    print("[3] Create new entry.")
    print("[4] Wipe all entries")
    print("[q] Exit")
    print("----------------------------------------------------------------------------------")
    print()


def load_passwords(fileName=""):
    key = load_key()
    f = Fernet(key)

    if fileName == "":
        print()
        fileName = input(
            "What is the name of the file in which your passwords are stored? ")
    i = 0
    try:
        with open(fileName) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                applications[row[0]] = {"username": row[1],
                                        "password": row[2]}
                tmp = row[2].encode()
                pwE = f.decrypt(tmp)
                pw = pwE.decode()
                applications[row[0]]["password"] = pw
                i += 1
            if i == 1:
                print(f"Loaded {i} entry.")
            else:
                print(f"Loaded {i} entries.")
    except:
        print("Error: Could not load passwords.")

    return applications


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def display_passwords():
    try:
        col_names = ["App", "Username", "Password"]
        values = [[name, *inner.values()]
                  for name, inner in applications.items()]
        print(tabulate(values, headers=col_names,
              tablefmt="grid", showindex="always"))
    except:
        print("Error: Unable to display passwords")


def create_new_passwd(appName="", passwd="", userName="", fileName=""):
    if appName == "":
        appName = input(
            "What is the name of the application for which your are creating this password?")
        print()

    if passwd == "":
        if input("Would you like to enter a password manually?[y/n] ").lower() == "y":
            passwd = input("Enter Password: ")
        else:
            specs = get_passwd_specifications()
            print()
            print_specs(specs)
            print()
            passwd = generate_random_password(specs)

    if userName == "":
        if input("Would you like to specify a username for this password?[y/n]").lower() == "y":
            userName = input("Enter username: ")
        else:
            userName = ""

    key = load_key()
    f = Fernet(key)

    try:
        encodedPW = passwd.encode()
        enryptedPasswd = f.encrypt(encodedPW).decode()
    except:
        print("Error: Could not encrypt password")

    try:
        if fileName == "":
            print()
            fileName = input("Specify name of password file: ")

        applications[appName] = {"username": userName, "password": passwd}
        values = [appName, userName, enryptedPasswd]
        with open(fileName, 'a',  newline='\n', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(values)
    except:
        print("Error: Could not store password in specified file")


def get_passwd_specifications(answers):
    specs = {}

    if not answers:
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
    else:
        if list(answers)[0] == "y":
            specs["num"] = True
        else:
            specs["num"] = False
        if list(answers)[1] == "y":
            specs["lower"] = True
        else:
            specs["lower"] = False
        if list(answers)[2] == "y":
            specs["upper"] = True
        else:
            specs["upper"] = False
        if list(answers)[3] == "y":
            specs["special"] = True
        else:
            specs["special"] = False

    while True:
        if not answers:
            len = int(input(
                "What length should your password have (maximal length is 100 characters)? "))
        else:
            len = answers[4]
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


def wipe(fileName="", ans=""):
    if fileName == "":
        fileName = input("What is the name of the file that you want to wipe?")

    with open(fileName, 'w',  newline='\n', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow('')
    applications.clear()

    if ans == "":
        ans = input("Dou you also want to delete the file?[y/n] ")

    if ans == "y":
        os.remove(fileName)

    return applications


if __name__ == '__main__':
    main()
