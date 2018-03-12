#!/usr/bin/env python2
import argparse
import math
import string

def error(msg):
	import sys
	print('[!] ERROR: %s'%msg)
	print('For more, see --help')
	sys.exit(1)


class Playfair:
	"""The Playfair Cipher Class
	This class encrypts pairs of characters, the key consists of a keysquare 25 characters in length.
	An example of key:
		M U Z E D
		F N V L S
		H O W A T
		I/J P X R B
		K Q Y G C

	To perform the substitution, apply the following 4 rules, in order,
	to each pair of letters in the plaintext:

	- If both letters are the same (or only one letter is left),
	  add an "X" after the first letter. Encrypt the new pair and continue.
	- If the letters appear on the same row of your table,
	  replace them with the letters to their immediate right respectively.
	- If the letters appear on the same column of your table,
	  replace them with the letters immediately below respectively.
	- If the letters are not on the same row or column,
	  replace them with the letters on the same row respectively
	  but at the other pair of corners of the rectangle defined by the original pair.
	  The order is important - the first letter of the encrypted pair is
	  the one that lies on the same row as the first letter of the plaintext pair.

	Fore more, see https://en.wikipedia.org/wiki/Playfair_cipher#Description
	"""
	def __init__(self, key, key_valid=False):
		'''
		@param key: Alpha string, accept spaces. (I is same as J in Playfair)
		'''
		key = ''.join(key.split()).upper() # remove all space include newlines, tabs
		if not key_valid and not Playfair.key_valid(key):
			error("Invalid key.")

		key = Playfair.remove_dups(key.replace('J', 'I'))
		for char in Playfair.DEFAULT_KEY:
			if char not in key:
				key.append(char)

		assert len(key) == 25, "Length of key is not equal 25"
		self.key = ''.join(key)

	def encode_pair(self, a, b):
		arow, acol = divmod(self.key.index(a), 5)
		brow, bcol = divmod(self.key.index(b), 5)
		if arow == brow:
			return (self.get_coord(arow, (acol + 1)%5), self.get_coord(brow, (bcol + 1)%5))
		elif acol == bcol:
			return (self.get_coord((arow + 1)%5, acol), self.get_coord((brow + 1)%5, bcol))
		else:
			return (self.get_coord(arow, bcol), self.get_coord(brow, acol))

	def decipher_pair(self, a, b):
		assert a != b, 'two of the same letters occurred together, illegal in Playfair ciphertext'
		arow, acol = divmod(self.key.index(a), 5)
		brow, bcol = divmod(self.key.index(b), 5)
		if arow == brow:
			return (self.get_coord(arow , (acol - 1)%5), self.get_coord(brow , (bcol - 1)%5))
		elif acol == bcol:
			return (self.get_coord((arow - 1)%5, acol), self.get_coord((brow - 1)%5 , bcol))
		else:
			return (self.get_coord(arow , bcol), self.get_coord(brow, acol))

	def get_coord(self, x, y):
		return self.key[x*5 + y]

	def encode(self, msg):
		"""Encrypt @msg using initialised key.
		Non-alpha characters will be removed from the @msg.
		If length of msg is odd, 'X' will be appended.

		Example:
		>>> ciphertext = Playfair(key='PLAYFAIRCIPHER').encode(plaintext)

		@param msg: ASCII string to encode
		@returns: an UPPERCASE encoded string
		"""
		msg = Playfair.filter_alpha(msg)
		msg = msg.upper().replace('J', 'I')

		msg = Playfair.handle_repeated_chars(msg)

		if not Playfair.is_even_string(msg):
			msg += 'X'

		out = []
		msg_len = len(msg)
		for x in xrange(0, msg_len, 2):
			out.extend(self.encode_pair(msg[x], msg[x+1]))

		return ''.join(out)

	def decode(self, msg):
		"""Decrypt @msg using initialised key.
		Length of msg must be even, else error.

		Example:
		>>> plaintext = Playfair(key='PLAYFAIRCIPHER').decode(ciphertext)

		@param msg: Alphabetic string to decode
		@returns: an UPPERCASE decoded string
		"""
		assert msg.isalpha(), "Invalid ciphertext. Must be Alphabetic string."
		msg = msg.upper().strip()
		assert 'J' not in msg, "J is in ciphertext, invalid because J is replace by I in Playfair."
		assert Playfair.is_even_string(msg), "Invalid ciphertext. Length of ciphertext must be even."
		out = []
		msg_len = len(msg)
		for x in xrange(0, msg_len, 2):
			out.extend(self.decipher_pair(msg[x], msg[x+1]))

		return ''.join(out)

	def print_key(self):
		print('========= KEY ==========')
		# assert len(self.key) == 25
		for x in xrange(0, 25, 5):
			print(' '.join(self.key[x:x+5]))
		print('========================')

	@staticmethod
	def is_even_string(msg):
		return len(msg) & 1 == 0 # equivalent with len(2) % 1 == 0

	@staticmethod
	def handle_repeated_chars(msg):
		'''If both letters are the same, add an "X" after the first letter
		Example:
		>>> text = Playfair.handle_repeated_chars('Hidethegoldinthetreestump')
		>>> text
		'Hidethegoldinthetrexestump'
		'''
		result = []
		x = 0
		length = len(msg) - 1
		while x < length:
			if msg[x] != msg[x+1]:
				result.append(msg[x:x+2])
				x += 2
			else:
				result.append(msg[x] + 'X')
				x += 1

		# if length of msg is odd, add the last char to result
		# else msg has same letter at end with even length
		if ((length+1) & 1 == 1) or (msg[-2] == msg[-1]):
			result.append(msg[-1])
		return ''.join(result)

	@staticmethod
	def filter_alpha(text):
		result = [char for char in text if char.isalpha()]
		return ''.join(result)

	@staticmethod
	def remove_dups(oldkey):
		'''Removes duplicates element on a list but keep its order

		@param oldkey: a string, list that need to deal with
		@returns: a non-duplicated list
		'''
		newkey = list()
		seen = set()
		for char in oldkey:
			if char not in seen:
				newkey.append(char)
				seen.add(char)
		return newkey

	@staticmethod
	def key_valid(key):
		return key.isalpha()

	DEFAULT_KEY=tuple('ABCDEFGHIKLMNOPQRSTUVWXYZ') # I is same as J


