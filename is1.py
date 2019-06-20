s = 1
ref = s
if s is ref:
	print "s is copy", s
else:
	print "s is not copy", s

t = 1
if s is t:
	print "s is t", s, t
else:
	print "s is not t", s, t