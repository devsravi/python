import random


try:
    name = input("Enter your name: ")
    print("Hi " + name + ", ")
    mobilenumber = int(input("Please enter your mobile number: "))
    otp = random.randint(100000, 999999)
    message = "Dear "+ name +", your OTP is: " + str(otp)
    print(message)
except ValueError:
    print("Something went wrong please try again!") 


