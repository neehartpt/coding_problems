s = raw_input()
l = len(s)
count = [1]
for i in range(1, l):
	count.append(0)
	if (s[i] > 0):
		count[i] = count[i-1]
	if (int(s[i-1:i+1]) < 27 and s[i - 1] > 0):
		if (i == 1):
			count[i] += 1
		else:
			count[i] += count[i-2]
print count[l-1]
