#!/usr/bin/env python

from PIL import Image


def simple_quant():
    with Image.open("bubble.jpg") as im:
        w, h = im.size
        for row in range(h):
            for col in range(w):
                r, g, b = im.getpixel((col, row))
                r = r // 36 * 36
                g = g // 42 * 42
                b = b // 42 * 42
                im.putpixel((col, row), (r, g, b))
        im.show()


if __name__ == "__main__":
    simple_quant()
