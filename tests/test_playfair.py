#!/usr/bin/env python2
import unittest

try:
    from classical_cipher.playfair import Playfair
except ImportError:
    from . import context
    from classical_cipher.playfair import Playfair


class TestPlayfair(unittest.TestCase):
    def test_encode(self):
        # test odd length string
        plaintext = 'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXY'
        keys = (
            'CZBNIWEMUORKPDSLQFXAGTHYV',
            'OHNUWKDBTIEPYZXCSQAMLGRVF',
            'PSLQOFAIYMCNWTUHDXEZBKGRV',
            'XQVLPNAKRSEWFCYHUTDBGZIOM',
            'XBHPUVMIYESDNWLAKCRGFZOTQ',
        )
        ciphertexts = (
            'FINRMQTYZSFWIUKFKRYEGOYNIQNZKULHVBRQUBMSLKKVOYULNY',
            'QTSKXLHDKDFCUHYSGQZTFUEZAVKQKPLRWDEOQWHERNADTUIMZE',
            'FKNHHYBXAGOIUSSOKQUCGUEIDMPHXZIBXFGSAUPSYQQNZOXGIE',
            'SUDOWCXGVFPORGXVSNDTQFPEQWDYHCEITGRVGSMLLAKBTQEQEP',
            'KXKNVQCUMCDECHUTAWQPYSPVFKHKLMQAINGDIDTHTGWFXESPVP',
        )

        for key, ciphertext in zip(keys, ciphertexts):
            result = Playfair(key=key).encode(plaintext)
            self.assertEqual(result, ciphertext)

        # test even length string
        plaintext ='aaaaaaaaajjjjjkkkkkllllmmmmnnnnffffooooossssoffffffe'
        key = 'tpaydcmhfoizwsuvxrbkelqgn'
        ciphertext = 'PRPRPRPRPRPRPRPRTWZVZVZVUVVRVRVRXNPLPLPZZLZLOLLKLKGOMBMBOCMKMKMKFUZBZBUFMBMBMBMBMBCG'
        result = Playfair(key=key).encode(plaintext)
        self.assertEqual(result, ciphertext)

    def test_decode(self):
        ciphertext = 'abcdefghiklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWXYZ'
        keys = (
            'lsfdpxwirnyveamoqgkchbtzu',
            'dytqplngirabskxcvoemzufwh',
            'ecsyinfmkpdrtuvgwqzbolaxh',
            'xquwfstzgeipboalykdnvrmch',
            'bxuthifmzrweasdovlpgcqnyk',
        )
        plaintexts = (
            'VZKPITOTRGPYXCSCWDBZWSLXKRUQFATETXODNPCLKWFBBMXNAH',
            'XAAZOWRFQIRCGVQTGXYFEUBPCLAVQCOTWRAIVRMTPIGFVBHKDU',
            'HQERCNBOYPAFEGMBTCRTRBZXQXWINONWBHFXFPHNWTAMTUZLXU',
            'OPDOFHECBLKVDATRVTZQCXQLEBOMNGWEVAYNHKBIRYESXMUFKT',
            'WUKWFXDKRCAUCLVYZDUXOETQMSCOSWRVBRNGULGLKFZYXLEBPT',
        )

        for key, plaintext in zip(keys, plaintexts):
            result = Playfair(key=key).decode(ciphertext)
            self.assertEqual(result, plaintext)


if __name__ == '__main__':
    unittest.main()

