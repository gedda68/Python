x = [1,2.45,"This is a string", 0]

print (len(x))

print(x[0])

print(x[1])
print(x[2])
print(x[3])

print()

x[2] = "This is a different string"

for e in x:
	print (e)

x[0:1] = [1,2,3,4,5]
print (x)
print (x[1])
print (x[2])
