from utils.Tokens import *
from utils.TreeNodes import *
from utils.intermidatecodes import *

class CodeOptimization:
    def __init__(self,input_code,input_identifiers,input_constants):
        self.input_code = input_code
        self.input_identifiers = input_identifiers
        self.input_constants = input_constants
        self.output_code = self.input_code
        self.output_identifiers = self.input_identifiers
        self.output_constants = self.input_constants
        self.optimize();


    def organize_labels(self,codearray):
        for index,code in enumerate(codearray.code):
            if(code.type=='label'):
                codearray.combine_next(index)
        return codearray

    def remove_temp(self,codearray):
        for index,code in enumerate(codearray.code):
            if(index>0 and isinstance(code,AssignmentCode) and isinstance(codearray.code[index-1],AssignmentCode)):
                last_loaded=codearray.code[index-1].var
                if(code.left == last_loaded):
                    codearray.code[index] = ChangeCode(last_loaded,code.op,code.right)
                elif((code.right==last_loaded and code.op in '+*')):
                    codearray.code[index] = ChangeCode(last_loaded,code.op,code.left)


        return codearray

    def optimize(self):
        #self.output_code = self.remove_temp(self.input_code)
        pass



    def get_code(self):
        return self.output_code,self.output_identifiers,self.output_constants
