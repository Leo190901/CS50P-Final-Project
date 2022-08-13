import random

passwords = {}


def main():
    random.seed()
    print("####################################")
    print("###  Secure Password Manager   ###")
    print("####################################")
    print()

    create_new_passwd()


def create_new_passwd():
    specs = get_passwd_specifications()
    # print(specs)


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

    return specs


main()
