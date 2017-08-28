if __name__ == "__main__":
	print "Enter number of test cases:"
	n = int(raw_input())
	for _ in range(n):
		print "Enter array:"
		a = map(int, raw_input().split())
		l = len(a)
		for i in range(0,l,2):
			if (i > 0 and a[i] < a[i-1]):
				a[i], a[i-1] = a[i-1], a[i]
			if (i < l-1 and a[i] < a[i+1]):
				a[i], a[i+1] = a[i+1],a[i]
		print a
