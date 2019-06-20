def genfunc():
	print ('first call')
	yield 1
	print ("second")
	yield 2

a = genfunc() # note nothing happens here
a.next() # call the function the first time
a.next() # call the function the second time