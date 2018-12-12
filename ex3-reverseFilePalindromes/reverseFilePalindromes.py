
def main():
	with open("myfile.txt") as file:
		filetext = file.read()

	print filetext
	lines = filetext.split('\n')
	newlines = []
	print lines
	count = 0
	for line in lines:
		words = line.split(' ')
		for word in words:
			if len(word) > 2:
				if word == word[::-1]:
					count += 1
		newlines.append(line[::-1])
	filetext = "\n".join(newlines)
	print filetext
	print "Number of palindromes: " + str(count)






if __name__ == '__main__':
	main()