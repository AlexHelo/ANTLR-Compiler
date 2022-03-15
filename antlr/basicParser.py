# Generated from c:\Users\alexx\Documents\8th Semester Resources\Compiler Design\BasicCompiler\antlr\basic.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\5\3\21\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7")
        buf.write("\3(\n\3\f\3\16\3+\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5")
        buf.write("\4B\n\4\3\4\3\4\7\4F\n\4\f\4\16\4I\13\4\3\4\2\4\4\6\5")
        buf.write("\2\4\6\2\2\2U\2\t\3\2\2\2\4\20\3\2\2\2\6A\3\2\2\2\b\n")
        buf.write("\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3")
        buf.write("\2\2\2\f\3\3\2\2\2\r\16\b\3\1\2\16\21\7\22\2\2\17\21\7")
        buf.write("\23\2\2\20\r\3\2\2\2\20\17\3\2\2\2\21)\3\2\2\2\22\23\f")
        buf.write("\13\2\2\23\24\7\3\2\2\24(\5\4\3\f\25\26\f\n\2\2\26\27")
        buf.write("\7\4\2\2\27(\5\4\3\13\30\31\f\t\2\2\31\32\7\5\2\2\32(")
        buf.write("\5\4\3\n\33\34\f\b\2\2\34\35\7\6\2\2\35(\5\4\3\t\36\37")
        buf.write("\f\7\2\2\37 \7\7\2\2 (\5\4\3\b!\"\f\6\2\2\"#\7\b\2\2#")
        buf.write("(\5\4\3\7$%\f\5\2\2%&\7\t\2\2&(\5\4\3\6\'\22\3\2\2\2\'")
        buf.write("\25\3\2\2\2\'\30\3\2\2\2\'\33\3\2\2\2\'\36\3\2\2\2\'!")
        buf.write("\3\2\2\2\'$\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\5")
        buf.write("\3\2\2\2+)\3\2\2\2,-\b\4\1\2-.\7\n\2\2./\5\4\3\2/\60\7")
        buf.write("\13\2\2\60\61\5\6\4\b\61B\3\2\2\2\62\63\7\n\2\2\63\64")
        buf.write("\5\4\3\2\64\65\7\13\2\2\65\66\5\6\4\2\66\67\7\f\2\2\67")
        buf.write("8\5\6\4\78B\3\2\2\29:\7\r\2\2:;\5\4\3\2;<\7\16\2\2<B\3")
        buf.write("\2\2\2=>\7\20\2\2>B\7\22\2\2?@\7\21\2\2@B\7\23\2\2A,\3")
        buf.write("\2\2\2A\62\3\2\2\2A9\3\2\2\2A=\3\2\2\2A?\3\2\2\2BG\3\2")
        buf.write("\2\2CD\f\5\2\2DF\7\17\2\2EC\3\2\2\2FI\3\2\2\2GE\3\2\2")
        buf.write("\2GH\3\2\2\2H\7\3\2\2\2IG\3\2\2\2\b\13\20\')AG")
        return buf.getvalue()


