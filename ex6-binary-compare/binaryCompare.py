import binascii

def main():
	string1 = raw_input("Give me string #1: ")
	string2 = raw_input("Give me string #2: ")

	strbin1 = bin(int(binascii.hexlify(string1), 16))
	strbin2 = bin(int(binascii.hexlify(string2), 16))

	print strbin1
	print strbin2

	countdiff = 0

	if len(strbin1) > len(strbin2):
		for i in range(len(strbin2)):
			if strbin1[i] != strbin2[i]:
				countdiff += 1
		countdiff += len(strbin1) - len(strbin2)
	elif len(strbin1) < len(strbin2):
		for i in range(len(strbin1)):
			if strbin1[i] != strbin2[i]:
				countdiff += 1
		countdiff += len(strbin2) - len(strbin1)
	else:
		for i in range(len(strbin1)):
			if strbin1[i] != strbin2[i]:
				countdiff += 1

	print "They differ in: "+str(countdiff)+" bits."

if __name__ == '__main__':
	main()