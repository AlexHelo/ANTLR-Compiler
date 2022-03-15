from antlr.basicListener import basicListener
from antlr.basicParser import basicParser

class GenCode(basicListener):

    def __init__(self):
        self.x = 0
        self.list = []
        self.list2 = []
    
    def enterProgram(self, ctx:basicParser.ProgramContext):
        print(".text")

    def exitNumber(self, ctx: basicParser.NumberContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("li $v" + str(self.x) + ", " + ctx.Number().getText())
    
    def exitText(self, ctx: basicParser.TextContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("lw $v" + str(self.x) + ", " + ctx.Text().getText())

    def exitAddition(self, ctx:basicParser.AdditionContext):
        print("Added $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

    def exitSubstract(self, ctx: basicParser.SubtractContext):
        print("Subtracted $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

    def exitMultiply(self, ctx: basicParser.MultiplyContext):
        print("Multiplied $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

    def exitDivide(self, ctx: basicParser.DivideContext):
        print("Divided $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

    def exitLess(self, ctx:basicParser.LessContext):
        print("lower $v" + str((self.x)) +", " + "$v" + str(self.list2.pop(1)) + ", " + "$v" + str(self.list2.pop()))
    
    def exitMore(self, ctx:basicParser.MoreContext):
        print("greater $v" + str((self.x)) +", " + "$v" + str(self.list2.pop(1)) + ", " + "$v" + str(self.list2.pop()))

    def exitAssign(self, ctx:basicParser.AssignContext):
        print("Assigned $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

    def exitIf(self, ctx:basicParser.IfelseContext):
        print("bequals $v" + str(self.list.pop(0)) +", $v" + str(self.list.pop(0)) + ", ELSE")

    def exitIfelse(self, ctx: basicParser.IfContext):
        print("bequals $v" + str(self.list.pop(0)) +", $v" + str(self.list.pop(0)))

    def exitPrint(self, ctx:basicParser.PrintContext):
        print("syscall")
        print("______")

    def exitEnd(self, ctx: basicParser.EndContext):
        print("Bye Bye!")

    def exitDeclaracion(self, ctx:basicParser.DeclareTextContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("sw $v" + str(self.x) + ", " + ctx.Text().getText())

    def exitDeclaracion(self, ctx:basicParser.DeclareNumContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("sw $v" + str(self.x) + ", " + ctx.Number().getText())






  
