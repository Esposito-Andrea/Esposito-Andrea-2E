#take new password from user and save(tuple): one number, letter, ask for login(password again), check if its the correct password
password = (tuple(input("Type new password: ")))
hasnumber = False
hasletter = False
for char in password:
    if char.isdigit():
        hasnumber = True
    if char.isalpha():
        hasletter = True
if (hasnumber == True) and (hasletter == True):
    print("Correct")
else:
    password = input("Incorrect. Try Again")