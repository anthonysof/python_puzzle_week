import re

def main():
	
	filename = raw_input("Give me the name of the .py file: ")
	while(filename[-3::] != ".py"):
		filename = raw_input("Wrong file, give me a .py file: ")
	try:
		with open(filename) as file:
			filetext = file.read()
	except OSError:
		print "Error accessing file. Check filename and path and try again..."

	regex = r"^\s*#.*$"

	regex2 = re.compile(regex, re.MULTILINE)
	result = re.sub(regex2, "", filetext)

	print "\n-----------\n\n"
	print result
	newfile = open(filename[:-3:]+"NoComments.py", "w+")
	newfile.write(result)
	print "Your new file was created!"

	






if __name__ == '__main__':
	main()