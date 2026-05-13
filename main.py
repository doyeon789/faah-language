import sys
from fah.lexer import Lexer, LexerError
from fah.parser import Parser, ParseError
from fah.interpreter import Interpreter, RuntimeError_

def run_file(path: str):
    
    try:
        source = open(path, encoding='utf-8').read()
    except FileNotFoundError:
        print(f"[ERRPR] Can't find files: {path}" )

    # Lexing 
    try:
        tokens = Lexer(source).tokenize()
    except LexerError as e:
        print(f"[Lexer Error] {e}")
        sys.exit(1)


    # Parshing
    try:
        ast = Parser(tokens).parse()
    except ParseError as e:
        print(f"[Parser Error] {e}")
        sys.exit(1)

    # Interpreting <- 인터프린팅




if __name__ == '__main__':
    args = sys.args[1:]

    # -- <= 콘솔 명령어 나중에 만들기 위해서
    # -- 제외한 파일 불러오기
    files= [a for a in args if not a.startswith('--')]

    run_file(files)