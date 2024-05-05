#for i in range(100):
#    print(i)

#the first argument represents the starting point, second represents the end point, third represents the interval
#for i in range(1,20,2):
#    print(i)

#for i in "Achilles":
#   print(i)

#creating a count down program
#import time
#for seconds in range(10,0,-1):
#   print(seconds)
#   time.sleep(1)
#print("It's a new day!")

#num1 = int(input("Enter the first number "))
#num2 = int(input("Enter the second number "))
#sum = num1 + num2
#if sum < 20:
#    print(" You're good to go! ")



#A program to accept and calculate the sum of two numbers, print the sum if its more than 20, re-enter numbers if its
#   less than 20
# def calculate_sum():
#    while True:
#        num1 = float(input("Enter the first number "))
#        num2 = float(input("Enter the second number "))
#        sum_nums = num1 + num2
#        if sum_nums < 20:
#            print("The sum of ", str(num1), " and ", str(num2), " is less than 20, please try again.")
#        else:
#            print("The sum of", str(num1), "and", str(num2) ," is greater than or equal to 20.")
#            break
# calculate_sum()

#A program to calculate the sum of natural numbers
# def sum(n):
#    if n < 0:
#        return "invalid input: n must be a non-negative integer"
#    sum_natural = n *  (n + 1)//2
#    return sum_natural
# n = int(input("Enter an integer n: "))
# print("The sum of natural numbers up to",  str(n), "is:", sum(n))

#def odd_num(n):
#    if n < 0:
#        return "Invalid input: n must be a non'-negative integer"
#    sum_odd = 0
#    for i in range(1, n+1, 2):
#        sum_odd = i
#        return sum_odd
#n = int(input("Enter a non-negative integer "))
#print("The sum of odd numbers up to n is:", odd_num(n))

#swaping the values of variables
#a = input("a: ")
#b = input("b: ")
#c = a
#a = b
#b = c
#print(a)
#print(b)

#Band Name Generator
#first = input("What is the name of your girlfriend?\n ")
#second = input("What is your nick name?\n ")
#print("The name of your band is ", str(second[:4]) + str(first[2:]))

#num1 = input("Enter num 1 \n")
#num2 = input("Enter num 2 \n")
#num3 = input("Enter num 3 \n")
#print (max(num1,num2,num3))

#Importing a calendar
#import calendar
#start = int(input("Enter start year "))
#print(calendar.calendar(start,1))

# def main():
# num = input("enter the number numbers ").split()
# for i in range (0, len(num)):
# num[i] = int(num[i])
# verage = int(num)/len(num)
# print (verage)


# main()

#A program to accept a user password
# password = "Achilles69"
# bing = input("Enter password: ")
# while password != bing:
#    bing = input("Enter password: ")
# print("You're guaranteed access!")

# global and local variables
#x = "Awesome"
#def myfunc():
#    x = "fantastic"
#    print("Python is " + x)
#myfunc()
#print("Python is " + x)

#random Numbers
#import random
#print(random.randrange(1,10))

# Checking if a text in a piecce of text
# chc = "Coding is a whole new vibe"
# print("Coding" in chc)

# print("Welcome to the tip calculator")
# bill = int(input("What was the total bill? "))
# num = int(input("How many people are to split the bill? "))
# per = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# percentage = per/100 * bill
# print("Each person is to pay " +str(percentage))
# print("THANK YOU!!!")


'''age = int(input("How old are you? "))
end = 90
years_remaining = end - age
weeks_left = years_remaining * 52
days_left = years_remaining * 365
print("You have " + str(weeks_left), " weeks", "and " +str(days_left), "days left to live")'''

# num = int(input("Enter a number "))
# if num % 2 == 1:
#     print("Odd")
# else:
#     print("Even")

'''height = float(input("What's your height? "))
mass = float(input("What's your mass? "))
BMI = mass/height * height
if BMI < 18.5:
    print("You're underweight")
elif BMI <= 25:
    print("Your weight is normal")
elif BMI <= 30:
    print("You're overweight")
elif BMI <= 35:
    print("Obese")
else:
    print("Clinically obese")'''

#Rollercoster bill calculator
# print("Welcome to the Rollercoster!!!")
# height = float(input("Enter your height "))
# if height < 0.5:
#     print("You can't have a ride!!!")
# else:
#     # print("You can have a ride!!!")
#     age = int(input("How old are you? "))
#     if age >= 18:
#         # print("You're good to go!!!")
#         pictures = input("Would you like to book for pictures? Y or N ")
#         if pictures == "Y":
#             print("Your bill will be in soon")
#         else:
#             print("Your bill is being calculatored")
#     else:
#         print("You are under age")

#Calculating the average of scores
'''Scores = input("Enter the scores of the student ").split()
for i in range(0, len(Scores)):
    Scores[i] = int(Scores[i])
average = sum(Scores)/len(Scores)
print(average)'''


