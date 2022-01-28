'''
Date: 2022.01.26 15:50:57
Description: 希尔密码
LastEditors: Rustle Karl
LastEditTime: 2022.01.26 16:54:30
'''
import sympy

K = sympy.Matrix([
    [10, 5, 12],
    [3, 14, 21],
    [8, 9, 11],
])

K_inverse = K.inv()


def e(x):
    return x*K


def d(y):
    return (y*K_inverse)[0, 0]


d(e(24))
