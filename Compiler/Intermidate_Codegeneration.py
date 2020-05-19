from utils.Tokens import *
from utils.TreeNodes import *
from utils.intermidatecodes import *

class TCounter:
    def __init__(self,char):
        self.counter = 1;
        self.char = char

    def increase(self):
        self.counter+=1;

    def reset(self):
        self.counter=1;

    def get(self):
        return f'{self.char}{self.counter}';



class IntermidateCodeGeneration:
    def __init__(self,tree_root):
        self.root = tree_root
        self.code=InterCodeArray()
        self.t = TCounter('T')
        self.l = TCounter('L')
        self.s = TCounter('S')
        self.identifiers = {}
        self.constants = {}
        self.execute_statement(tree_root)


    def execute_exp(self,root):
        if(isinstance(root,IdentifierNode) or isinstance(root,NumberNode)):
            return root.get_num()
        else:
            left = self.execute_exp(root.left)
            op = root.op_tok.value
            right = self.execute_exp(root.right)
            cur_t = self.t.get()
            self.identifiers[cur_t] = 'int'
            self.t.increase()
            self.code.append(AssignmentCode(cur_t,left,op,right))
            return cur_t;


    def execute_assignment(self,root):
        right = self.execute_exp(root.expression)
        self.code.append(AssignmentCode(root.identifier.value,right))



    def execute_if(self,root):
        self.execute_condition(root.if_condition);

        body = self.l.get();self.l.increase()
        end_if = self.l.get();self.l.increase()

        if(root.else_body):
            goto_else_end = self.l.get();self.l.increase()
            self.code.append(JumbCode(goto_else_end))
            self.code.append(LabelCode(body))
            self.execute_statement(root.if_body)
            self.code.append(JumbCode(end_if))
            self.code.append(LabelCode(goto_else_end))
            self.execute_statement(root.else_body)
            self.code.append(LabelCode(end_if))
        else:
            self.code.append(JumbCode(end_if))
            self.code.append(LabelCode(body))
            self.execute_statement(root.if_body)
            self.code.append(LabelCode(end_if))

    def execute_while(self,root):
        start_loop = self.l.get();self.l.increase()
        self.code.append(LabelCode(start_loop))

        self.execute_condition(root.condition);
        body = self.l.get();self.l.increase()

        end_while = self.l.get();self.l.increase()

        self.code.append(JumbCode(end_while))
        self.code.append(LabelCode(body))
        self.execute_statement(root.body)
        self.code.append(JumbCode(start_loop))
        self.code.append(LabelCode(end_while))


    def execute_condition(self,root):
        left = self.execute_exp(root.left_expression)
        compare = root.comparison.value
        right = self.execute_exp(root.right_expression)

        body = self.l.get()

        self.code.append(CompareCode(left,compare,right,body))

    def execute_print(self,root):
        if(root.type=="string"):
            self.constants[self.s.get()] = root.value
            right = self.s.get()
            self.s.increase()
            self.code.append(PrintCode("string",right))
        elif(root.type=="int"):
            right = self.execute_exp(root.value)
            self.code.append(PrintCode("int",right))


    def execute_declaration(self,root):
        type = root.declaration_type
        for i in root.identifiers:
            self.identifiers[i.value]=type.value

    def execute_statement(self,root):
        if(root==None):
            return ;

        if(isinstance(root,Statement)):
            self.execute_statement(root.left)
            self.execute_statement(root.right)
        elif(isinstance(root,IfStatement)):
            self.execute_if(root)
        elif(isinstance(root,WhileStatement)):
            self.execute_while(root)
        elif(isinstance(root,PrintStatement)):
            self.execute_print(root)
        elif(isinstance(root,Declaration)):
            self.execute_declaration(root)
        elif(isinstance(root,Assignment)):
            self.execute_assignment(root)



    def get_code(self):
        return self.code,self.identifiers,self.constants
