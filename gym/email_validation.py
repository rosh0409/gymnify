import re

validEmail = "^[a-z]++[\.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email = input("Enter your email :: ")

if re.search(validEmail,email):
    print("Right Email")
else:
    print("Wrong Email")