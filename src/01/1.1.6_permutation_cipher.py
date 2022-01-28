'''
Date: 2022.01.26 16:58:57
Description: Omit
LastEditors: Rustle Karl
LastEditTime: 2022.01.26 17:12:12
'''
from random import shuffle

chars = 'SHIFTCIPHER'

origin = list(range(len(chars)))
origin_shuffle = origin[:]
shuffle(origin)

pi = dict(zip(origin, origin_shuffle))
pi_inverse = dict(zip(origin_shuffle, origin))


def e(x):
    return pi[x]


def d(y):
    return pi_inverse[y]


def encrypt(chars: str) -> str:
    e_chars = list(chars)

    for i in range(len(chars)):
        e_chars[e(i)] = chars[i]

    return ''.join(e_chars)


def decrypt(chars: str) -> str:
    d_chars = list(chars)

    for i in range(len(chars)):
        d_chars[d(i)] = chars[i]

    return ''.join(d_chars)


e_chars = encrypt(chars)
d_chars = decrypt(e_chars)
