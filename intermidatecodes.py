class AssignmentCode:
    def __init__(self,var,left,op=None,right=None):
        self.var = var
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        if(self.op==None):
            return f'{self.var} = {self.left}'
        return f'{self.var} = {self.left}{self.op}{self.right}'

class ChangeCode:
    def __init__(self,var,op,right):
        self.var = var
        self.op = op
        self.right = right

    def __str__(self):
        return f'{self.var} {self.op}= {self.right}'

class JumbCode:
    def __init__(self,dist):
        self.dist = dist

    def __str__(self):
        return f"GOTO({self.dist})"

class LabelCode:
    def __init__(self,label):
        self.label = label

    def __str__(self):
        return f'{self.label} : '

class DeclareCode:
    def __init__(self,name,bytes):
        self.name=name
        self.bytes = bytes

    def __str__(self):
        return f'Declare {self.name} {self.bytes} bytes'

class CompareCode:
    def __init__(self,left,operation,right,jump):
        self.left = left
        self.operation = operation
        self.right = right
        self.jump = jump

    def __str__(self):
        return f"if {self.left}{self.operation}{self.right} GOTO({self.jump})"



class InterCodeArray:
    def __init__(self):
        self.code=[]

    def append(self,n):
        self.code.append(n)

    def push(self):
        pass

    def print_extra(self):
        for i in self.code:
            print(i)

    def combine_next(self,i):
        if(i+1<len(self.code)):
            s = self.code.pop(i+1)
            self.code[i].str_rep += s.str_rep
            self.code[i].type = s.type
