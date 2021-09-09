x = input("Enter a Number: ")
y = 0
try:
	y = 10 / int(x) * 100
	print("y =", y)
finally:
	print("In Finally Y=", format(y, '.2f'), "%")
