# Stored credentials
correct_username = "admin"
correct_password = "1234"

# Taking input from user
username = input("Enter username: ")
password = input("Enter password: ")

# Checking login
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Credentials")