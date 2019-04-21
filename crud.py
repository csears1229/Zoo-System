from passlib.hash import pbkdf2_sha256
import mysql.connector
import user

# Create the connection to the MySQL database
mydb = mysql.connector.connect (
    host='sql176.main-hosting.eu',
    user='u547332284_test',
    passwd='test123',
    database="u547332284_test",
    auth_plugin="mysql_native_password"
)

# Create cursor for sending SQL commands to the database
cursor = mydb.cursor(buffered=True)

# Create new user and add them to the database
# Function is only available to admin
def createUser():
    print("Enter the following information - all fields are required")
    firstName = str(input("Enter New User's First Name: "))
    lastName = str(input("Enter New User's Last Name: "))
    username = createUsername(firstName, lastName)
    print("Username: " + username)
    password = createPassword()
    role = str(input("Enter New User's Role (Admin/User): "))
    sql = "INSERT INTO name(first_name, last_name) values(%s, %s);"
    val = (firstName, lastName)
    cursor.execute(sql, val)
    mydb.commit()
    sql = "INSERT INTO users(username, password, role, lockout_status, namekey)\
        values(%s, %s, %s, %s, %s);"
    val = (username, password, role, "F", cursor.lastrowid)
    cursor.execute(sql, val)
    mydb.commit()
    print("User successfuly created")

# Function used to create a new username username format is first initial last name
# it will check username and if it is taken it will append a number to the end
# this method is only called in the createUser method
def createUsername(firstName, lastName):
    username = firstName[:1] + lastName
    user = findUser(username)
    if type(user) == type(None):
        return username
    else:
        for x in range(1, 10):
            username = username + str(x)
            user = findUser(username)
            if type(user) == type(None):
                return username

# Method to set users password as default password (password1)
# user can change password when logged in
# this method is only called in the createUser method
def createPassword():
    password = "password1"
    hashedPassword = pbkdf2_sha256.encrypt(password, rounds=10, salt_size=10)
    print("Password has been set to the default password (password1)")
    return hashedPassword

# Method to update user password this method can be called by admin
# to reset user password or by user to change their own password
def updatePassword(username):
    password = str(input("Enter a new password for " + username + ": "))
    hashedPassword = pbkdf2_sha256.encrypt(password, rounds=10, salt_size=10)
    sql = "UPDATE users SET password = %s WHERE username = %s;"
    val = (hashedPassword, username)
    cursor.execute(sql, val)
    mydb.commit()
    print("Password for " + username + " has been set!")

# Method for an admin to unlock a users account if the get three wrong password attempts
def unlockAccount(username):
    sql = "UPDATE users SET lockout_status = 'F' WHERE username = '" + username +"';"
    cursor.execute(sql)
    mydb.commit()
    print("Account Unlocked for ", username)

# Method to lock a users account if they get their password wrong 3 times
# this method is called automatically from the main menu after 3 bad attempts
def lockAccount(username):
    sql = "UPDATE users SET lockout_status = 'T' WHERE username = '" + username +"';"
    cursor.execute(sql)
    mydb.commit()
    print("Account Locked for " + username + " Contact System Admin for Assistance.")

# Method to query the database to find a user and store it as an object to be used
# can be called by either admin or user
def findUser(username):
    sql = "SELECT first_name, last_name, \
        username, password, role, lockout_status, namekey FROM name as name \
        INNER JOIN users as users on \
        name.name_id = users.namekey WHERE username = '" + str(username) + "';"
    cursor.execute(sql)
    myresult = cursor.fetchone()
    if type(myresult) == type(None):
        return myresult
    _user = user.User(myresult[0], myresult[1], myresult[2], myresult[3], myresult[4], myresult[5], myresult[6])
    return _user

# Method to find and display all users in the database
# can be called by admin or user
def findAll():
    sql = "SELECT first_name, last_name, \
        username, password, role, lockout_status, namekey FROM name as name \
        INNER JOIN users as users on \
        name.name_id = users.namekey;"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    for x in myresult:
        _user = user.User(x[0], x[1], x[2], x[3], x[4], x[5], x[6])
        printUser(_user)

# Method used to print the users when they are stored as objects.
# This will print the user information in an easy-to-read format
def printUser(user):
    print("First Name: " + user.firstName)
    print("Last Name: " + user.lastName)
    print("Username: " + user.username)
    if user.accountLockedOut == True:
        print("Account Locked: Yes")
    else:
        print("Account Locked: No")
    print("User Role: " + user.role)
    print("\n")

# Method used to delete a user from the database can only be called by admin
def deleteUser(username):
    user = findUser(username)
    sql = "DELETE FROM name WHERE name_id = " + str(user.userID) + ";"
    cursor.execute(sql)
    mydb.commit()
    print(cursor.rowcount, "record deleted")
