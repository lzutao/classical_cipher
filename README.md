# classical_cipher

[![Build Status][travis_status]][travis_repo]

[travis_status]: https://travis-ci.com/lzutao/classical_cipher.svg?branch=master
[travis_repo]: https://travis-ci.com/lzutao/classical_cipher

A Python package and command line script for encoding,
decoding with classical cipher such as Caesar Cipher,
Vigenere Cipher, Affine Cipher, Playfair, etc

## Features

- Encoding
- Decoding
- Command line interface
- Test suite
- Only python2 supported

## Installation

The latest version can be downloaded via `github`.

```bash
git clone --depth 1 https://github.com/lzutao/classical_cipher
cd classical_cipher
```

To install to your local home folder:

```bash
python setup.py install --user
```

Or you want to install system wide:

```bash
python setup.py install
```

Else want to install in `development mode`, you may use `--user` flag to
only install in your home

```bash
python setup.py.py develop
```

## Usage

If you get some error such as `ValueError: Attempted relative import in non-package`.
You should try to run it as module instead of a single python file:

```bash
cd /path/to/classical_cipher
python -m classical_cipher/vigenere/vigenere
```

Note that you should use `classical_cipher/vigenere/vigenere` instead of
`classical_cipher/vigenere/vigenere.py`

Replace `vigenere` with other tools if needed.

## Testing

Use the following command to test:

```bash
python setup.py test
```

## Meta

- Written by @lzutao
- Released under [MIT License](LICENSE)
- Software is as is - no warranty expressed or implied.
