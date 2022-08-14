import random
import sys

applications = {}


def main():
    random.seed()
    print("##################################################################################")
    print("###########################  Secure Password Manager   ###########################")
    print("##################################################################################")
    print()

    while True:
        print("----------------------------------------------------------------------------------")
        print("1. Display all your passwords.")
        print("2. Create new entry.")
        #print("3. View Statistics TODO")
        #print("4. Wipe entry TODO")
        print("3. Exit")
        print("----------------------------------------------------------------------------------")
        print()
        action = int(input("What would you like to do? "))
        print()

        match action:
            case 1:
                # display_passwords()
                for app, info in applications.items():
                    print(
                        f'{app}: username: {info["username"]} password: {info["password"]}')
            case 2:
                create_new_passwd()
            case 3:
                sys.exit()


def display_passwords():
    for app, info in applications.items():
        print(
            f'{app}: username: {info["username"]} password: {info["password"]}')


def create_new_passwd():
    appName = input(
        "What is the name of the application for which your are creating this password?")
    print()

    specs = get_passwd_specifications()
    print()
    print_specs(specs)
    print()

    if input("Would you like to specify a username for this password?[y/n]").lower() == "y":
        userName = input("Enter username: ")
    else:
        userName = ""

    passwd = generate_random_password(specs)

    applications[appName] = {"username": userName, "password": passwd}


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


if __name__ == '__main__':
    main()
