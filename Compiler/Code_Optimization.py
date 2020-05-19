from utils.Tokens import *
from utils.TreeNodes import *
from utils.intermidatecodes import *

def eval_op(left,op,right):
    if(op=='+'):
        return left+right
    elif(op=='*'):
        return left*right
    elif(op=='-'):
        return left-right
    elif(op=='/'):
        if(right==0):
            raise Exception("Error Division By Zero");
        return left//right

def eval_comparison(left,op,right):
    if(op=='>'):
        return left>right
    elif(op=='=='):
        return left==right
    elif(op=='<'):
        return left<right
    elif(op=='>='):
        return left>=right
    elif(op=='<='):
        return left<=right
    elif(op=='!='):
        return left!=right

def isint(s):
    try:
        int(s)
        return 1
    except Exception as e:
        return 0

class CodeOptimization:
    def __init__(self,input_code,input_identifiers,input_constants):
        self.input_code = input_code
        self.input_identifiers = input_identifiers
        self.input_constants = input_constants
        self.output_code = self.input_code
        self.output_identifiers = self.input_identifiers
        self.output_constants = self.input_constants
        self.tempmap={}
        self.optimize();

    def remove_temp(self,codearray):
        temparray = InterCodeArray()
        for code in codearray.code:
            if(isinstance(code,AssignmentCode)):
                left = self.tempmap.get(code.left,code.left)
                right = self.tempmap.get(code.right,code.right)
                if(isint(left) and isint(right)):
                    self.tempmap[code.var] = eval_op(int(left),code.op,int(right))
                    del self.output_identifiers[code.var];
                else:
                    code.left = self.tempmap.get(code.left,code.left)
                    code.right = self.tempmap.get(code.right,code.right)
                    temparray.append(code)
            else:
                temparray.append(code)


        return temparray


    def loading_once(self,codearray):
        temparray = InterCodeArray()
        last_loaded = ""
        for code in codearray.code:
            if(isinstance(code,AssignmentCode)):
                left = code.left
                right = code.right
                if(code.op!=None and left==last_loaded):
                    c = ChangeCode(code.var,code.op,right)
                    temparray.append(c)
                elif(code.op!=None and (right==last_loaded and code.op in '*+')):
                    c = ChangeCode(code.var,code.op,left)
                    temparray.append(c)
                else:
                    temparray.append(code)

                last_loaded = code.var
            else:
                temparray.append(code)
                last_loaded=""


        return temparray

    def end_comparisions(self,codearray):
        temparray = InterCodeArray()
        remove_until = ""
        for index,code in enumerate(codearray.code):
            if(remove_until!=""):
                if(isinstance(code,LabelCode) and code.label == remove_until):
                    remove_until = ""
                continue

            if(isinstance(code,CompareCode)):
                left = code.left
                right = code.right
                if(isint(left) and isint(right)):
                    x = eval_comparison(int(left),code.operation,int(right))
                    if(x):
                        remove_until = code.jump
                    else:
                        remove_until = codearray.code[index+1].dist
                else:
                    temparray.append(code)
            else:
                temparray.append(code)
        return temparray


    def optimize(self):
        self.output_code = self.remove_temp(self.input_code)
        self.output_code = self.loading_once(self.output_code)
        self.output_code = self.end_comparisions(self.output_code)


    def get_code(self):
        return self.output_code,self.output_identifiers,self.output_constants,self.tempmap
