class Token:
    def __init__(self,type,value=None,line=None):
        self.type=type
        self.value = value
        self.line=line

    def __str__(self):
        return "{} : {}".format(self.type,self.value)



class TokenArray:
    def __init__(self):
        self.lis = []
        self.cur_position=0
        self.cur_char = ""

    def push(self,val):
        self.lis.append(val)

    def next(self):
        if(self.cur_position+1 < len(self.lis)):
            self.cur_position+=1
        self.cur_char = self.lis[self.cur_position]

    def current(self):
        return self.lis[self.cur_position]


    def __str__(self):
        j=""
        for i in self.lis:
            j+=str(i)+"\n"
        return j

    def __len__(self):
        return len(lis)
