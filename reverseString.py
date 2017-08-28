if __name__ == "__main__":
	print "Enter the number of test cases:"
	n = int(raw_input())
	for _ in range(n): 
		print "Enter the string"
		arr = raw_input().split('.')
		print ".".join(arr[::-1])
