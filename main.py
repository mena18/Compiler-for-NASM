from Compiler.LexicalAnalysis  import Lexer
from Compiler.Parsing import Parser
from Compiler.Intermidate_Codegeneration import IntermidateCodeGeneration
from Compiler.Code_Optimization import CodeOptimization
from Compiler.code_generation import CodeGeneration

"""
o = nasm -f elf64 -o output.o output.asm
man ld
ld output.o -o output
./output
"""
counter=0;

while True:
    counter+=1
    f = open("read.txt",'r')
    a = f.read()

    try:
        arr = Lexer(a).get_tokens();
        # print(arr)
        tree = Parser(arr).get_root();
        # print(tree)
        code,identifiers,constants = IntermidateCodeGeneration(tree).get_code();
        # print(identifiers)
        # print(constants)
        # code.print_extra()
        # print("-"*50)
        code,identifiers,constants,tempmap = CodeOptimization(code,identifiers,constants).get_code();
        # print(identifiers)
        # print(constants)
        # code.print_extra()
        print("-"*50)
        print(f"[{counter}] : ",end="\n\n")
        CodeGeneration(code,identifiers,constants,tempmap)
        print("-"*50)
    except Exception as e:
        print(e)


    f.close()
    input()
