
what = input("Hello, would you like to save to file 'OS' y or n?  ")

while what == "y":
	print("Thank you for accessing the OS system!")
	if "n":
		break
filename = 'OS.txt'

name = input("Please advise your name:  ")
with open(filename, 'w') as file_object:
	file_object.write(f"{name},\n")

address = input("Please advise your address:  ")
with open(filename, 'a') as file_object:
	file_object.write(f"{address},\n")

phone = input("Please provide phone number:  ")
with open(filename, 'a') as file_object:
	file_object.write(f"{phone}.")

with open(filename)as file_object:
	lines = file_object.readlines()

print(f"{name}, \n {address}, \n {phone}.")






