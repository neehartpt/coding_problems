if __name__ == "__main__":
	print "Enter number of test cases:"
	n = int(raw_input())
	for _ in range(n):
		print "coordinates of first rectangle:"
		A = map(int, raw_input().split())
		print "coordinates of second rectangle:"
		B = map(int, raw_input().split())
		if (B[0] > A[2] or A[0] > B[2]):
			print "0"
		elif (A[1] < B[3] or B[1] < A[3]):
			print "0"
		else:
			print "1"
