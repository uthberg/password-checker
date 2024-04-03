#!/usr/bin/python3

#defines password from user input
password = input("Enter a password: ")

#checks length of password is greater or equal to 16
if len(password) >= 16:
	
	print("Strong password detected!")

elif len(password) >= 12:

	print("Decent password detected!")
else:
	print("Weak password detected!")

