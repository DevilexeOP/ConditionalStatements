# Write a program to find greatest of four numbers entered by user
from cgi import print_arguments
from errno import ESTALE


num1 = int((input("Enter the number 1 :")))
num2 = int((input("Enter the number 2 :")))
num3 = int((input("Enter the number 3 :")))
num4 = int((input("Enter the number 4:")))

if(num1 > num4):
    f1 = num1
else:
    f1 = num4

if(num2 > num3):
    f2 = num2
else:
    f2 = num1

if(f1 > f2):
    print(str(f1) + "- is greatest")
else:
    print(str(f2) + "is greatest")

'''Write a program to find whether student is pass or fail , 
it requires total 40% and atleast 33% in each subject to pass
Assume 3 subjects and take marks as an input from user'''

m1 = int((input("Enter your marks 1\n-")))
m2 = int((input("Enter your marks 2\n-")))
m3 = int((input("Enter your marks 3\n-")))

if(m1 < 33 or m2 < 33 or m3 < 33):
    print("You have failed because u have percentage less than 33 in one of the subject ")

if(m1+m2+m3)/3 < 40:
    print("You have failed due to percent less than 40")
else:
    print("You have passed , with flying colors  !")

'''Q3 - A spam comment is defined as a text containing following keywords'''
'''  "make a lot of money" , "buy now" , "subscribe this" , "click this"
write a program to detect these spams '''

text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this " in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is Spam ")
else:
    print("This tetx is not spam")

'''Q4- Write a program to find whether a given 
username contains less than 10 characters or not'''
name = input("Enter Your name\n")
if(len(name) < 10):
    print("The name has less than 10 characters ")
elif(len(name) > 10):
    print("The name has more than 10 characters ")
else:
    print("Your name has 10 characters")

'''Q5 - Write a program which finds out whether the given name is present 
in a list or not '''
names = ["mukesh", "suresh", "rajan"]
name = input("Enter the name to check\n")
if name in names:
    print("your name is present in the list")
else:
    print("your name is not present")

'''Q5 -  Write a program to calculate the grade of a student 
from  his marks from thew following scheme
90-100 = Ex
80-90 = A
70-80 = B
60-70 = C
50-60 = D
<50 = F'''

marks = int((input("Enter your marks\n")))

if marks >= 90:
    grade = "Ex"

elif marks >= 80:
    grade = "A"

elif marks >= 70:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is " + grade)

'''Q6 - Write a program to find out whether a given post is 
talking about "D3VIL" or not '''
post = input("Enter the Name\n")
if "D3VIL" in post:
    print("D3VIL is present in the post")
else:
    print("D3VIl is not present in the post")
