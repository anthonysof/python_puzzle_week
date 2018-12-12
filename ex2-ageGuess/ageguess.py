import random
from random import randint

def main():
	rng = random.SystemRandom()
	guess = rng.randint(10, 60)
	max = 60
	min = 10
	guessnew = 0
	while(True):
		if max <= min or guessnew == guess:
			break
		print "is your age over: " + str(guess)
		resp = raw_input("y/n\n")
		guessnew = guess
		if resp == "y":
			min = guess
			guess = int(round((min + max) / 2))
		elif resp == "n":
			max = guess
			guess = int(round((min + max) / 2))
		
	print "Your age is " + str(guess+1)




if __name__ == '__main__':
	main()
