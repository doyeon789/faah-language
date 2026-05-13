"""
Laxer : 소스 코드 문자열 -> Token 리스트 

I got this.     -> PROGRAM_START
Pew             -> PROGRAM_END
줄바꿈           -> NEWLINE

"""

import re
from .tokens import Token, TokenType

# 토큰 패턴 
TOKEN_PATTERNS = [
    (TokenType.PROGRAM_START, r'I got this\.'),
    (TokenType.PROGRAM_END, r'Pew'),
    (TokenType.NEWLINE, r'\n'),
    (TokenType.UNKNOWN, r'.'),
]

# 각 토큰 패턴에 이름 붙이기: (?P<T0>패턴)|(?P<T1>패턴)|...
# 소스코드를 한 번만 훑어서 모든 토큰을 찾기 위해 하나로 합침
MASTER_PATTERN = re.compile(
    '|'.join(f'(?P<T{i}>{p})' for i, (_, p) in enumerate(TOKEN_PATTERNS))
)

class LexerError(Exception):
    pass

class Lexer:
    def __init__(self, source: str):
        self.source = source

    def tokenize(self) -> list[Token]:
        tokens = []
        line = 1

        for m in MASTER_PATTERN.finditer(self.source):
            for i, (ttype, _) in enumerate(TOKEN_PATTERNS):
                group = m.group(f'T{i}')
                if group is None:
                    continue

                if ttype == TokenType.NEWLINE:
                    tokens.append(Token(TokenType.NEWLINE, '\\n', line))
                    line += 1

                elif ttype == TokenType.UNKNOWN:
                    # 공백은 조용히 무시, 나머지는 경고
                    if group.strip():
                        tokens.append(Token(TokenType.UNKNOWN, group, line))

                else:
                    tokens.append(Token(ttype, group, line))
                break
        
        tokens.append(Token(TokenType.EOF, '', line))
        return tokens