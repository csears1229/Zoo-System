from passlib.hash import pbkdf2_sha256
import mysql.connector
import user
from crud import *

# Menu for users that are "Admin"
def menu():
    # Welcome message for the Admin
    print("\nHello, System Admin!\n\nAs an administrator, you have access to the zoo's " \
        "main computer system.\nThis allows you to monitor users in the system and their roles.\n")
    # Condition used for while loop
    quit = False
    # While loop to give menu functionallity to the user. All functions are found in the CRUD.py
    # this is just the menu available for "Admin" to access certain functions
    while quit == False:
        print("\nPlease select a function from the menu below:")
        print("\nc = create new user\nv = view existing user\nu = update existing user\nr = remove user\n")
        userInput = input("\nSelection: ")
        if userInput == 'c':
            createUser()
        elif userInput == 'v':
            username = str(input("\nEnter username or enter 'all' to see all users: "))
            if username == 'all':
                findAll()
            else:
                user = findUser(username)
                printUser(user)
        elif userInput == 'u':
            update = str(input("\np = Reset Password\nu = Unlock Account\n\nSelection: "))
            username = str(input("\nEnter username: "))
            if update == 'p':
                updatePassword(username)
            elif update == 'u':
                unlockAccount(username)
        elif userInput == 'r':
            username = str(input("\nEnter username: "))
            deleteUser(username)
        elif userInput == 'quit':
            quit = True
        else:
            print("\n!! Invalid Input !!\n")
    print("You have signed out of the system\n")
