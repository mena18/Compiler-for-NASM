from utils import Token,TokenArray

keyword = ['if', 'for', 'while','int','float']
comparison = ["==", ">", "<", "<=", "!=", '>=']

delimiters = {
    '(': "L1",
    ')': "R1",
    '{': "L2",
    '}': "R2",
    ';': 'SEMICOLON'
}
error = ['!', '@', '$', '&', '~', '`']


seperate_operations="(){ }[]\t\n+-*/=><"
operators = ['+', '-', '*', '/', '%', '^', '=', '&', '|', '==', '>', '<', '!', '++', '--', '+=', '!=', '-=', '&&',
            '||', '>=', '<=']



def valid_word(word):
    return word.isdigit() or word.isalpha() or word =='_'


class Lexer:
    def __init__(self,file):
        self.file = list(file)+['END']
        self.array = TokenArray()
        self.cur_position=0
        self.cur_char = self.file[0]
        self.line = 1
        self.create_tokens()

    def next(self):
        if(self.cur_position+1 < len(self.file)):
            self.cur_position+=1
        self.cur_char = self.file[self.cur_position]



    def make_operators(self):
        t = Token("OPERATOR",self.cur_char,self.line)
        self.next()
        self.array.push(t)

    def make_delimiter(self):
        t = Token(delimiters[self.cur_char],self.cur_char,self.line)
        self.next()
        self.array.push(t)

    def make_word(self):
        cur=""
        while(self.cur_char!='END' and valid_word(self.cur_char)):
            cur+=self.cur_char
            self.next()

        if(cur in keyword):
            t = Token(cur.upper(),cur,self.line)
            self.array.push(t)
        else:
            t = Token("VAR",cur,self.line)
            self.array.push(t)

    def make_number(self):
        num=""
        dot_count=0

        while(self.cur_char!='END' and self.cur_char in '0123456789.'):
            if(self.cur_char=="."):
                if(dot_count==1):
                    raise Exception("many . in number in line {}".format(self.line));
                else:
                    dot_count=1

            num+=self.cur_char
            self.next()

        if(dot_count ==1):
            if(num[-1]=='.'):num+='0'
            t = Token('FLOAT',num,self.line)
        else:
            t = Token('INT',num,self.line)

        self.array.push(t)


    def create_tokens(self):
        while(self.cur_char != "END"):
            if(self.cur_char =='\n'):
                self.line+=1
                self.next()
            elif(self.cur_char in '\t '):
                self.next()
            elif(self.cur_char in operators):
                self.make_operators()
            elif(self.cur_char in delimiters):
                self.make_delimiter()
            elif(self.cur_char.isalpha()):
                self.make_word()
            elif(self.cur_char.isdigit()):
                self.make_number()
            else:
                raise Exception("unknown char {} in line {}".format(self.cur_char,self.line));



    def get_tokens(self):
        return self.array
