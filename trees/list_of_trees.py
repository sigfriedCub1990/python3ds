#!/usr/bin/python
import pprint


def make_binary_tree(root):
    return [root, [], []]


def insert_left(root, new_child):
    old_child = root.pop(1)
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root


def insert_right(root, new_child):
    old_child = root.pop(2)
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])
    else:
        root.insert(2, [new_child, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def build_tree():
    tree = make_binary_tree("a")
    insert_left(tree, "b")
    insert_right(tree, "c")
    insert_right(get_left_child(tree), "d")
    insert_right(get_right_child(tree), "f")
    insert_left(get_right_child(tree), "e")

    return tree


if __name__ == "__main__":
    tree = make_binary_tree(1)
    insert_left(tree, 2)
    insert_right(tree, 3)
    insert_left(tree, 4)
    insert_right(tree, 5)
    ex_tree = build_tree()
    pp = pprint.PrettyPrinter(indent=4)
    pprint.pprint(ex_tree, indent=2, width=15)
    # print(f"{get_root_val(tree):30}")
    # print(f"{get_left_child(tree)[0]:25} {get_right_child(tree)[0]:9}")
    # print(f"{get_left_child(get_left_child(tree))[0]:20} {get_right_child(get_right_child(tree))[1]:20}")
