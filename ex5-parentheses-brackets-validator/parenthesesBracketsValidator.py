def main():
	openingBrackets = {"(":0, "[":0, "{":0}
	closingBrackets = {")":0, "]":0, "}":0}
	quotes = 0

	filename = raw_input("Give me the name of the .py file: ")
	while(filename[-3::] != ".py"):
		filename = raw_input("Wrong file, give me a .py file: ")
	try:
		with open(filename) as file:
			filetext = file.read()
	except OSError:
		print "Error accessing file. Check filename and path and try again..."


	for line in filetext:
		for char in line:
			if char == "[":
				openingBrackets.update({"[":(openingBrackets["["]+1)})
			if char == "(":
				openingBrackets.update({"(":(openingBrackets["("]+1)})
			if char == "{":
				openingBrackets.update({"{":(openingBrackets["{"]+1)})
			if char == '"':
				quotes += 1

			if char == "]":
				closingBrackets.update({"]":(closingBrackets["]"]+1)})
			if char == ")":
				closingBrackets.update({")":(closingBrackets[")"]+1)})
			if char == "}":
				closingBrackets.update({"}":(closingBrackets["}"]+1)})

	print openingBrackets
	print closingBrackets
	print '": '+str(quotes)

	if openingBrackets["("] == closingBrackets[")"] and openingBrackets["{"] == closingBrackets["}"] and openingBrackets["["] == closingBrackets["]"] and quotes % 2 == 0:
		print "Your brackets are in order, go on."
	else:
		print "You are missing something, your code is wrong." 


if __name__ == '__main__':
	main()