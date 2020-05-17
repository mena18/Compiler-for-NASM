from utils import *
from TreeNodes import *


class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.tokens.push(Token("END",value="END"))
        self.dele = 0


    def read_token_pass(self,expected,message):
        t = self.tokens.current()
        if(t.value != expected):
            raise Exception("{}  in line {}".format(message,t.line))
        self.tokens.next();

    def factor(self):
        tok = self.tokens.current()
        if(tok.type in ('FLOAT','INT')):
            self.tokens.next();
            return NumberNode(tok)
        if(tok.type =="VAR"):
            self.tokens.next();
            return IdentifierNode(tok)
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



        return left


    def if_condition(self):
        left = self.expr()
        operation = self.tokens.current()
        self.tokens.next()
        right = self.expr()

        return IFCondition(left,operation,right)

    def if_statement(self):
        else_body = None
        self.read_token_pass('(','Missing ( in the beginnig of if condition ')

        condition = self.if_condition()

        self.read_token_pass(')','Missing ) in the end of if condition ')

        self.read_token_pass('{','Missing { in the beginnig of if body ')
        self.dele+=1

        body = self.statements();

        #self.read_token_pass('}','Missing } in the end of if body ')

        t = self.tokens.current()
        if(t.value == 'else'):
            self.tokens.next()

            self.read_token_pass('{','Missing { in the beginnig of if body ')
            self.dele+=1

            else_body = self.statements();

            #self.read_token_pass('}','Missing } in the end of if body ')


        return IfStatement(condition,body,else_body)



    def declarations(self):
        identifier_type = self.tokens.current()
        self.tokens.next()

        lis = [self.tokens.current()]
        self.tokens.next()
        while(self.tokens.current().value == ','):
            self.tokens.next()
            lis.append(self.tokens.current())
            self.tokens.next()

        self.read_token_pass(';',"Missing ; ");
        return Declaration(identifier_type,lis)



    def assignment(self):
        identifier = self.tokens.current()
        self.tokens.next()
        self.read_token_pass('=','Missing = ')
        expression = self.expr()
        self.read_token_pass(';','Missing ;')
        return Assignment(identifier,expression)




    def statements(self):
        left = None;right = None
        t = self.tokens.current()


        while(t.value!='END' and t.value!='}'):
            if(t.type == 'IF'):
                self.tokens.next()
                right = self.if_statement()
            elif(t.type in ('FLOAT','INT')):
                right = self.declarations();
            elif(t.type == 'VAR'):
                right = self.assignment()
            else:
                raise Exception("Syntax Error in line {}".format(t.line))

            left = Statement(left,right)
            t = self.tokens.current()

        if(t.value=='END'):
            return left
        elif(t.value=='}'):
            if(self.dele>0):
                self.dele-=1;
                self.tokens.next()
                return left
            else:
                raise Exception("un Expected } at end of line {}".format(t.line))




    def get_root(self):
        root = self.statements()
        if(self.tokens.current().type!="END"):
            raise Exception("Syntax Error")
        return root
