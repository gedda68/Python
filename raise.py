try:
	x = input("Enter a non-zero value: ")
	if x == 0:
		raise Exception
	print "You entered a valid value", x
except:
	print "Exception caught", x
