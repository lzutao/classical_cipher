#!/usr/bin/env python2
import argparse
import string

def error(msg):
	import sys
	print('[!] ERROR: %s'%msg)
	print('For more, see --help')
	sys.exit(1)


class Atbash():
	"""The Atbash Cipher is a type of monoalphabetic cipher by
	taking the alphabet and mapping it to its reverse,

	This tool encrypts a letter according to the following equation:

		plaintext =  ABCDEFGHIJKLMNOPQRSTUVWXYZ,
		ciphertext = ZYXWVUTSRQPONMLKJIHGFEDCBA.

	For more, see [https://en.wikipedia.org/wiki/Atbash].
	"""

	@staticmethod
	def encode(msg):
		"""Encrypt string

		Example:
		>>> ciphertext = Atbash.encode(plaintext)

		@param msg: ASCII string to encode
		@returns: encoded string
		"""
		return string.translate(msg, Atbash.TRANS)

	@staticmethod
	def decode(msg):
		"""Decrypt string
		Example:
			plaintext = Atbash.decode(ciphertext)

		@param msg: ASCII string to encode
		@returns: decoded string
		"""
		return Atbash.encode(msg)

	TRANS = string.maketrans(string.ascii_letters, string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1])


def main():
	parser = argparse.ArgumentParser(description=Atbash.__doc__, epilog="[+] Written by 15520599")
	parser.add_argument('message', help="ASCII message to be encoded, decoded.")

	# Conflicting options
	conflicted_group = parser.add_mutually_exclusive_group()
	conflicted_group.add_argument('-e', '--encode', action="store_true", help="encodes the message.")
	conflicted_group.add_argument('-d', '--decode', action="store_true", help="decodes the message.")


	args = parser.parse_args()

	message = args.message.strip()

	# Required arguments.
	if args.encode:
		ciphertext = Atbash.encode(message)
		print("Encoded message: %r"%(ciphertext))
		#
	elif args.decode:
		plaintext = Atbash.decode(message)
		print("Decoded message: %r"%(plaintext))
		#
	else:
		error("Please choose option to encode, decode the message.")


if __name__ == '__main__':
	main()

