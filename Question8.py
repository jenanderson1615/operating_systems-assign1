#Jen Anderson
#anderjen@onid.oregonstate.edu
#CS311-400
#Homework1
#Question8 


#To use user input instead of a set value
#userInput = input('Enter a max value for the range: ')
max = 100

#This function takes in the upper limit as a parameter and returns the number
#of primes below the parameter and the values of all those primes   
def getPrimes(max):
	primeArray = range(2, max + 1)
	x = 2
	while x <= max:
		i = 2
		while (x*i) <= max:
			if x*i in primeArray:
				primeArray.remove(x*i)
			i += 1
		x += 1
	return len(primeArray), primeArray

numberOfPrimes, primes = getPrimes(max)
print numberOfPrimes
print primes
