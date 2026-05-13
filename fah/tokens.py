from enum import Enum, auto

class TokenType(Enum):
    # 프로그램 구조
    PROGRAM_START = auto() # I got this.
    PROGRAM_END = auto() # Pew

    # 키워드

    # 기타
    NEWLINE = auto()
    EOF = auto()
    UNKNOWN = auto()

class Token:
    def __init__(self, type: TokenType, value:str, line:int=0):
        self.type = type
        self.value = value
        self.line = line
    
    def __repr__(self):
        return f'Token({self.type}, {self.value!r}, line={self.line})'