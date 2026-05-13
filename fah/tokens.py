from enum import Enum, auto

class TokenType(Enum):
    # 프로그램 구조
    PROGRAM_START = auto() # I got this.
    PROGRAM_END = auto() # Pew

    # 변수
    FAH_SET = auto() # F(a*)H  - 대입
    FAH_GET = auto()  # f(a*)h  - 사용

    # 츨력
    PRINT_INT = auto()
    PRINT_CHAR = auto()

    # 정수 리터럴
    INT_PLUS  = auto() # !  (+1)
    INT_MINUS = auto() # @  (-1)

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