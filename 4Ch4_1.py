# Import the string modue for the constants required
import string

# Imput the string from the user and assume that it's ok
s = input("Please input a string using only lower and upper case letters: ")
valid = True

# Loop through all of the characters, checking to see if they are all
# in the valid groups we allow 
for c in s:
	if(c in string.ascii_uppercase):
		continue
	if(c in string.ascii_lowercase):
		continue
	print("You have entered an invalid character: [" + c + "]")
	valid = False
	break

# If the whole string was valid echo it back to the user
if valid == True:
	print ("You entered a valid string: " + str.capitalize(s))