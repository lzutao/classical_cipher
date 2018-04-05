#!/usr/bin/env python2
import argparse
import math


def error(msg):
	import sys
	print('[!] ERROR: %s'%msg)
	print('For more, see --help')
	sys.exit(1)

class CaesarCipher():
	"""Caesar cipher
	This cipher encrypts a letter according to the following equation::
		c = (p + key)%26
	where c is the ciphertext letter, p the plaintext letter.

	Example:
	>>> ciphertext = CaesarCipher.encode(plaintext, key)
	>>> plaintext = CaesarCipher.decode(ciphertext, key)
	"""
	@staticmethod
	def encode(msg, key=13):
		"""encodes the message

		@param msg: ASCII message to encode
		@param key: shift amount from 1-25
		@returns: encoded string
		"""
		message = bytearray(msg)
		result = bytearray()
		for char in message:
			result.append(CaesarCipher.caesar(char, key))

		return str(result)

	@staticmethod
	def decode(msg, key=13):
		"""decodes the message

		@param msg: ASCII message to decode
		@param key: shift amount from 1-25
		@returns: decoded string
		"""
		return CaesarCipher.encode(msg, 26-key)

	@staticmethod
	def __isupper(b):
		return (CaesarCipher.LOWER_A_OFFSET <= b) and (b <= CaesarCipher.LOWER_Z_OFFSET)

	@staticmethod
	def __islower(b):
		return (CaesarCipher.UPPER_A_OFFSET <= b) and (b <= CaesarCipher.UPPER_Z_OFFSET)

	@staticmethod
	def __translate(b, offset, key):
		return (b - offset + key)%26 + offset

	@staticmethod
	def caesar(char, key):
		"""caesar(bytes('a'), 3) -> bytes('d')

		@param char: a bytes to shitf
		@param key: amount to shift

		@returns: a shifted bytes
		"""
		result = char
		if CaesarCipher.__isupper(char):
			result = CaesarCipher.__translate(char, CaesarCipher.LOWER_A_OFFSET, key)
		elif CaesarCipher.__islower(char):
			result = CaesarCipher.__translate(char, CaesarCipher.UPPER_A_OFFSET, key)
		return result

	@staticmethod
	def entropy_analysics(msg):
		"""Calculates the entropy of a string based on known frequency of English letters.
		Ref:
			+ https://arxiv.org/pdf/1707.08209.pdf
			+ https://en.wikipedia.org/wiki/Entropy_(information_theory)

		@param msg: ASCII string to calculate
		@returns: A float with the total entropy of the string (lower is better).
		"""
		message = msg.lower()
		total = 0.0
		# calculate log(x, base=2)
		for char in message:
			if char.isalpha():
				total -= math.log(CaesarCipher.english_freq[char], 2)
		return total

	@staticmethod
	def crack(msg, cache=None):
		"""Attempts to crack ciphertext using frequency of letters in English.

		@param msg: ASCII string to crack
		@param cache: a dictionary to cache crack result

		@returns: a tuple of key and most likely ASCII message.
		"""
		if cache is None:
			cache = {}

		entropies = {}

		# some people try to trick me with original message
		# not the encoded message
		entropies[0] = CaesarCipher.entropy_analysics(msg)
		cache[0] = msg
		for x in xrange(1,26):
			ciphertext = CaesarCipher.decode(msg, x)
			entropies[x] = CaesarCipher.entropy_analysics(ciphertext)
			cache[x] = ciphertext
		# outloop

		lowest_entropy_index = sorted(entropies, key=entropies.get)[0]

		return (lowest_entropy_index, cache[lowest_entropy_index])


	LOWER_A_OFFSET = ord('a')
	LOWER_Z_OFFSET = ord('z')
	UPPER_A_OFFSET = ord('A')
	UPPER_Z_OFFSET = ord('Z')

	LOWER_E_OFFSET = ord('e')

	# Relative frequencies of letters in the English language
	# Ref: https://en.wikipedia.org/wiki/Letter_frequency
	english_freq = {
		'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
		'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
		'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
		'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
		'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
		'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
		'y': 0.01974, 'z': 0.00074,
	}


def main():
	parser = argparse.ArgumentParser(description='Caesar Cipher - encode, decode or crack messages.',
		epilog="[+] Written by 15520599")
	parser.add_argument('message', help="ASCII message to be encoded, decoded or cracked.")
	parser.add_argument('-k', '--key', type=int,
		help='Integer from 1 to 25 to encode/decode the message. Default is 13.',
		default=13)
	# Conflicting options
	conflicted_group = parser.add_mutually_exclusive_group()
	conflicted_group.add_argument('-e', '--encode', action="store_true", help="encodes the message.")
	conflicted_group.add_argument('-d', '--decode', action="store_true", help="decodes the message.")
	conflicted_group.add_argument('-c', '--crack',  action="store_true", help="Crack ciphertext to find most likely message in English.")


	args = parser.parse_args()
	message = args.message.strip()
	key = args.key % 26

	# Required arguments.
	if args.encode:
		ciphertext = CaesarCipher.encode(message, key)
		print('KEY = %d'%key)
		print("Encoded message: %r"%ciphertext)
		#
	elif args.decode:
		plaintext = CaesarCipher.decode(message, key)
		print('KEY = %d'%key)
		print("Decoded message: %r"%plaintext)
		#
	elif args.crack:
		cache = {}
		key, msg = CaesarCipher.crack(message, cache=cache)
		print("="*80)
		print("KEY = %d"%key)
		print('Most likely message: %r'%msg)
		print("="*80)
		yes = raw_input("[+] Continue to bruteforce (y/N)? ")
		if yes == 'y':
			for x in xrange(0,26):
				print("KEY =%4d"%x)
				print('Message: %r'%cache[x])
				print('='*40)
	else:
		error("Please choose option to encode, decode or crack.")


if __name__ == '__main__':
	main()

