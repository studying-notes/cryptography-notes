'''
Date: 2022.01.26 13:25:27
Description: Omit
LastEditors: Rustle Karl
LastEditTime: 2022.01.28 13:23:13
'''

from PIL import Image

stem = '算法5.4_RSA参数生成_1'

raw = Image.open(f"assets/images/{stem}.png")

w, h = raw.size

p1 = raw.crop((0, 0, w, 150))
p1.show()

p2 = raw.crop((0, 420, w, h))
p2.show()

new = Image.new('RGB', (w, p1.size[1]+p2.size[1]), (255, 255, 255))


new.paste(p1)
new.paste(p2, (0, p1.size[1]))
new.show()

new.save(f"assets/images/{stem[:-2]}.png")
