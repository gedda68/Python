dict
dict1 = {}

dict2 = {"1":"one"}
dict3 = {"2":"two","3":"three","4":"four"}

print(dict)
print(dict1)

print(dict2)
print(dict3)

dict3["5"] = "five"

print(dict3)

dict3["5"] = "five"
print(dict3['2'])


for k in dict3.keys():
	print(k)