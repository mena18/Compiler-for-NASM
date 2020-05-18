from LexicalAnalysis  import Lexer
from Parsing import Parser
from Intermidate_Codegeneration import IntermidateCodeGeneration
from Code_Optimization import CodeOptimization
from code_generation import CodeGeneration

"""
o = nasm -f elf64 -o output.o output.asm
man ld
ld output.o -o output
./output
"""

while True:
    input()
    f = open("read.txt",'r')
    a = f.read()

    # try:
    arr = Lexer(a).get_tokens();
    tree = Parser(arr).get_root();
    code,identifiers = IntermidateCodeGeneration(tree).get_code();
    code,identifiers = CodeOptimization(code,identifiers).get_code();
    #code.print_extra()
    CodeGeneration(code,identifiers)
    # except Exception as e:
    #     print(e)


    f.close()
