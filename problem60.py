'''
Created on Apr 28, 2010

@author: bmann
'''
import math
import sys

def intsfrom(i):
    while True:
        yield i
        i += 1
        
def exclude_multiples(n, ints):
    for i in ints:
        if (i % n):
            yield i

def sieve(ints):
    while True:
        prime = ints.next()
        yield prime
        ints = exclude_multiples(prime, ints)
        
def is_prime(num):
    max = int(math.floor(math.sqrt(num) + 1))
    for i in xrange(2, max):
        if num % i == 0:
            return False
    return True

def permute(list, choose):
    i = 0
    max = 0
    while i < choose:
        max += 2 ** (len(list) - (i + 1))
        i += 1
    for j in range(max + 1):
        binary = bin(j)[2:]
        if binary.count("1") == choose:
            if len(binary) < len(list):
                pad = "0" * (len(list) - len(binary))
                binary = pad + binary
            output = []
            for x in range(len(binary)):
                if binary[x] == "1":
                    output.append(list[x])
            yield output
            
def permute_sets(list, choose):
    i = 0
    max = 0
    while i < choose:
        max += 2 ** (len(list) - (i + 1))
        i += 1
    for j in range(max + 1):
        binary = bin(j)[2:]
        if binary.count("1") == choose:
            if len(binary) < len(list):
                pad = "0" * (len(list) - len(binary))
                binary = pad + binary
            output = []
            for x in range(len(binary)):
                if binary[x] == "1":
                    output.append(list[x])
            yield output

def next_prime(num):
    val = num + 1
    while True:
        if is_prime(val):
            return val
        val += 1

def concats_are_prime(primes):
    for perm in permute(primes, 2):
        if not is_prime(int(str(perm[0]) + str(perm[1]))) or not is_prime(int(str(perm[1]) + str(perm[0]))):
            return False
    return True

if __name__ == '__main__':
    choose = 3
    choose_count = 2
    #s = sieve(intsfrom(2))
    f = open('primes.txt', 'r')
    primes_list = f.read().split(" ")
    f.close()
    prime_pool = []
    prime_pool2 = []
    prime_pool3 = []
    prime_pool4 = []
    for curr_prime in primes_list:
        curr_prime = int(curr_prime)
        prime_pool.append(curr_prime)
        #for perm in permute(prime_pool, 2):
        for p0 in prime_pool:
            perm = [p0, curr_prime]
            if concats_are_prime(perm):
                s1 = set(perm)
                if s1 not in prime_pool2:
                    prime_pool2.append(s1)
                    #for s2 in prime_pool2:
                    s2 = s1
                    for p1 in prime_pool:
                        if p1 not in s2:
                            l1 = list(s2)
                            l1.append(p1)
                            if concats_are_prime(l1):
                                s3 = set(l1)
                                if s3 not in prime_pool3:
                                    prime_pool3.append(s3)
                                    s4 = s3
                                    for p2 in prime_pool:
                                        #if p2 not in s4:
                                        l2 = list(s4)
                                        l2.append(p2)
                                        if concats_are_prime(l2):
                                            s5 = set(l2)
                                            if s5 not in prime_pool4:
                                                prime_pool4.append(s5)
                                                print(s5)
                                                for p3 in prime_pool:
                                                    #if p3 not in s5:
                                                    l3 = list(s5)
                                                    l3.append(p3)
                                                    if concats_are_prime(l3):
                                                        print(l3)
                                                        sys.exit(0)
                
    