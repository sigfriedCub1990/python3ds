#!/usr/bin/python
from gates.and_gate import And
from gates.or_gate import Or
from gates.not_gate import Not
from base.connector import Connector
from gates.xor_gate import Xor

def main():
    # g1 = And('G1')
    # g2 = And('G2')
    # g3 = Or('G3')
    # g4 = Not('G4')
    # c1 = Connector(g1, g3)
    # c2 = Connector(g2, g3)
    # c3 = Connector(g3, g4)
    # print(g4.get_output())
    # Half adder https://en.m.wikipedia.org/wiki/Adder_(electronics)
    g1 = Xor('xor')
    g2 = And('and')
    print(g1.get_output())
    print(g2.get_output())
    print(g1.get_output())
    print(g2.get_output())
    print(g1.get_output())
    print(g2.get_output())
    print(g1.get_output())
    print(g2.get_output())

if __name__ == '__main__':
    main()
