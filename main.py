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

"""
remove extra files and organize existing files
remove float
add print function
add forloop
some optimization
"""

while True:
    input()
    f = open("read.txt",'r')
    a = f.read()

    # try:
    arr = Lexer(a).get_tokens();
    tree = Parser(arr).get_root();
    code,identifiers,constants = IntermidateCodeGeneration(tree).get_code();
    code,identifiers,constants = CodeOptimization(code,identifiers,constants).get_code();
    # print(identifiers)
    # print(constants)
    # code.print_extra()
    CodeGeneration(code,identifiers,constants)
    # except Exception as e:
    #     print(e)


    f.close()
