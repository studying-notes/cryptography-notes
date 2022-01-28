'''
Date: 2022.01.26 14:05:25
Description: 移位密码
LastEditors: Rustle Karl
LastEditTime: 2022.01.26 14:29:36
'''

# 模的算术运算

# 0<=K<=25


def e(x: int, K: int) -> int:
    return(x+K) % 26


def d(y: int, K: int) -> int:
    return (y-K) % 26


K = 12

d(e(10, K), K)


def encrypt(chars: str, K: int) -> str:
    e_chars = ''

    for char in chars.upper():
        e_chars += chr(e(ord(char)-ord('A'), K)+ord('A'))

    return e_chars


def decrypt(chars: str, K: int) -> str:
    d_chars = ''

    for char in chars.upper():
        d_chars += chr(d(ord(char)-ord('A'), K)+ord('A'))

    return d_chars


K = 12
e_chars = encrypt('SHIFTCIPHER', K)
d_chars = decrypt(e_chars, K)


# 密钥穷尽搜索方法破译

# e_chars = 'JBCRCLQRWCRVNBJENBWRWN'
e_chars = 'BEEAKFYDJXUQYHYJIORYHTYJIQFBQDUYJIIKFUHCQD'

# LOOKUPINTHEAIRITSYBIRDITSAPLANEITSSUPERMAN

for i in range(26):
    print(decrypt(e_chars, i))

# 哪个字符串有意义哪个就是明文

import wordninja

wordninja.split('LOOKUPINTHEAIRITSYBIRDITSAPLANEITSSUPERMAN')