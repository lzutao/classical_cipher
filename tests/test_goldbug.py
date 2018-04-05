#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest

try:
    from classical_cipher.goldbug import GoldbugCipher
except ImportError:
    import sys
    import os
    sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
    from classical_cipher.goldbug import GoldbugCipher


class TestGoldbugCipher(unittest.TestCase):
    def test_decode(self):
        plaintexts = [
            u"agoodglassinthebishopshostelinthede",
            u'vilsseattwentyonedegreesandthirteenmi',
        ]

        ciphertexts = [
            u'53‡‡†305))6*;4826)4‡.)4‡);806*;48†8',
            u'¶60))85;;]8*;:‡*8†83(88)5*†;46(;88*96',
        ]

        for plaintext, ciphertext in zip(plaintexts, ciphertexts):
            msg = GoldbugCipher.encode(plaintext)
            self.assertEqual(msg, ciphertext)

    def test_decode(self):
        plaintexts = [
            u"nutesnortheastandbynorthmainbranchse",
            u'venthlimbeastsideshootfromthelefteyeo',
        ]

        ciphertexts = [
            u'*?;8)*‡(;485);5*†2:*‡(;4956*2(5*-4)8',
            u'¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡',
        ]

        for plaintext, ciphertext in zip(plaintexts, ciphertexts):
            msg = GoldbugCipher.decode(ciphertext)
            self.assertEqual(msg, plaintext)


if __name__ == '__main__':
    unittest.main()

