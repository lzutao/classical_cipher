#!/usr/bin/env python2

import unittest
from classical_cipher.vigenere import VigenereCipher

class TestVigenereCipher(unittest.TestCase):
	def test_encode(self):
		# testcases: each is a tuple (a, key, b) where b = VigenereCipher.encode(a, key)
		testcases = [
			# Task 1.3 page 5
			(
				'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
				'GERMAN',
				'gftpesmlzvkysrfbqeyxlhwkedrncqkjxtiwqpdzocwvjfuicbpl'
			),
			(
				'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
				'CIPHERS',
				'cjrkiwyjqyrpdfqxfywkmxemfdrteltmkyalsatrfhszhaymozgo'
			),
		]

		for a, key, solution in testcases:
			result = VigenereCipher.encode(a, key)
			self.assertEqual(result, solution)

	def test_decode(self):
		# testcases: each is a tuple (a, key, b) where a = VigenereCipher.decode(b, key)
		testcases = [
			# Task 1.3 page 5
			(
				'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
				'GERMAN',
				'gftpesmlzvkysrfbqeyxlhwkedrncqkjxtiwqpdzocwvjfuicbpl',
			),
			(
				'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
				'CIPHERS',
				'cjrkiwyjqyrpdfqxfywkmxemfdrteltmkyalsatrfhszhaymozgo'
			),
		]

		for a, key, b in testcases:
			result = VigenereCipher.decode(b, key)
			self.assertEqual(result, a)


if __name__ == '__main__':
	unittest.main()

