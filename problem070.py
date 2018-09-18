import math
import itertools

def sieve():
    current = 1
    primes = []
    yield 2
    while True:
        isPrime = True
        current += 2
        limit = current**.5
        for prime in primes:
            if (prime > limit):
                break
            if (current % prime == 0):
                isPrime = False
                break
        if isPrime:
            primes.append(current)
            yield current
'''
def prime_factors(num):
	factors = []
	global prime_list, primesieve
	if max(prime_list) < num:
		p = 0
		while p < num:
			p = primesieve.next()
			prime_list.append(p)
	n = num
	for val in prime_list:
		while num % val == 0:
			num = num / val
			factors.append(val)
		if num == 1:
			break
	return list(set(factors))
'''

def prime_factors(n):
	"Returns all the prime factors of a positive integer"
	factors = []
	d = 2
	while (n > 1):
		while (n%d==0):
			factors.append(d)
			n /= d
		d = d + 1 if d == 2 else d + 2
		if d*d > n:
			if n > 1:
				factors.append(n)
			break
	return factors

def is_prime(num):
	global prime_list, primesieve
	if max(prime_list) < num:
		p = 0
		while p < num:
			p = primesieve.next()
			prime_list.append(p)
	return num in prime_list

def phi(num):
	product = num
	primes = prime_factors(num)
	for prime in primes:
		product *= (1 - (1.0/prime))
	return int(product)

def phi_prime(prime):
	return prime - 1

def is_perm(a, b):
	if len(a) != len(b):
		return False
	for c in a:
		b = b.replace(c, '', 1)
	if len(b) != 0:
		return False
	return True

def discard(n, lowquotient):
	possibles = []
	for perm in itertools.permutations(str(n)):
		val = int(str(''.join(perm)))
		if val < n and val % 2 == 0 and float(n) / val < lowquotient:
			return False
	return True

primesieve = sieve()
primesieve.next()
prime_list = [2]

if __name__ == '__main__':
	maximum = 10**7
	smallest = 10**7
	prime = 0
	#s = sieve()
	n = 1
	while n < 10**7:
		n += 2
		#if discard(n, smallest):
		#	continue
		p = phi_prime(n) if is_prime(n) else phi(n)
		val = float(n)/p
		if is_perm(str(n), str(p)):
			if smallest > val:
				smallest = val
			print('n: {0}, phi: {1}, n/phi: {2}'.format(n, p, val))
		#print('NOT PERM n: {0}, phi: {1}, n/phi: {2}'.format(n, p, val))
		#print('n: {0}, phi: {1}, n/phi: {2}'.format(n, p, val))
	print(smallest)