if __name__ == "__main__":
	print "Enter number of test cases:"
	n = int(raw_input())
	for _ in range(n):
		print "Enter the string:"
		s = raw_input().strip()
		l = 0 
		for i in s:
			if (s.count(i) == 1):
				print i
				break
			l += 1
		if (l == len(s)):
			print "-1"
