
# !If else ladder only one thing is excecuted
# !If
# !elif # Can be used multiple times
# !else
a = 55
if(a < 3):
    print("The value of 3 is not greater than a")
elif(a > 59):
    print("The value of a is greater than 3")
else:
    print("The value is not greater than 3 or 59")

x = 23
if(x > 2):
    print("The value of x is greater than 2")
    print("True")
if(x < 8):
    print("The value of 8 is greater than x")
    print("False")
if(x == 2):
    print("The value of x is equal to 2")
    print("False")
else:
    print("false")

'''# Quiz - Write a program to print yes when the age entered
by the user is greater than or equal to 18'''
age = int((input("Enter Your Age:")))
if(age > 18):
    print("True")
else:
    print("No")
if(age == 18):
    print("True")

# ! Else Statement/Condition is optional
