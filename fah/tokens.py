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

