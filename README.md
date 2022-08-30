# Command Line Password Manager

## Video Demo

## Description

    For my Final Project I decided to make a password manager.
    It enables you to store passwords that you can generate in the manager in a csv file.
    You can also manually type in passwords and store them in a csv file.
    Those passwords can then be displayed in a tabular format.
    The application also allows you to wipe all of the passwords.
    In the csv file the passwords are encrypted and are only decrypted when they are loaded into the password manager. The encryption and decryption are accomplished by simple symmetric cryptography, the key for this is stored in a secret.key file. The security of the password manager relies on this file being stored at a secure place and only being used when passwords need to be encrypted or decrypted.

## Explanation of each function

### main()

    The main function first checks if a secret.key file is available, if not a new key is generated. After that the start screen and the available options for the user are displayed. Depending on which option the user chooses different functions are called. In case of a invalid selection the user will be told that their selection was invalid and will be prompted to choose again.

### display_start_screen()

    A pretty trivial function. It simply displays the start screen which looks like this:
    ##################################################################################
    ###############################  Password Manager   ##############################
    ##################################################################################

### display_options()

    Also pretty self explanatory. Displays the options to the user:
    ----------------------------------------------------------------------------------
    [1] Load passwords from csv file
    [2] Display all your passwords.
    [3] Create new entry.
    [4] Wipe all entries
    [q] Exit
    ----------------------------------------------------------------------------------

### load_passwords()

    This function loads the passwords from a specified file into a dict object called "applications". First the key is loaded from the key, then a Fernet object from pythons cryptography library is initialised. Then the user is prompted to enter the name of his passwords file. Afterwards the csv file will be read line by line and each password entry is immediately decrypted and stored into the dict in plain text. A counter variable "i" keeps track of how many entries are being loaded, so that after the program displays how many entries were loaded. The function returns the applications dictionary only for testing purposes (test_project.py).

### generate_key()

    Here a secret key is being generated with the Fernet object, then this key is stored in a secret.key file.

### load_key()

    This function loads the key from the secret.key file. Here it is important that the secret.key file is in the same directory as the program. It returns the key.

### display_passwords()

    This function uses the tabulate module in order to display the name of the application, the username and the password in tabular format.

### create_new_passwd(appName="", passwd="", userName="", fileName="")

    This function is used to create new password and store them in the applications dict and the specified file. It can take 4 optional arguments only for test_project.py program, the default values of those arguments are all set to the empty string and are to be specified by the user in the normal execution (meaning not for testing) of the program. The user is first asked to enter the name of the application for which he wants to store a password. Afterwards he has the choice to either manually enter a password or have one randomly created for him. If he chooses the latter he is asked for specifications for his random password through the get_passwd_specifications() function, then thos specifications are passed to the generate_random_password() function and the thereby created password is stored in a variable named passwd. In the former case the user is simply asked to enter a password. After that the user is asked wheter he would like to specify a username for that password. If so he is prompted to enter that username. Then the password first gets encoded and then encrypted. In the next step do user gets asked for a filename in which to store his data, then his entries are first stored in a dictionary, and after with the help of a csv writer are stored in the by him specified csv file.

### get_passwd_specifications(answers)

    This function is used in the case that the user wants to have a random password generated for him. It again can take a argument only for the sake of testing. The user is asked for 5 specifications: wheter he wants numbers, whether he wants lowercase letters, uppercase letters, special characters and the length of the password. Here a maximal length of 100 characters has been arbitrarily chosen, since in any case 100 random characters should be secure enough. This function then returns a dictionary containing those specifications. 

### print_specs(specs)

    This function prints the specifications specified in the get_passwd_specifications() function.

### generate_random_password(specs)

    In the case that the user wants a random password to be created for him this function accomplishes just that. The specifications from the get_passwd_specifications() are used here. Four lists are created here: one for alle the lowercase letters, one for all the uppercase letters, one for all the digits and one for a selection of special characters. Then only those lists which were specified are put into another list called "apply". Then a for loop with the number of iterations of the desired length of the password is run. For each iteration a random choice (with the help of pythons random module) is made from the lists in the apply list. Then a random choice is made between the elements in that list. This randomly chosen character is then added to the initially empty "passwd" string. At the end the passwd variable is returned.

### wipe(fileName="", ans="")

    This function is used to wipe all the information from a specified file (and in any case also the information contained in the applications dictionary). It again only takes arguments for testing. First the user is asked for the filename. Then this will will be opened an cleared, afterwards the applications dictionary will be completely cleared. Then the user is also given the option to delete the specified file. The for testing purposes only the applications dict is returned.

### clear_view()

    This function simply clears the view that the user is currently seeing. It does that in a windows shell as well as in a unix based shell.
