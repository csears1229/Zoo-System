# Class used for holding the user information as an object to allow us to access
# parts of it later
class User:
    role = 'User'
    username = 'username'
    password = 'password'
    accountLockedOut = False
    firstName = 'firstName'
    lastName = 'lastName'
    userID = 0

    # Constructor for the class 
    def __init__(self, firstname, lastname, username, password, role, accountLockedOut, namekey):
        self.firstName = firstname
        self.lastName = lastname
        self.username = username
        self.password = password
        self.role = role
        self.userID = namekey
        if accountLockedOut == "T":
            self.accountLockedOut = True
        else:
            self.accountLockedOut = False
