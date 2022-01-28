'''
Date: 2022.01.26 15:28:36
Description: 维吉尼亚密码
LastEditors: Rustle Karl
LastEditTime: 2022.01.26 15:46:11
'''

from typing import List


def e(x: int, K: int) -> int:
    return(x+K) % 26


def d(y: int, K: int) -> int:
    return (y-K) % 26


def encrypt(chars: str, K: List[int]) -> str:
    e_chars = ''

    for i in range(len(chars)):
        e_chars += chr(e(ord(chars[i])-ord('A'), K[i])+ord('A'))

    return e_chars


def decrypt(chars: str, K: List[int]) -> str:
    d_chars = ''

    for i in range(len(chars)):
        d_chars += chr(d(ord(chars[i])-ord('A'), K[i])+ord('A'))

    return d_chars


K = [12, 13, 14, 15]
e_chars = encrypt('JUST', K)
d_chars = decrypt(e_chars, K)
