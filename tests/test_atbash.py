#!/usr/bin/env python2

import unittest

try:
    from classical_cipher.atbash import Atbash
except ImportError:
    import sys
    import os
    sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
    from classical_cipher.atbash import Atbash


class TestAtbash(unittest.TestCase):
    def test_encode(self):
        plaintext = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ciphertext = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
        result = Atbash.encode(plaintext)
        self.assertEqual(result, ciphertext)

if __name__ == '__main__':
    unittest.main()

