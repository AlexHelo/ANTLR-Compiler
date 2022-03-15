# Generated from c:\Users\alexx\Documents\8th Semester Resources\Compiler Design\BasicCompiler\antlr\basic.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .basicParser import basicParser
else:
    from basicParser import basicParser

# This class defines a complete listener for a parse tree produced by basicParser.
class basicListener(ParseTreeListener):

    # Enter a parse tree produced by basicParser#program.
    def enterProgram(self, ctx:basicParser.ProgramContext):
        pass

    # Exit a parse tree produced by basicParser#program.
    def exitProgram(self, ctx:basicParser.ProgramContext):
        pass


    # Enter a parse tree produced by basicParser#Divide.
    def enterDivide(self, ctx:basicParser.DivideContext):
        pass

    # Exit a parse tree produced by basicParser#Divide.
    def exitDivide(self, ctx:basicParser.DivideContext):
        pass


    # Enter a parse tree produced by basicParser#More.
    def enterMore(self, ctx:basicParser.MoreContext):
        pass

    # Exit a parse tree produced by basicParser#More.
    def exitMore(self, ctx:basicParser.MoreContext):
        pass


    # Enter a parse tree produced by basicParser#Addition.
    def enterAddition(self, ctx:basicParser.AdditionContext):
        pass

    # Exit a parse tree produced by basicParser#Addition.
    def exitAddition(self, ctx:basicParser.AdditionContext):
        pass


    # Enter a parse tree produced by basicParser#Number.
    def enterNumber(self, ctx:basicParser.NumberContext):
        pass

    # Exit a parse tree produced by basicParser#Number.
    def exitNumber(self, ctx:basicParser.NumberContext):
        pass


    # Enter a parse tree produced by basicParser#Multiply.
    def enterMultiply(self, ctx:basicParser.MultiplyContext):
        pass

    # Exit a parse tree produced by basicParser#Multiply.
    def exitMultiply(self, ctx:basicParser.MultiplyContext):
        pass


    # Enter a parse tree produced by basicParser#Subtract.
    def enterSubtract(self, ctx:basicParser.SubtractContext):
        pass

    # Exit a parse tree produced by basicParser#Subtract.
    def exitSubtract(self, ctx:basicParser.SubtractContext):
        pass


    # Enter a parse tree produced by basicParser#Text.
    def enterText(self, ctx:basicParser.TextContext):
        pass

    # Exit a parse tree produced by basicParser#Text.
    def exitText(self, ctx:basicParser.TextContext):
        pass


    # Enter a parse tree produced by basicParser#Assign.
    def enterAssign(self, ctx:basicParser.AssignContext):
        pass

    # Exit a parse tree produced by basicParser#Assign.
    def exitAssign(self, ctx:basicParser.AssignContext):
        pass


    # Enter a parse tree produced by basicParser#Less.
    def enterLess(self, ctx:basicParser.LessContext):
        pass

    # Exit a parse tree produced by basicParser#Less.
    def exitLess(self, ctx:basicParser.LessContext):
        pass


    # Enter a parse tree produced by basicParser#Print.
    def enterPrint(self, ctx:basicParser.PrintContext):
        pass

    # Exit a parse tree produced by basicParser#Print.
    def exitPrint(self, ctx:basicParser.PrintContext):
        pass


    # Enter a parse tree produced by basicParser#Ifelse.
    def enterIfelse(self, ctx:basicParser.IfelseContext):
        pass

    # Exit a parse tree produced by basicParser#Ifelse.
    def exitIfelse(self, ctx:basicParser.IfelseContext):
        pass


    # Enter a parse tree produced by basicParser#End.
    def enterEnd(self, ctx:basicParser.EndContext):
        pass

    # Exit a parse tree produced by basicParser#End.
    def exitEnd(self, ctx:basicParser.EndContext):
        pass


    # Enter a parse tree produced by basicParser#If.
    def enterIf(self, ctx:basicParser.IfContext):
        pass

    # Exit a parse tree produced by basicParser#If.
    def exitIf(self, ctx:basicParser.IfContext):
        pass


    # Enter a parse tree produced by basicParser#DeclareText.
    def enterDeclareText(self, ctx:basicParser.DeclareTextContext):
        pass

    # Exit a parse tree produced by basicParser#DeclareText.
    def exitDeclareText(self, ctx:basicParser.DeclareTextContext):
        pass


    # Enter a parse tree produced by basicParser#DeclareNum.
    def enterDeclareNum(self, ctx:basicParser.DeclareNumContext):
        pass

    # Exit a parse tree produced by basicParser#DeclareNum.
    def exitDeclareNum(self, ctx:basicParser.DeclareNumContext):
        pass



del basicParser