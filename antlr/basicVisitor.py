# Generated from c:\Users\alexx\Documents\8th Semester Resources\Compiler Design\BasicCompiler\antlr\basic.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .basicParser import basicParser
else:
    from basicParser import basicParser

# This class defines a complete generic visitor for a parse tree produced by basicParser.

class basicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by basicParser#program.
    def visitProgram(self, ctx:basicParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Divide.
    def visitDivide(self, ctx:basicParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#More.
    def visitMore(self, ctx:basicParser.MoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Addition.
    def visitAddition(self, ctx:basicParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Number.
    def visitNumber(self, ctx:basicParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Multiply.
    def visitMultiply(self, ctx:basicParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Subtract.
    def visitSubtract(self, ctx:basicParser.SubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Text.
    def visitText(self, ctx:basicParser.TextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Assign.
    def visitAssign(self, ctx:basicParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Less.
    def visitLess(self, ctx:basicParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Print.
    def visitPrint(self, ctx:basicParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#Ifelse.
    def visitIfelse(self, ctx:basicParser.IfelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#End.
    def visitEnd(self, ctx:basicParser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#If.
    def visitIf(self, ctx:basicParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#DeclareText.
    def visitDeclareText(self, ctx:basicParser.DeclareTextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by basicParser#DeclareNum.
    def visitDeclareNum(self, ctx:basicParser.DeclareNumContext):
        return self.visitChildren(ctx)



del basicParser