'''
Date: 2022.01.26 15:01:37
Description: 仿射密码
LastEditors: Rustle Karl
LastEditTime: 2022.01.26 15:27:13
'''

from math import gcd


def get_multiplicative_inverse(a):
    '''求乘法逆，这里只是简单列举'''
    return {
        1: 1,
        3: 9, 9: 3,
        5: 21, 21: 5,
        7: 15, 15: 7,
        11: 19, 19: 11,
        17: 23, 23: 17,
        25: 25
    }[a]


def e(x: int, a: int, b: int) -> int:
    if gcd(a, 26) != 1:  # 最大公约数
        raise ValueError

    # 唯一解充分必要条件 gcd(a, 26)=1
    return (a*x+b) % 26


def d(y: int, a: int, b: int) -> int:
    return get_multiplicative_inverse(a)*(y-b) % 26


def encrypt(chars: str, a: int, b: int) -> str:
    e_chars = ''

    for char in chars.upper():
        e_chars += chr(e(ord(char)-ord('A'), a, b)+ord('A'))

    return e_chars


def decrypt(chars: str, a: int, b: int) -> str:
    d_chars = ''

    for char in chars.upper():
        d_chars += chr(d(ord(char)-ord('A'), a, b)+ord('A'))

    return d_chars


a, b = 11, 4
e_chars = encrypt('SHIFTCIPHER', a, b)
d_chars = decrypt(e_chars, a, b)
