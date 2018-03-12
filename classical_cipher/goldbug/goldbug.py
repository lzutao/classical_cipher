#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import argparse
import math
import itertools

def error(msg):
	import sys
	print('[!] ERROR: %s'%msg)
	print('For more, see --help')
	sys.exit(1)


class GoldbugCipher():
	"""Goldbug Cipher class

	The Goldbug cipher has included in a short story by Edgar Allan Poe
	and which was published in 1843. It tells the tail of William Legrand
	and how he was bitten by a gold-colored bug. The mapping is:

		abcdefghijklmnopqrstuvwxyz
		52-†81346,709*‡.$();?¶]¢:[

	Example:
	>>> ciphertext = GoldbugCipher.encode(plaintext)
	>>> plaintext = GoldbugCipher.decode(ciphertext)
	"""
	@staticmethod
	def encode(msg):
		'''encodes the message

		@param msg: Unicode message to encode
		@returns: encoded string
		'''
		msg = GoldbugCipher.filter_alpha(msg).lower().replace(' ', '')
		return GoldbugCipher.__encode(msg, GoldbugCipher.MAPPING)

	@staticmethod
	def decode(msg):
		'''decodes the message

		@param msg: Unicode message to decode
		@returns: decoded string
		'''
		for char in msg:
			assert char in GoldbugCipher.GOLDBUG_CHARS, 'Invalid char %s in ciphertext'%char.encode('utf-8')
		return GoldbugCipher.__encode(msg, GoldbugCipher.INVERT_MAPPING)

	@staticmethod
	def __encode(msg, mapping):
		result = []
		for char in msg:
			result.append(mapping[char])
		return ''.join(result)

	@staticmethod
	def filter_alpha(text):
		result = [char for char in text if char.isalpha()]
		return ''.join(result)

	GOLDBUG_CHARS = u'52-†81346,709*‡.$();?¶]¢:['
	LOWERCASE = u'abcdefghijklmnopqrstuvwxyz'

	MAPPING = dict(zip(LOWERCASE, GOLDBUG_CHARS))
	INVERT_MAPPING = dict(zip(GOLDBUG_CHARS, LOWERCASE))

def main():
	parser = argparse.ArgumentParser(
		description='''The Gold-Bug cipher has included in a short story
		by Edgar Allan Poe and which was published in 1843.''',
		epilog="[+] Written by 15520599")
	parser.add_argument('message', help="Unicode message to be encoded, decoded. Note that also accepts space character.")

	# Conflicting options
	conflicted_group = parser.add_mutually_exclusive_group()
	conflicted_group.add_argument('-e', '--encode', action="store_true", help="encodes the message.")
	conflicted_group.add_argument('-d', '--decode', action="store_true", help="decodes the message.")

	args = parser.parse_args()
	message = args.message.strip()

	# Required arguments.
	if args.encode:
		ciphertext = GoldbugCipher.encode(message)
		print("Encoded message: %r"%ciphertext.encode('utf-8'))
		#
	elif args.decode:
		plaintext = GoldbugCipher.decode(message)
		print("Decoded message: %r"%plaintext.encode('utf-8'))
		#
	else:
		error("Please choose option to encode, decode.")


if __name__ == '__main__':
	main()

