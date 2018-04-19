#!python

import random
from libnum import *
import sys

e= 65537

def isprime(x):
	for i in xrange(2, x-1):
		if x%i == 0:
			return False
	else:
		return True

def generatePrime(bits):
	while True:
		value= random.getrandbits(bits)
		if isprime(value):
			return value


def encrypted(m):
	p= generatePrime(m)

	q = generatePrime(m)

	phi = (p -1 ) * (q-1)
	n = p * q

	d= invmod(e,phi)

	print "public key (%d, %d)"% (n,e)
	print "private key ({0},{1})".format(n,d)

	c=pow(m,e,n)
	print "encrypted number %d "% c

	decryptedM= pow(c,d,n)

	print "Decrypted number %d "% decryptedM

if __name__ == '__main__':
	encrypted(int(sys.argv[1]))






		