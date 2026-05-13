"""
Parser: Token list -> AST

문법 :
  program  ::= PROGRAM_START stmt* PROGRAM_END
  stmt     ::= var_set | NEWLINE
"""

from .tokens import Token, TokenType

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