def foo():
	# 1
	print ("Call 1")
	yield 0
	# 2
	print("Call 2")
	yield 1
	print("CAll 3")
	yield 2

a=foo()
a.next()