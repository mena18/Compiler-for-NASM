from utils import *

class NumberNode:
    def __init__(self,tok):
        self.tok = tok

    def __str__(self):
        return f'{self.tok}'

class BinOpNode:
    def __init__(self,left,op_tok,right):
        self.left = left
        self.op_tok = op_tok
        self.right = right

    def __str__(self):
        return f'[{self.left} {self.op_tok} {self.right}]'

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.tokens.push(Token("END",value="END"))

    def factor(self):
        tok = self.tokens.current()
        if(tok.type in ('FLOAT','INT')):
            self.tokens.next();
            return NumberNode(tok)
        elif(tok.value =='('):
            self.tokens.next()
            exp = self.expr()
            if(self.tokens.current().value==')'):
                self.tokens.next()
                return exp
            else:
                raise Exception('Syntax Error Missing ) in line {} '.format(self.tokens.current().line))
        else:
            raise Exception('Syntax Error : Expected Integer or float in line{} ',format(self.tokens.current().line))



    def term(self):
        left = self.factor()

        while(self.tokens.current().value in '*/'):
            op_tok = self.tokens.current()
            self.tokens.next()
            right = self.factor();
            left = BinOpNode(left,op_tok,right)

        return left

    def expr(self):
        left = self.term()

        while(self.tokens.current().value in '+-'):
            op_tok = self.tokens.current()
            self.tokens.next()
            right = self.term();
            left = BinOpNode(left,op_tok,right)

        if(self.tokens.current().value == ')'):
            raise Exception('Syntax Error : Missing ( in line {}'.format(self.tokens.current().line));


        if(self.tokens.current().type in ('FLOAT','INT')):
            raise Exception('Syntax Error : Expected operation  in line {}'.format(self.tokens.current().line));



        if(self.tokens.current().value != ';'):
            raise Exception('Syntax Error : Expected semicolon in line {}'.format(self.tokens.current().line));
        self.tokens.next();
        return left




    def get_root(self):
        root = self.expr()
        if(self.tokens.current().type!="END"):
            raise Exception("Syntax Error")
        return root
