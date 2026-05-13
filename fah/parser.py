"""
Parser: Token list -> AST

문법 :
  program  ::= PROGRAM_START stmt* PROGRAM_END
  stmt     ::= var_set | NEWLINE
"""

from .tokens import Token, TokenType
from .ast_nodes import *

class ParseError(Exception):
    pass

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.pos = 0

    # 헬퍼
    def peek(self) -> Token:
        return self.tokens[self.pos]

    def advance(self) -> Token:
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def expect(self, ttype: TokenType) -> Token:
        tok = self.advance()
        if tok.type != ttype:
            raise ParseError(
                f"line {tok.line}: Expext '{ttype.name}' But '{tok.type.name}({tok.value})' appear"
            )
        return tok

    def skip_newlines(self):
        while self.peek().type == TokenType.NEWLINE:
            self.advance()


    def parse_var_set(self) -> VarSet:
        tok = self.advance()  # FAH_SET
        index = getattr(tok, 'index', tok.value.count('a'))
        expr  = self.parse_expr()
        return VarSet(index=index, expr=expr)

    def parse_expr(self):
        tok = self.peek()

        # 정수 리터럴: ! 또는 @ 가 하나 이상
        if tok.type in (TokenType.INT_PLUS, TokenType.INT_MINUS):
            return self.parse_int_literal()

        # 변수 읽기
        if tok.type == TokenType.FAH_GET:
            t = self.advance()
            return VarGet(index=getattr(t, 'index', t.value.count('a')))

        # 아무것도 없으면 0
        return IntLiteral(value=0)

    # 파싱
    def parse(self) -> Program:
        self.expect(TokenType.PROGRAM_START)
        self.skip_newlines()

        body = []
        while self.peek().type not in (TokenType.PROGRAM_END, TokenType.EOF):
            stmt = self.parse_stmt()
            if stmt is not None:
                body.append(stmt)
            self.skip_newlines()

        if self.peek().type == TokenType.EOF:
            raise ParseError("프로그램이 'Pew' 없이 끝났어요!")
        self.expect(TokenType.PROGRAM_END)

        return Program(body=body)
    
    def parse_stmt(self):
        tok = self.peek()

        if tok.type == TokenType.FAH_SET:
            return self.parse_var_set()

        elif tok.type == TokenType.UNKNOWN:
            raise ParseError(f"line {tok.line}: unknown token '{tok.value}'")
        
        elif tok.type == TokenType.PRINT_INT:
            return self.parse_print_int()

        elif tok.type == TokenType.PRINT_CHAR:
            return self.parse_print_char()

        else:
            self.advance()
            return None
    
    def parse_int_literal(self) -> IntLiteral:
        value = 0
        while self.peek().type in (TokenType.INT_PLUS, TokenType.INT_MINUS):
            t = self.advance()
            value += 1 if t.type == TokenType.INT_PLUS else -1
        return IntLiteral(value=value)
    

    def parse_print_int(self) -> PrintInt:
        self.advance()
        expr = self.parse_expr()
        return PrintInt(expr=expr)
    

    def parse_print_char(self) -> PrintChar:
        tok = self.advance()
        newline = tok.value.endswith('H!')  # H! 로 끝나면 줄바꿈
        inner = tok.value[1:]
        inner = inner[:-1] if not newline else inner[:-2]
        binary = inner.replace('!', '1').replace('@', '0')
        return PrintChar(binary=binary, newline=newline)