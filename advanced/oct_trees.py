#!/usr/bin/env python

import sys
from PIL import Image


class OctTree:
    def __init__(self) -> None:
        self.root = None
        self.max_level = 5
        self.num_leaves = 0
        self.all_leaves = []

    def insert(self, r, g, b):
        if not self.root:
            self.root = self.OTNode(outer=self)
        self.root.insert(r, g, b, 0, self)

    def find(self, r, g, b):
        if self.root:
            return self.root.find(r, g, b, 0)

    def reduce(self, max_cubes):
        while len(self.all_leaves) > max_cubes:
            smallest = self.find_min_cube()
            smallest.parent.merge()
            self.all_leaves.append(smallest.parent)
            self.num_leaves += 1

    def find_min_cube(self):
        min_count = sys.maxsize
        max_level = 0
        min_cube = None
        for i in self.all_leaves:
            if i.count <= min_count and i.level >= max_level:
                min_cube = i
                min_count = i.count
                max_level = i.level
        print(f"Min cube is: {min_cube}")
        return min_cube

    class OTNode:
        def __init__(self, parent=None, level=0, outer=None) -> None:
            self.red = 0
            self.green = 0
            self.blue = 0
            self.count = 0
            self.parent = parent
            self.level = level
            self.oTree = outer
            self.children = [None] * 8

        def merge(self):
            for i in self.children:
                if i:
                    if i.count > 0:
                        self.oTree.all_leaves.remove(i)
                        self.oTree.num_leaves -= 1
                    else:
                        print("Recursively mergin non-leaf...")
                        i.merge()
                    self.count += i.count
                    self.red += i.red
                    self.green += i.green
                    self.blue += i.blue
            for i in range(8):
                self.children[i] = None

        def find(self, r, g, b, level):
            if level < self.oTree.max_level:
                idx = self.compute_index(r, g, b, level)
                if self.children[idx]:
                    return self.children[idx].find(r, g, b, level + 1)
                elif self.count > 0:
                    return (
                        self.red // self.count,
                        self.green // self.count,
                        self.blue // self.count,
                    )
                else:
                    print("No leaf to represent this color")
            else:
                return (
                    self.red // self.count,
                    self.green // self.count,
                    self.blue // self.count,
                )

        def insert(self, r, g, b, level, outer):
            if level < self.oTree.max_level:
                idx = self.compute_index(r, g, b, level)
                if self.children[idx] == None:
                    self.children[idx] = outer.OTNode(
                        parent=self, level=level + 1, outer=outer
                    )
                self.children[idx].insert(r, g, b, level + 1, outer)
            else:
                if self.count == 0:
                    self.oTree.num_leaves = self.oTree.num_leaves + 1
                    self.oTree.all_leaves.append(self)
                self.red += r
                self.green += g
                self.blue += b
                self.count += 1

        def compute_index(self, r, g, b, l):
            shift = 8 - l
            rc = r >> shift - 2 & 0x4
            gc = g >> shift - 1 & 0x2
            bc = b >> shift & 0x1
            return rc | gc | bc


def build_and_display():
    with Image.open("bubble.jpg") as im:
        w, h = im.size
        ot = OctTree()
        for row in range(0, h):
            for col in range(0, w):
                r, g, b = im.getpixel((col, row))
                ot.insert(r, g, b)

        ot.reduce(256)

        for row in range(0, h):
            for col in range(0, w):
                r, g, b = im.getpixel((col, row))
                nr, ng, nb = ot.find(r, g, b)
                im.putpixel((col, row), (nr, ng, nb))

        # im.save('quantized.png')
        im.show()


if __name__ == "__main__":
    build_and_display()
