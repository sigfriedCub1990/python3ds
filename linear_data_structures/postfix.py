#!/usr/bin/python
from stack import Stack


def tokenizer(expression):
    output = []

    for token in expression:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            output.append(token)
        elif token in "()-*/=^+":
            output.append(token)

    return output


def to_postfix_notation(expression):
    precedence = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1,
        "^": 2,
        "(": -1,
        ")": -1
    }
    operators = {"+", "-", "*", "/"}
    parentheses = "()"
    output = []
    op_stack = Stack()

    tokens = tokenizer(expression)

    for token in tokens:
        # If it's an operand, append it to the list
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            output.append(token)
        # If it's an opening parentheses push it into the stack
        elif token == "(":
            op_stack.push(token)
        # If it's a closing parentheses let's pop the operands in between
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                output.append(top_token)
                top_token = op_stack.pop()
        # If it's an operand let's push it into the Stack, but first, let's pop
        # the ones with a higher precedence, if any
        else:
            while (not op_stack.is_empty()) and (precedence[op_stack.peek()] >= precedence[token]):
                output.append(op_stack.pop())
            op_stack.push(token)

    # Finally, if there are elements in the stack just append them to the output
    while op_stack.size() != 0:
        output.append(op_stack.pop())

    return output


if __name__ == '__main__':
    print(to_postfix_notation("A * B + C * D"))
