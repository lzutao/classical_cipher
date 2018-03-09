#!/usr/bin/env python2
import argparse
import math
import string

def error(msg):
	import sys
	print('[!] ERROR: %s'%msg)
	print('For more, see --help')
	sys.exit(1)


class SimpleSubstitution:
	"""The Simple Substitution Cipher has a key consisting of the letters A-Z jumbled up.
	e.g. 'AJPCZWRLFBDKOTYUQGENHXMIVS'
	This cipher encrypts a letter according to the following equation:

		plaintext =  ABCDEFGHIJKLMNOPQRSTUVWXYZ
		ciphertext = AJPCZWRLFBDKOTYUQGENHXMIVS

	To convert a plaintext letter into ciphertext, read along the plaintext
	row until the desired letter is found, then substitute it with the letter
	below it.

	@param table: a permutation of the 26 characters of the alphabet.
	"""
	def __init__(self, table='AJPCZWRLFBDKOTYUQGENHXMIVS'):
		if not SimpleSubstitution.key_valid(table):
			error("Invalid key.")

		self.table = table.lower()
		self.TABLE = table.upper()

		self.uppertable = None
		self.lowertable = None

		self.invert_upper = None
		self.invert_lower = None

	@staticmethod
	def key_valid(table):
		return (len(set(table)) == 26 and table.isalpha())

	def encode(self, msg):
		"""Encrypt string using initialised table.

		Example:
		>>> ciphertext = SimpleSubstitution(key='AJPCZWRLFBDKOTYUQGENHXMIVS').encode(plaintext)

		@param msg: ASCII string to encode
		@returns: encoded string
		"""
		# map A-Z to table
		if self.uppertable is None:
			self.uppertable = dict(zip(string.uppercase, self.TABLE))
			self.lowertable = dict(zip(string.lowercase, self.table))

		ret = []
		for char in msg:
			if char.isalpha():
				tmp = self.lowertable[char] if char.islower() else self.uppertable[char]
				ret.append(tmp)
			else:
				ret.append(char)

		return ''.join(ret)

	def decode(self, msg):
		"""Decrypt string using initialised table.
		Example:
			plaintext = SimpleSubstitution('AJPCZWRLFBDKOTYUQGENHXMIVS').decode(ciphertext)

		@param msg: ASCII string to encode
		@returns: decoded string
		"""
		# Find inverse key
		if self.invert_lower is None:
			self.invert_upper = dict(zip(self.TABLE, string.uppercase))
			self.invert_lower = dict(zip(self.table, string.lowercase))

		ret = []
		for char in msg:
			if char.isalpha():
				tmp = self.invert_lower[char] if char.islower() else self.invert_upper[char]
				ret.append(tmp)
			else:
				ret.append(char)

		return ''.join(ret)

	def print_key(self):
		print('========= KEY ==========')
		print('This clear text : %s'%string.lowercase)
		print('        maps to : %s'%self.table)
		print('========================')


def main():
	parser = argparse.ArgumentParser(description='''
Simple Substitution Cipher -- encode, decode or crack messages.

This tool solves monoalphabetic substitution ciphers, also known as cryptograms.
These are ciphers where each letter of the clear text is replaced by a
corresponding letter of the cipher alphabet.
''', epilog="[+] Written by 15520599")
	parser.add_argument('message', help="ASCII message to be encoded, decoded.")
	parser.add_argument('-k', '--key',
		help='ASCII string consisting of the letters A-Z jumbled up. Default is AJPCZWRLFBDKOTYUQGENHXMIVS.',
		default='AJPCZWRLFBDKOTYUQGENHXMIVS')
	# Conflicting options
	conflicted_group = parser.add_mutually_exclusive_group()
	conflicted_group.add_argument('-e', '--encode', action="store_true", help="encodes the message.")
	conflicted_group.add_argument('-d', '--decode', action="store_true", help="decodes the message.")


	args = parser.parse_args()

	table = args.key

	if not SimpleSubstitution.key_valid(table):
		error("Invalid key. Only accept permutation of [A-Z].")

	message = args.message.strip()

	# Required arguments.
	substituter = SimpleSubstitution(table)
	if args.encode:
		substituter.print_key()
		ciphertext = substituter.encode(message)
		print("Encoded message: %r"%(ciphertext))
		#
	elif args.decode:
		substituter.print_key()
		plaintext = substituter.decode(message)
		print("Decoded message: %r"%(plaintext))
		#
	else:
		error("Please choose option to encode, decode the message.")


if __name__ == '__main__':
	main()

