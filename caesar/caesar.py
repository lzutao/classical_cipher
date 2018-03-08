#!/usr/bin/env python2
import argparse
import math


LOWER_A_OFFSET = ord('a')
LOWER_Z_OFFSET = ord('z')
UPPER_A_OFFSET = ord('A')
UPPER_Z_OFFSET = ord('Z')

LOWER_E_OFFSET = ord('e')

LOGA_2 = math.log(2)

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


def caesar(msg, key=13):
	"""Caesar cipher
	This cipher encrypts a letter according to the following equation::
	    c = (p + key)%26
	where c is the ciphertext letter, p the plaintext letter.

	:param msg: ASCII message to encode or decode
	:param key: shift amount (from 0-25)
	:returns: the encoded or decoded string
	"""
	p = bytearray(msg)
	out = bytearray()
	for c in p:
		if LOWER_A_OFFSET <= c and c <= LOWER_Z_OFFSET:
			out.append((c - LOWER_A_OFFSET + key)%26 + LOWER_A_OFFSET)
		elif UPPER_A_OFFSET <= c and c <= UPPER_Z_OFFSET:
			out.append((c - UPPER_A_OFFSET + key)%26 + UPPER_A_OFFSET)
		else:
			out.append(c)
	return out


def entropy_analysics(msg):
	"""Calculates the entropy of a string based on known frequency of English letters.
	Ref:
		+ https://arxiv.org/pdf/1707.08209.pdf
		+ https://en.wikipedia.org/wiki/Entropy_(information_theory)

    :param msg: ASCII string to calculate
    :returns: A float with the total entropy of the string (lower is better).
    """
	message = msg.lower()
	total = 0.0
	for char in message:
		if char.isalpha():
			total -= math.log(english_freq[char]) / LOGA_2
	return total


def crack(msg, cache={}):
	"""Attempts to crack ciphertext using frequency of letters in English.

	:param msg: ASCII string to crack
	:param cache: a dictionary to cache crack result

    :returns: a tuple of key and most likely ASCII message.
    """
	entropies = {}

	# some people try to trick me with original message
	# not the encoded message
	entropies[0] = entropy_analysics(msg)
	cache[0] = msg
	for x in xrange(1,26):
		ciphertext = str(caesar(msg=msg, key=x))
		entropies[x] = entropy_analysics(ciphertext)
		cache[x] = ciphertext
	# outloop

	lowest_entropy_index = sorted(entropies, key=entropies.get)[0]

	return (lowest_entropy_index, cache[lowest_entropy_index])


def main():
	parser = argparse.ArgumentParser(description='Caesar Cipher - encode, decode or crack messages.',
		epilog="[+] Written by 15520599")
	parser.add_argument('message', help="ASCII message to be encoded, decoded or cracked.")
	# Conflicting options
	conflic_group = parser.add_mutually_exclusive_group()
	conflic_group.add_argument('-e', '--encode', action="store_true", help="encodes this message.")
	conflic_group.add_argument('-d', '--decode', action="store_true", help="decodes this message.")
	conflic_group.add_argument('-c', '--crack',  action="store_true", help="Crack this ciphertext to find most likely message in English.")
	#
	parser.add_argument('-k', '--key', type=int, choices=range(1,26),
		help='Integer from 1 to 25 to encode/decode the message. Default is 13 and this encoding/decoding called ROT13.',
		default=13)


	args = parser.parse_args()

	# Required arguments.
	if args.encode is True:
		ciphertext = caesar(args.message, args.key)
		print('key = %r'%args.key)
		print("Encoded message: %r"%(str(ciphertext)))
		#
	elif args.decode is True:
		plaintext = caesar(args.message, 26 - args.key)
		print('key = %r'%args.key)
		print("Decoded message: %r"%(str(plaintext)))
		#
	elif args.crack is True:
		cache = {}
		key, msg = crack(args.message, cache=cache)
		print("="*80)
		print("KEY: %d"%key)
		print('Most likely message: %r'%msg)
		print("="*80)
		yes = raw_input("[+] Continue to bruteforce (y/n)? ")
		if yes == 'y':
			for x in xrange(0,26):
				print("KEY =%4d"%x)
				print('Message: %r'%cache[x])
				print('='*40)


if __name__ == '__main__':
	main()