class basicParser ( Parser ):

    grammarFileName = "basic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'<'", "'>'", 
                     "'='", "'when this ('", "') do that'", "'if not then'", 
                     "'showme('", "')'", "'byebye'", "'num'", "'abc'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Number", "Text", "WS" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_statement = 2

    ruleNames =  [ "program", "expression", "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    Number=16
    Text=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basicParser.ExpressionContext,i)


        def getRuleIndex(self):
            return basicParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = basicParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.expression(0)
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==basicParser.Number or _la==basicParser.Text):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return basicParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivideContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basicParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide" ):
                listener.enterDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide" ):
                listener.exitDivide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide" ):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class MoreContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basicParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMore" ):
                listener.enterMore(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMore" ):
                listener.exitMore(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore" ):
                return visitor.visitMore(self)
            else:
                return visitor.visitChildren(self)


    class AdditionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basicParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddition" ):
                listener.enterAddition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddition" ):
                listener.exitAddition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(basicParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basicParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)


    class SubtractContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basicParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtract" ):
                listener.enterSubtract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtract" ):
                listener.exitSubtract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtract" ):
                return visitor.visitSubtract(self)
            else:
                return visitor.visitChildren(self)


    class TextContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Text(self):
            return self.getToken(basicParser.Text, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterText" ):
                listener.enterText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitText" ):
                listener.exitText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitText" ):
                return visitor.visitText(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basicParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basicParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(basicParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLess" ):
                listener.enterLess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLess" ):
                listener.exitLess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = basicParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [basicParser.Number]:
                localctx = basicParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 12
                self.match(basicParser.Number)
                pass
            elif token in [basicParser.Text]:
                localctx = basicParser.TextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(basicParser.Text)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = basicParser.AdditionContext(self, basicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 16
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 17
                        self.match(basicParser.T__0)
                        self.state = 18
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = basicParser.SubtractContext(self, basicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 19
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 20
                        self.match(basicParser.T__1)
                        self.state = 21
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = basicParser.MultiplyContext(self, basicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 22
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 23
                        self.match(basicParser.T__2)
                        self.state = 24
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = basicParser.DivideContext(self, basicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 25
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 26
                        self.match(basicParser.T__3)
                        self.state = 27
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = basicParser.LessContext(self, basicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 28
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 29
                        self.match(basicParser.T__4)
                        self.state = 30
                        self.expression(6)
                        pass

                    elif la_ == 6:
                        localctx = basicParser.MoreContext(self, basicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 31
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 32
                        self.match(basicParser.T__5)
                        self.state = 33
                        self.expression(5)
                        pass

                    elif la_ == 7:
                        localctx = basicParser.AssignContext(self, basicParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 34
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 35
                        self.match(basicParser.T__6)
                        self.state = 36
                        self.expression(4)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return basicParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PrintContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(basicParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class IfelseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(basicParser.ExpressionContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(basicParser.StatementContext)
            else:
                return self.getTypedRuleContext(basicParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfelse" ):
                listener.enterIfelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfelse" ):
                listener.exitIfelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfelse" ):
                return visitor.visitIfelse(self)
            else:
                return visitor.visitChildren(self)


    class EndContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self):
            return self.getTypedRuleContext(basicParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnd" ):
                listener.enterEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnd" ):
                listener.exitEnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnd" ):
                return visitor.visitEnd(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(basicParser.ExpressionContext,0)

        def statement(self):
            return self.getTypedRuleContext(basicParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class DeclareTextContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Text(self):
            return self.getToken(basicParser.Text, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareText" ):
                listener.enterDeclareText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareText" ):
                listener.exitDeclareText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareText" ):
                return visitor.visitDeclareText(self)
            else:
                return visitor.visitChildren(self)


    class DeclareNumContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a basicParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(basicParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareNum" ):
                listener.enterDeclareNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareNum" ):
                listener.exitDeclareNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareNum" ):
                return visitor.visitDeclareNum(self)
            else:
                return visitor.visitChildren(self)



    def statement(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = basicParser.StatementContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_statement, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = basicParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 43
                self.match(basicParser.T__7)
                self.state = 44
                self.expression(0)
                self.state = 45
                self.match(basicParser.T__8)
                self.state = 46
                self.statement(6)
                pass

            elif la_ == 2:
                localctx = basicParser.IfelseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(basicParser.T__7)
                self.state = 49
                self.expression(0)
                self.state = 50
                self.match(basicParser.T__8)
                self.state = 51
                self.statement(0)
                self.state = 52
                self.match(basicParser.T__9)
                self.state = 53
                self.statement(5)
                pass

            elif la_ == 3:
                localctx = basicParser.PrintContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(basicParser.T__10)
                self.state = 56
                self.expression(0)
                self.state = 57
                self.match(basicParser.T__11)
                pass

            elif la_ == 4:
                localctx = basicParser.DeclareNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(basicParser.T__13)
                self.state = 60
                self.match(basicParser.Number)
                pass

            elif la_ == 5:
                localctx = basicParser.DeclareTextContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(basicParser.T__14)
                self.state = 62
                self.match(basicParser.Text)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = basicParser.EndContext(self, basicParser.StatementContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statement)
                    self.state = 65
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 66
                    self.match(basicParser.T__12) 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        self._predicates[2] = self.statement_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

    def statement_sempred(self, localctx:StatementContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         




