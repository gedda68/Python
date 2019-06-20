BAD=1

def foo():
	print "Foo Called"
	global BAD
	BAD = 2

def foo1():
	print "Foo 1 called"
	BAD = 12

foo() #1
print BAD

foo1() #2

print BAD