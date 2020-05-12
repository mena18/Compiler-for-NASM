from LexicalAnalysis  import Lexer
from Parsing import Parser

while True:
    a = input("Basic > ")
    try:
        arr = Lexer(a).get_tokens();
        tree = Parser(arr).get_root();
        print(tree)
    except Exception as e:
        print(e)
