def countDecoding(s, l):
	if (l == 0 or l == 1):
		return 1
	count = 0
	if (int(s[l-1]) > 0):
		count = countDecoding(s, l-1)
	if (s[l-2] == '1' or s[l-2] == '2' and int(s[l-1]) < 7):
		count += countDecoding(s, l-2)
	return count

if __name__ == "__main__":
	print "Enter number of test cases:"
	n = int(raw_input())
	for _ in range(n):
		print "Enter String length:"
		l = int(raw_input())
		print "Enter String:"
		s = raw_input().strip()
		print countDecoding(s,l)


