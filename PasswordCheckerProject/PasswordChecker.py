#Ask the user to create a password
#Check if it meets these rules:
    #At least 8 characters long
    #Contains at least one number
#If it fails:
    #Tell them what’s wrong
    #Ask them to try again
#Keep looping until they enter a valid password
#When valid → print “Password accepted”


password = input("Please Enter your password: ")
len(password)

if len(password) < 10:
    print("Please create a stronger password by making it more than 10 digits")
else:
    print("This password is acceptable")
