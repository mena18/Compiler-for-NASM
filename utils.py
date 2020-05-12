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
        self.counter=0

    def push(self,val):
        self.lis.append(val)

    def get(self):
        self.counter+=1
        return self.list[self.counter-1]

    def __str__(self):
        j=""
        for i in self.lis:
            j+=str(i)+"\n"
        return j
