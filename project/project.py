import random

applications = {}


def main():
    random.seed()
    print("##################################################")
    print("###########  Secure Password Manager   ###########")
    print("##################################################")
    print()

    create_new_passwd()


def create_new_passwd():
    appName = input(
        "What is the name of the application for which your are creating this password?")
    print()

    specs = get_passwd_specifications()
    print()
    print_specs(specs)

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
    pass


main()
