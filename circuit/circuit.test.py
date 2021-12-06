#!/usr/bin/python
import unittest

from and_gate import And
from or_gate import Or
from not_gate import Not
from nand_gate import Nand
from nor_gate import Nor
from connector import Connector

def main():
    g1 = And('g1')
    g2 = And('g2')
    g3 = Or('g3')
    g4 = Not('g4')
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.get_output())

    g5 = Nand('g5')
    g6 = Nand('g6')
    g7 = And('g7')
    c4 = Connector(g5, g7)
    c5 = Connector(g6, g7)
    print(g7.get_output())

if __name__ == '__main__':
    main()
