import string
if __name__ == "__main__":
	print "Enter number of test cases:"
	n = int(raw_input())
	alpha = string.ascii_uppercase
	a = alpha[25] + alpha[:25]
	print a
	for _ in range(n):
		print "Enter column number:"
		c = int(raw_input())
		res = []
		while (c > 26):	
			r = c%26; print r
			c = c//26; print q 
			res.append(a[r])
		res.append(a[c%26])
		print "".join(res[::-1])
