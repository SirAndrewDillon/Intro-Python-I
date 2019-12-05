# from codingame.com

def sieve(num: int) -> list:
	primes = 2*[False] + (num-1)*[True]
	# more effecient to max out at sqrt of num
	sqr = int(num**0.5+1.5)
	for i in range(2, sqr):
		if primes[i]:
			for j in range(i*i, num+1, i):
				primes[j] = False
	return [n for n, isPrime in enumerate(primes) if isPrime]