'''
Date: 2022.01.27 17:36
Description: Omit
LastEditors: Rustle Karl
LastEditTime: 2022.01.27 17:36
'''


def z(i):
    '''线性递归关系产生密钥流'''
    assert i >= 0

    if i < 4:
        return [1, 0, 0, 0][i]

    return (z(i - 4) + z(i - 3)) % 2


assert z(4) == 1
assert z(5) == 0
assert z(6) == 0


# 自动密钥密码


def e(x, z):
    return (x + z) % 26


def d(y, z):
    return (y - z) % 26


def encrypt(chars: str, K: int) -> str:
    e_chars = ''

    for i in range(len(chars)):
        e_chars += chr(e(ord(chars[i]) - ord('A'), ord(chars[i - 1]) - ord('A') if i > 0 else K) + ord('A'))

    return e_chars


def decrypt(chars: str, K: int) -> str:
    d_chars = ''

    for i in range(len(chars)):
        # 每次获得下一个明文字母，用它作为下一个密钥流元素。
        K = d(ord(chars[i]) - ord('A'), K)
        d_chars += chr(K + ord('A'))

    return d_chars


K = 12
e_chars = encrypt('SHIFTCIPHER', K)
d_chars = decrypt(e_chars, K)