#listing in python
# food = ["Koose", "Pork", "Gob3"]
# # food[0] = "TZ"
# # food.append("Rice")
# # food.remove("Gob3")
# food.sort()
# # food.pop()
# for i in food:
#     print(i)

import random
# victim = input("Enter the names of the friends ")
# hey = victim.split(" ")
# for i in hey:
#     print(f"{hey} is responsible for the payment of the bills ")

#Assignment
# pin = "0000"
# Amount_in_Account = 10000
# print("Welcome to your bank portal ")
# password = input("Enter your 8-digit pin ")
# while pin != password:
#     input("Sorry! you entered a wrong pin. Enter the pin again ")
#     break
# else:
#     print("Access granted")
# choice = input("Which transaction would you like to undertake? " "Deposit, Withdrawal,Check Account Balance ")
# if choice == "Withdrawal":
#     Amount_to_withdraw = int(input("How much would you like to withdraw? "))
#     Authorisation = input("Enter your pin ")
#     while  Authorisation!= password:
#         input("Sorry! you entered a wrong pin. Enter the pin again ")
#         break
#     else:
#         remainder = Amount_in_Account - Amount_to_withdraw
#     while Amount_to_withdraw > Amount_in_Account:
#             print("The amount you have is less than the requested amount ")
#     print(f"An amount of {Amount_to_withdraw} has been deducted from your account. Your current balance is {remainder}")
# elif choice == "Deposit":
#     Amount_to_deposit = int(input("How much would you like to deposit? "))
#     Authorisation = input("Enter your pin ")
#     while  Authorisation!= password:
#         input("Sorry! you entered a wrong pin. Enter the pin again ")
#         break
#     Balance = Amount_in_Account +Amount_to_deposit
#     print(f"An amount of {Amount_to_deposit} has been added to your bank account. Your total account balance is {Balance}")
# elif choice == "Check Account Balance":
#     Authorisation = input("Enter your pin ")
#     while  Authorisation!= password:
#         input("Sorry! you entered a wrong pin. Enter the pin again ")
#         break
#     print(f"Your account balance is {Amount_in_Account}")
# print("Thanks for transacting with us")


#other trial on the same assignment
#print("          <<<<<<<<<<<<<<<<<<<<<<<<<<WELCOME TO WORLD BANK<<<<<<<<<<<<<<<<<<<<                   ")
# revenue = 10000.00
# print("Welcome to World bank")
# print("Insert bank ID ")
# # password setup
# for attempt in range(3, 0, -1):
#     password = (input("Enter pin: "))
#     if password == "1234":
#         break
#     else:
#         print("Wrong password")
# if attempt == 1 and password != "1234":
#     print("Access denied")
#     quit()
# else:
#     print('''     Access Granted''')
# # service provided
# choice = input("""Welcome to your bank portal.
# Press the number below for our service
# 1.Deposit
# 2.Withdrawal
# 3.Check balance
# : """)
# # deposit
# if choice == "1":
#     credited = float(input("How much do you want to deposit: GHc "))
#     balance = revenue + credited
#     print(f"Your current balance is GHc{balance}")
# # Withdrawal
# elif choice == "2":
#     debited = float(input("How much do you want to withdraw: GHc "))
#     if debited >= revenue:
#         print("Insufficient balance to make the transaction")
#     # balance
#     else:
#         balance = revenue - debited
#
# # elif choice == "3":
#     # balance = revenue
# else:
#     print("Your current balance is GHc", revenue)



# x = 0
# a = 0
# b = -5
# if a > 0:
#     if b <0:
#         x = x +5
#     elif a >5:
#         x = x + 4
#     else:
#         x = x +3
# else:
#     x = x + 2
# print(x)


# x = 0
# while (x < 100):
#     x += 2
# print(x)

# x = 36/4*(3+2)*4 +2
# print(x)

# listOne = [20,40,60,80]
# listTwo = [20,40,60,80]
# print(listOne == listTwo)
# print(listOne is listTwo)

# x = 2.5679
# y = 9.0
# print("Answers {:.3f} and {:.3f}".format(x,y))

# def s(x):
#     return x*x
# tot = 0
# for n in [1, 3, 5]:
#     tot = tot + s(n)
# print(tot)

# TRAIL
# factorial of a number
'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial (n - 1)
num = int(input("Enter a number: "))
print("The factorial of " +str(num), " is", factorial(num))'''

# pyramid
'''print("Normal Pyramid")
for i in range(5):
    x = "#"
    x = x * i
    print(f'{x:^10}')'''

#Invert Pyramid
'''print("Invert Triangle")
for i in range(5):
    x = "*"
    x = x *(5 - i)
    print(f'{x:^10}')'''

#Right Handed Pyramid
'''print("Right handed pyramid")
for i in range(5):
    x = " * "
    x = x * i
    print(f'{x: <10}')'''

'''a = "A"
print(int(a, 16))'''

password = "SecretWord"
guess = input("Kindly enter your password: ")
while guess != password:
    guess = input("Kindly enter your password: ")
print ("Access Granted")

