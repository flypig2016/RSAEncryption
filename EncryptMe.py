#!/usr/bin/env python2

import random
from libnum import *
import sys


class private_key(object):
	e = 65537

	def __init__(self,bitlength):
		self.p = generate_prime(bitlength)
		print self.p
		self.q = generate_prime(bitlength)
		print self.q
		self.phi = (self.p - 1) * (self.q - 1)
		self.n = self.p * self.q
		self.d = invmod(self.e, self.phi)
	
class public_key(object):
	def __init__(self, private_key):
		self.n = private_key.n
		self.e = private_key.e

class key(object):
	
	def __init__(self, bitlength):
		self.private_key = private_key(bitlength)
		self.public_key = public_key(self.private_key)

	def print_key(self):
		print "public key (%d,%d)"% (self.public_key.n, self.public_key.e)
		print "private key ({0},{1})".format(self.private_key.n, self.private_key.d)

class RSA(object):
	def __init__(self, key):
		self.key = key
		self.plaintext = 0
		self.ciphertext = 0

	def encrypt(self, plaintext):
		self.plaintext = plaintext
		ciphertext= pow(self.plaintext, self.key.private_key.e, self.key.private_key.n)
		return ciphertext
		
	def decrypt(self, ciphertext):
		self.ciphertext = ciphertext
		plaintext = pow(self.ciphertext, self.key.private_key.d, self.key.private_key.n)
		return plaintext

	def print_message(self):
		print "Encrypted number %d "% self.ciphertext
		print "Decrypted number %d "% self.plaintext

if __name__ == '__main__':
	#encrypted(int(sys.argv[1]))
	k = key(1024)
	k.print_key()
	r = RSA(k)
	c = r.encrypt(57777)
	d = r.decrypt(c)
	r.print_message()



