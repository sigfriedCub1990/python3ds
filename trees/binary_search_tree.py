#!/usr/bin/python


class BinarySearchTree:
    def __init__(self):
        self.root: TreeNode = None
        self.size: int = 0

    def put(self, key, value):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self._put(key, value, self.root)
        self.size = self.size + 1

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
        return None

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._delete(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")

    def size(self) -> int:
        return self.size

    def _delete(self, current_node):
        if current_node.is_leaf():
            if current_node.parent.left_child == current_node:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_children():
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:
            if current_node.get_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_value(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_value(
                        current_node.right_child.key,
                        current_node.right_child.value,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value)
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value)

    def _get(self, key, current_node):
        if current_node.key == key:
            return current_node
        elif current_node.is_leaf():
            return None
        else:
            if key < current_node.key:
                return self._get(key, current_node.left_child)
            else:
                return self._get(key, current_node.right_child)

    def __contains__(self, key):
        return bool(self.get(key))

    def __delitem__(self, key):
        self.delete(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def find_successor(self):
        successor = None
        if self.right_child:
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        """Find minimum value

        In a Binary Search Tree this value will always be the left-most
        element of the tree, i.e. we will simply look up for the left-most
        element without a left_child property.
        """
        current = self
        while current.left_child:
            current = current.left_child
        return current

    def splice_out(self):
        """Splice out a Node

        1. If Node is a leaf just remove reference from parent to Node
        2. If Node has a child then:
            2.1 If it has a Left child
                2.1.1 If Node is a Left child
                    2.1.1.1 Parent's Left child is Left child of Node
                2.1.2 Else
                    2.1.2.1 Parent's Right child is Left child of Node
                2.1.3 Node's Left child's Parent is Node's Parent
            2.2 If it has a Left child
                2.2.1 If Node is a Left child
                    2.2.1.1 Parent's Left child is Left child of Node
                2.2.2 Else
                    2.2.2.1 Parent's Right child is Left child of Node
                2.2.3 Node's Right child's Parent is Node's Parent
        """
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_a_child():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_a_child(self):
        return self.right_child or self.left_child

    def has_children(self):
        return self.right_child and self.left_child

    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def __iter__(self):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.right_child:
                for elem in self.right_child:
                    yield elem


if __name__ == "__main__":
    # tree = BinarySearchTree()
    # tree.put(70, 1)
    # tree.put(31, 2)
    # tree.put(93, 3)
    # print(tree.get(93))
    # print(tree.get(40))
    # print(20 in tree)
    my_tree = BinarySearchTree()
    my_tree["a"] = "a"
    my_tree["q"] = "quick"
    my_tree["b"] = "brown"
    my_tree["f"] = "fox"
    my_tree["j"] = "jumps"
    my_tree["o"] = "over"
    my_tree["t"] = "the"
    my_tree["l"] = "lazy"
    my_tree["d"] = "dog"

    print(my_tree["q"])
    print(my_tree["l"])
    print("There are {} items in this tree".format(len(my_tree)))
    my_tree.delete("a")
    print("There are {} items in this tree".format(len(my_tree)))

    for node in my_tree:
        print(my_tree[node], end=" ")
    print()
