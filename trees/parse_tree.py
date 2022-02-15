#!/usr/bin/python
from binary_tree import BinaryTree


def build_tree(expression: str):
    parse_tree = BinaryTree("")
    numbers = "0123456789"
    operators = "+-*/"

    # To keep track of the previous
    # node(s) we accessed
    stack = [parse_tree]
    current = parse_tree
    for token in expression:
        if token == "(":
            current.insert_left("")
            stack.append(current)
            current = current.get_left_child()
        elif token == ")":
            current = stack.pop()
        elif token in numbers:
            current.set_root_val(int(token))
            current = stack.pop()
        elif token in operators:
            current.set_root_val(token)
            current.insert_right("")
            stack.append(current)
            current = current.get_right_child()

    return parse_tree


def print_exp(tree):
    result = ""
    if tree:
        result = "(" + print_exp(tree.get_left_child())
        result = result + str(tree.get_root_val())
        result = result + print_exp(tree.get_right_child()) + ")"
    return result


if __name__ == "__main__":
    expression = "(3+(4*5))"
    # expression = "((7+3)*(5-2))"
    parse_tree = build_tree(expression)
    print(parse_tree.bfs())
    print(f"Evaluation result: {parse_tree.evaluate(parse_tree)}")
    print("Traversals:")
    print("Preorder")
    parse_tree.preorder(parse_tree)
    print()
    print("Inorder")
    parse_tree.inorder(parse_tree)
    print()
    print("Postorder")
    parse_tree.postorder(parse_tree)
    print(print_exp(parse_tree))
