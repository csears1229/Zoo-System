from passlib.hash import pbkdf2_sha256
import mysql.connector
import user
from crud import *

# Menu for users to reset their password or view users in the database
def menu(user):
    # Condition used for the while loop
    quit = False
    # Welcom message for the users (zookeeper)
    print("\nHello, Zookeeper!\n\nAs zookeeper, you have access to " \
        "all of the animals' information and their daily monitoring " \
        "logs.\nThis allows you to track their feeding habits, habitat " \
        "conditions, and general welfare.\n")
    # Loop used for the menu for users
    while quit == False:
        print("\nPlease select a function from the menu below:")
        userInput = input("\nc = change your password\nv = view user\n\nSelection: ")
        if userInput == 'c':
            updatePassword(user.username)
        elif userInput == 'v':
            username = str(input("\nEnter username or enter 'all' to see all users: "))
            if username == 'all':
                findAll()
            else:
                user = findUser(username)
                printUser(user)
        elif userInput == 'quit':
            break
        else:
            print("\n!! Invalid Input !!\n")
    print("You have signed out of the system\n")
