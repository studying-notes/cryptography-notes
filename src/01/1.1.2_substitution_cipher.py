'''
Date: 2022.01.26 14:30:49
Description: 代换密码
LastEditors: Rustle Karl
LastEditTime: 2022.01.26 14:41:33
'''
from string import ascii_uppercase
from random import shuffle


ascii_uppercase = list(ascii_uppercase)
ascii_uppercase_shuffle = ascii_uppercase[:]
shuffle(ascii_uppercase_shuffle)

pi = dict(zip(ascii_uppercase, ascii_uppercase_shuffle))
pi_inverse = dict(zip(ascii_uppercase_shuffle, ascii_uppercase))


def e(x):
    return pi[x]


def d(y):
    return pi_inverse[y]


d(e('A'))


def encrypt(chars) -> str:
    e_chars = ''

    for char in chars.upper():
        e_chars += e(char)

    return e_chars
    # return ''.join(e(char) for char in chars.upper())


def decrypt(chars: str) -> str:
    d_chars = ''

    for char in chars.upper():
        d_chars += d(char)

    return d_chars


e_chars = encrypt('SHIFTCIPHER')
d_chars = decrypt(e_chars)