def main():
	parser = argparse.ArgumentParser(description='''
Playfair Cipher -- encode, decode or crack messages.

This tool solves monoalphabetic substitution ciphers, also known as cryptograms.
These are ciphers where each letter of the clear text is replaced by a
corresponding letter of the cipher alphabet.
''', epilog="[+] Written by 15520599")
	parser.add_argument('message', help="ASCII message to be encoded, decoded.")
	parser.add_argument('-k', '--key',
		help='ASCII string used to encode/decode message. Default is PLAYFAIRCIPHER.',
		default='PLAYFAIRCIPHER')
	# Conflicting options
	conflicted_group = parser.add_mutually_exclusive_group()
	conflicted_group.add_argument('-e', '--encode', action="store_true", help="encodes the message.")
	conflicted_group.add_argument('-d', '--decode', action="store_true", help="decodes the message.")


	args = parser.parse_args()

	key = args.key

	message = args.message.strip()

	# Required arguments.
	playfairer = Playfair(key)
	if args.encode:
		playfairer.print_key()
		ciphertext = playfairer.encode(message)
		print("Encoded message: %r"%(str(ciphertext)))
		#
	elif args.decode:
		playfairer.print_key()
		plaintext = playfairer.decode(message)
		print("Decoded message: %r"%(str(plaintext)))
		#
	else:
		error("Please choose option to encode, decode the message.")


if __name__ == '__main__':
	main()

