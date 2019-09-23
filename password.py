while True:
    password = input("Please, introduce your new password: ")
    checkpass = input("Please, introduce again your new password: ")
    if password == checkpass:
        break
    else:
        print("You've written two different passwords. Please, fuck off and write it again.")
enterpass = input("What is your pass?")
if enterpass == password:
    print("Welcome!")
else:
    print("Get out of here, please.")
