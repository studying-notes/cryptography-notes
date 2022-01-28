'''
Date: 2022.01.27 21:24
Description: Omit
LastEditors: Rustle Karl
LastEditTime: 2022.01.27 21:24
'''
from collections import Counter
from io import StringIO


def get_sorted_elements_list(text: str) -> list:
    '''
    获取编码表

    {'A': 10, 'B': 15, 'C': 25, 'D': 50} -> [((((((('A', 10), ('B', 15)), 25), ('C', 25)), 50), ('D', 50)), 100)]
    '''
    words = Counter(text)

    # Sort elements by probability of occurrence
    # m = sorted(words.items(), key=lambda x: x[1], reverse=True)
    m = words.most_common()

    while True:
        if len(m) < 2:
            break

        x = m.pop()
        y = m.pop()

        # The two elements with the smallest probability are combined into one element,
        # and the sum of these two probabilities is used as the probability of the new element
        m.append(((x, y), x[1] + y[1]))

        j = -1
        # Sort by element probability again
        for i in range(len(m) - 2, -1, -1):
            if m[i][1] < m[j][1]:
                m[i], m[j] = m[j], m[i]
                j = i
            else:
                break

    return m


def flatten_elements_list(m, x=''):
    '''将编码表解析成一对一的字符编码映射表'''
    for i in m[0]:
        if not isinstance(i[0], str):
            yield from flatten_elements_list(i, x + str(m[0].index(i)))
        else:
            yield i[0], x + str(m[0].index(i))


# 编解码成字符串方便演示，实际应该编解码成二进制

def encode(flatten_elements, text: str) -> str:
    buf = StringIO()

    for char in text:
        buf.write(flatten_elements[char])

    return buf.getvalue()


def decode(sorted_elements, text: str) -> str:
    buf = StringIO()

    m = sorted_elements[0]
    for i in map(int, list(text)):
        m = m[0][i]
        if len(m[0]) == 1:
            buf.write(m[0])
            m = sorted_elements[0]

    return buf.getvalue()


if __name__ == '__main__':
    text = '''
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    '''

    sorted_elements = get_sorted_elements_list(text)
    flatten_elements = dict(flatten_elements_list(sorted_elements[0]))

    e = encode(flatten_elements, text)
    d = decode(sorted_elements, e)
