min_length = 8
password = input("Enter your password: ")

while len(password) < min_length:
    password = input("Password too short. Enter your password: ")

print('*' * len(password))
