#!/usr/bin/env python2

import unittest
try:
    from classical_cipher.substitution import SimpleSubstitution
except ImportError:
    import sys
    import os
    sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
    from classical_cipher.substitution import SimpleSubstitution

class TestSimpleSubstitution(unittest.TestCase):
    def test_encode(self):
        # testcases: each is a tuple (a, k, b) where b = SimpleSubstitution(k).encode(a)
        testcases = [
            # Task 1.3 page 5
            (
                'The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it. -- Terry Pratchett',
                'wisdomabcnxghjklepqrtuvzyf',
                'Rbo rpktigo vcrb bwucja wj kloj hcjd, km sktpqo, cq rbwr loklgo vcgg cjqcqr kj skhcja wgkja wjd rpycja rk ltr rbcjaq cj cr. -- Roppy Lpwrsborr',
            ),
        ]

        for a, k, solution in testcases:
            result = SimpleSubstitution(k).encode(a)
            self.assertEqual(result, solution)


    def test_decode(self):
        # testcases: each is a tuple (a, k, b) where b = SimpleSubstitution(k).decode(a)
        testcases = [
            # Task 1.3 page 5
            (
                'Rbo rpktigo vcrb bwucja wj kloj hcjd, km sktpqo, cq rbwr loklgo vcgg cjqcqr kj skhcja wgkja wjd rpycja rk ltr rbcjaq cj cr. -- Roppy Lpwrsborr',
                'wisdomabcnxghjklepqrtuvzyf',
                'The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it. -- Terry Pratchett',
            ),
        ]

        for a, k, solution in testcases:
            result = SimpleSubstitution(k).decode(a)
            self.assertEqual(result, solution)


if __name__ == '__main__':
    unittest.main()

