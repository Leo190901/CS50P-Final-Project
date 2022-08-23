# Password Manager

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

    This function loads the key from the secret.key file. It return this key.

### display_passwords()

    This function uses the tabulate module in order to display the name of the application, the username and the password in tabular format.
