from antlr4 import *
from antlr.basicParser import basicParser
from antlr.basicLexer import basicLexer
from listeners.genCode import GenCode

import sys


def main():
    parser = basicParser(CommonTokenStream(basicLexer(FileStream("input.txt"))))
    tree = parser.program()

    gencode = GenCode()
    walker = ParseTreeWalker()
    walker.walk(gencode, tree)


if __name__ == '__main__':
    main()