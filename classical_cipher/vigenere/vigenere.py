#!/usr/bin/env python2
import argparse
import math
import itertools

try:
    from classical_cipher.caesar import CaesarCipher
except ImportError:
    import sys
    import os
    sys.path.append( os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) ) )
    from caesar import CaesarCipher

def error(msg):
    import sys
    print('[!] ERROR: %s'%msg)
    print('For more, see --help')
    sys.exit(1)


class VigenereCipher():
    """Vigenere cipher class
    This cipher encrypts a letter according to the following equation::
        c[i] = (p[i] + key[i % m]) % 26
    where c is the ciphertext,
          p the plaintext,
          m = len(key).

    Example:
    >>> ciphertext = VigenereCipher.encode(plaintext, key)
    >>> plaintext = VigenereCipher.decode(ciphertext, key)
    """
    @staticmethod
    def encode(msg, key='VIGENERE', key_valid=False):
        '''encodes the message

        @param msg: ASCII message to encode
        @param key: Only alpha string, no punctuation and space
        @param key_valid: if True, skip checking key

        @returns: encoded string
        '''
        if not key_valid and not VigenereCipher.key_valid(key):
            error("Invalid key")

        message = bytearray(msg)
        shifts = VigenereCipher.__createShiftArray(key)
        result = VigenereCipher.__shift(message, shifts)
        return str(result)

    @staticmethod
    def decode(msg, key='VIGENERE', key_valid=False):
        '''decodes the message

        @param msg: ASCII message to decode
        @param key: Only alpha string, no punctuation and space
        @param key_valid: if True, skip checking key

        @returns: decoded string
        '''
        if not key_valid and not VigenereCipher.key_valid(key):
            error("Invalid key")

        message = bytearray(msg)
        shifts = [-x for x in VigenereCipher.__createShiftArray(key)] # create invert shift key
        result = VigenereCipher.__shift(message, shifts)
        return str(result)

    @staticmethod
    def __shift(msg, shifts):
        '''
        @param msg: bytearray want to shift
        @param shifts: an bytearray contains amounts to shift
        @returns: an shitfed bytearray
        '''
        shifts = itertools.cycle(shifts) # cycle('ABCD') --> A B C D A B C D

        result = bytearray()
        for char, k in zip(msg, shifts):
            result.append(CaesarCipher.caesar(char, k))
        return result

    @staticmethod
    def key_valid(key):
        return (len(key) > 0 and key.isalpha())

    @staticmethod
    def __createShiftArray(key):
        '''
        @param key: Must be valid key
        @returns: an array represents amount to shift according to key
        '''
        shifts = []
        for char in key:
            charcase = VigenereCipher.UPPER_A_OFFSET if char.isupper() else VigenereCipher.LOWER_A_OFFSET
            shifts.append(ord(char) - charcase)
        return shifts

    # static variables
    LOWER_A_OFFSET = ord('a')
    UPPER_A_OFFSET = ord('A')


def main():
    parser = argparse.ArgumentParser(description='Vigenere Cipher - encode, decode messages polyalphabetic cipher.',
        epilog="[+] Written by 15520599")
    parser.add_argument('message', help="ASCII message to be encoded, decoded. Note that also accepts space character.")
    parser.add_argument('-k', '--key',
        help='ASCII string consists of alphabetical characters only, no punctuation or number. Default is VIGENERE',
        default='VIGENERE')
    # Conflicting options
    conflicted_group = parser.add_mutually_exclusive_group()
    conflicted_group.add_argument('-e', '--encode', action="store_true", help="encodes the message.")
    conflicted_group.add_argument('-d', '--decode', action="store_true", help="decodes the message.")

    args = parser.parse_args()
    message = args.message.strip()
    key = ''.join(args.key.upper().split()) # split to remove all whitespace include tabs, newlines

    if not VigenereCipher.key_valid(key):
        error("Invalid key. Only accept strings consist of [A-Z].")
        return 1

    # Required arguments.
    if args.encode:
        ciphertext = VigenereCipher.encode(message, key, True)
        print('KEY = %s'%key)
        print("Encoded message: %r"%(ciphertext))
        #
    elif args.decode:
        plaintext = VigenereCipher.decode(message, key, True)
        print('KEY = %s'%key)
        print("Decoded message: %r"%(plaintext))
        #
    else:
        error("Please choose option to encode, decode.")


if __name__ == '__main__':
    main()

