import random
from random import randint

def main():
	n = int(raw_input("Give me length of sequence: "))

	rng = random.SystemRandom();
	primes = []

	for i in range(2, n+1):
		flag = True
		for j in range(2, int(i**0.5)+1):
			if i % j == 0:
				flag = False
				break
		if flag == True:
			primes.append(i)
	print primes


if __name__ == '__main__':
	main()