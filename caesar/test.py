#!/usr/bin/env python2

import unittest
import caesar


class TestCaesar(unittest.TestCase):
	def test_caesar(self):
		# testcases: each is a tuple (a, k, b) where caesar.caesar(a, k) = b
		testcases = [
			# Task 1.3 page 5
			(
				'Gurer ner gjb xvaqf bs crbcyr va guvf jbeyq: gubfr jub ner ybbxvat sbe n ernfba naq gubfr jub ner svaqvat fhpprff. Gubfr jub ner ybbxvat sbe n ernfba nyjnlf frrxvat gur ernfbaf jul gur jbex vf abg svavfurq. Naq crbcyr jub svaq fhpprff ner nyjnlf ybbxvat sbe ernfbaf jul gur jbex pna or pbzcyrgrq.',
				13,
				'There are two kinds of people in this world: those who are looking for a reason and those who are finding success. Those who are looking for a reason always seeking the reasons why the work is not finished. And people who find success are always looking for reasons why the work can be completed.'
			),
			(
				'That\'s the never ending story of Robert.',
				11,
				"Esle'd esp ypgpc pyotyr dezcj zq Czmpce."
			),
		]

		for a, k, solution in testcases:
			result = caesar.caesar(a, k)
			self.assertEqual(result, solution)


	def test_entropy_analysics(self):
		# testcases: each is a tuple (msg, e) where e = caesar.entropy_analysics(msg)
		testcases = [
			('Accepts messages', 62.594804275),
			('That\'s the never ending story of Robert.', 128.908800926),
		]
		for msg, e in testcases:
			result = caesar.entropy_analysics(msg)
			self.assertAlmostEqual(result, e)


	def test_crack(self):
		plaintext = 'There are two kinds of people in this world: those who are looking for a reason and those who are finding success. Those who are looking for a reason always seeking the reasons why the work is not finished. And people who find success are always looking for reasons why the work can be completed.'
		ciphertext = 'Gurer ner gjb xvaqf bs crbcyr va guvf jbeyq: gubfr jub ner ybbxvat sbe n ernfba naq gubfr jub ner svaqvat fhpprff. Gubfr jub ner ybbxvat sbe n ernfba nyjnlf frrxvat gur ernfbaf jul gur jbex vf abg svavfurq. Naq crbcyr jub svaq fhpprff ner nyjnlf ybbxvat sbe ernfbaf jul gur jbex pna or pbzcyrgrq.'
		cache = {}
		key, msg = caesar.crack(ciphertext, cache)
		self.assertEqual(msg, plaintext)


if __name__ == '__main__':
	unittest.main()

