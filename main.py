from LexicalAnalysis  import Lexer
from Parsing import Parser
from Intermidate_Codegeneration import IntermidateCodeGeneration

while True:
    input()
    f = open("read.txt",'r')
    a = f.read()

    # try:
    arr = Lexer(a).get_tokens();
    tree = Parser(arr).get_root();
    code = IntermidateCodeGeneration(tree).get_code();
    print("\n".join(code))
    # except Exception as e:
    #     print(e)


    f.close()
