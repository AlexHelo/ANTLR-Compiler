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
        print("li $" + str(self.x) + ", " + ctx.Number().getText())
    
    def exitText(self, ctx: basicParser.TextContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("lw $" + str(self.x) + ", " + ctx.Text().getText())

    def exitAddition(self, ctx:basicParser.AdditionContext):
        print("Added $" + str((self.x)) +", " + "$" + str(self.list2.pop()) + ", " + "$" + str(self.list2.pop()))

    def exitSubstract(self, ctx: basicParser.SubtractContext):
        print("Subtracted $" + str((self.x)) +", " + "$" + str(self.list2.pop()) + ", " + "$" + str(self.list2.pop()))

    def exitMultiply(self, ctx: basicParser.MultiplyContext):
        print("Multiplied $" + str((self.x)) +", " + "$" + str(self.list2.pop()) + ", " + "$" + str(self.list2.pop()))

    def exitDivide(self, ctx: basicParser.DivideContext):
        print("Divided $" + str((self.x)) +", " + "$" + str(self.list2.pop()) + ", " + "$" + str(self.list2.pop()))

    def exitLess(self, ctx:basicParser.LessContext):
        print("lower $" + str((self.x)) +", " + "$" + str(self.list2.pop(1)) + ", " + "$" + str(self.list2.pop()))
    
    def exitMore(self, ctx:basicParser.MoreContext):
        print("greater $" + str((self.x)) +", " + "$" + str(self.list2.pop(1)) + ", " + "$" + str(self.list2.pop()))

    def exitAssign(self, ctx:basicParser.AssignContext):
        print("Assigned $" + str((self.x)) +", " + "$" + str(self.list2.pop()) + ", " + "$" + str(self.list2.pop()))

    def exitIf(self, ctx:basicParser.IfelseContext):
        print("bequals $" + str(self.list.pop(0)) +", $" + str(self.list.pop(0)) + ", ELSE")

    def exitIfelse(self, ctx: basicParser.IfContext):
        print("bequals $" + str(self.list.pop(0)) +", $" + str(self.list.pop(0)))

    def exitPrint(self, ctx:basicParser.PrintContext):
        print("syscall")
        print("______")

    def exitEnd(self, ctx: basicParser.EndContext):
        print("Bye Bye!")

    def exitDeclaracion(self, ctx:basicParser.DeclareTextContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("sw $" + str(self.x) + ", " + ctx.Text().getText())

    def exitDeclaracion(self, ctx:basicParser.DeclareNumContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("sw $" + str(self.x) + ", " + ctx.Number().getText())






  
