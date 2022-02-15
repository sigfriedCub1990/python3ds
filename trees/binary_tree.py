#!/usr/bin/python

import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child = self.right_child
            self.right_child = new_child

    def get_root_val(self):
        return self.key

    def set_root_val(self, new_obj):
        self.key = new_obj

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def __str__(self):
        return self.key

    def bfs(self):
        queue = [self]
        result_tree = []
        while len(queue) != 0:
            tree = queue.pop(0)
            # print(tree.get_root_val())
            result_tree.append(tree.get_root_val())
            if tree.get_left_child() is not None:
                queue.append(tree.get_left_child())
            if tree.get_right_child() is not None:
                queue.append(tree.get_right_child())

        return result_tree

    def is_leaf(self):
        return self.right_child == None and self.left_child == None

    def evaluate(self, node):
        if node.is_leaf():
            return node.get_root_val()
        else:
            left_child = node.get_left_child()
            right_child = node.get_right_child()
            fn = operators[node.get_root_val()]
            return fn(self.evaluate(left_child), self.evaluate(right_child))

    def preorder(self, node):
        if node:
            print(node.get_root_val())
            self.preorder(node.get_left_child())
            self.preorder(node.get_right_child())

    def inorder(self, node):
        if node:
            self.preorder(node.get_left_child())
            print(node.get_root_val())
            self.preorder(node.get_right_child())

    def postorder(self, node):
        if node:
            self.preorder(node.get_left_child())
            self.preorder(node.get_right_child())
            print(node.get_root_val())


def build_tree():
    tree = BinaryTree("a")
    tree.insert_left("b")
    tree.insert_right("c")
    tree.get_left_child().insert_right("d")
    tree.get_right_child().insert_left("e")
    tree.get_right_child().insert_right("f")
    print(tree.bfs())
    tree.preorder(tree)


if __name__ == "__main__":
    tree = BinaryTree("a")
    tree.insert_left("b")
    tree.insert_right("c")
    build_tree()
