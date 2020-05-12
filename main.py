from LexicalAnalysis  import Lexer

while True:
    a = input("Basic > ")

    arr = Lexer(a).get_tokens();
    print(arr)
