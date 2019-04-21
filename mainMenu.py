from passlib.hash import pbkdf2_sha256
import mysql.connector
import user
from crud import *
import adminMenu
import userMenu

# condition used for the while loop
quit = False
# counter to count bad password attempts to lock account after 3 bad attempts
badPassword = 0
# Welcome message when the app starts
print("Welcome to the Zoo Authentication System")
print("Type \"quit\" at any time to exit the application")
# Main menu loop
while quit == False:
    # Get username for login
    username = str(input("Please enter your username: "))
    # If user types 'quit' exit the application
    if username == "quit":
        quit = True
        continue
    plainTextPassword = str(input("Please enter your password: "))
    # If user types 'quit' exit the application
    if plainTextPassword == "quit":
        quit = True
        continue
    else:
        # Get user information and store it as an Object
        user = findUser(username)
        # If the user is not found it will return an empty object check to see if
        # Object is empty and give error message that user is not found
        if type(user) == type(None):
            print("\n!! Username Not Found !!\n")
        # Check to see if user is not locked and password is correct
        elif pbkdf2_sha256.verify(plainTextPassword, user.password) and user.accountLockedOut == False:
            # Account not locked and password is correct log in user as user type (admin or user)
            if user.role == "Admin":
                adminMenu.menu()
                badPassword = 0
            elif user.role == "User":
                userMenu.menu(user)
                badPassword = 0
            else:
                # If for some reason user does not have role or role is not correct it will give error
                print("\n!! User Role Undefined. Please Contact Your System Admin !!\n")
                badPassword = 0
        else:
            # if the password is correct but the acount is locked it will not login and will give error message
            if pbkdf2_sha256.verify(plainTextPassword, user.password) or user.accountLockedOut:
                print("\n!! Account Locked - Contact Your System Admin for Assistance !!\n")
            # if account is not locked but the password is wrong it will give an error and increase
            # value of badPassword until 3 incorrect attempts then the user will be locked out
            elif user.accountLockedOut == False:
                badPassword += 1
                print("\n!! Invalid Password Please Try Again !!\n")
                print(badPassword)
                if badPassword == 3:
                    lockAccount(user.username)
# Message shown when user exits the system
print("Now Exiting the System")
print("Goodbye")
