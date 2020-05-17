class NumberNode:
    def __init__(self,tok):
        self.tok = tok

    def __str__(self):
        return f'{self.tok}'

    def get_num(self):
        return self.tok.value

class IdentifierNode:
    def __init__(self,tok):
        self.tok = tok

    def __str__(self):
        return f'{self.tok}'

    def get_num(self):
        return self.tok.value

class BinOpNode:
    def __init__(self,left,op_tok,right):
        self.left = left
        self.op_tok = op_tok
        self.right = right

    def __str__(self):
        return f'[{self.left} {self.op_tok} {self.right}]'

class Statement:
    def __init__(self,left,right=None):
        self.left = left
        self.right = right

    def __str__(self):
        return f'[{self.left} {self.right}]'



class IfStatement:
    def __init__(self,if_condition,if_body,else_body=None):
        self.if_condition = if_condition
        self.if_body = if_body
        self.else_body = else_body

    def __str__(self):
        if(self.else_body):
            return f'[IF {self.if_condition} THEN {self.if_body} ELSE {self.else_body}]'
        return f'[IF {self.if_condition} THEN {self.if_body}]'


class IFCondition:
    def __init__(self,left_expression,comparision,right_expression):
        self.left_expression = left_expression
        self.comparison = comparision
        self.right_expression = right_expression

    def __str__(self):
        return f'[ {self.left_expression} {self.comparison} {self.right_expression} ]'



class Assignment:
    def __init__(self,identifier,expression):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return f'[{self.identifier} EQUAL {self.expression}]';


class Declaration:
    def __init__(self,declaration_type,identifiers):
        self.declaration_type = declaration_type
        self.identifiers = identifiers

    def __str__(self):
        return f'[{self.declaration_type}  ({",".join(map(str,self.identifiers))})]';
