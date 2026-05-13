"""
AST 노드 정의

파서가 만들어내는 트리의 각 노드 타입.

"""

from dataclasses import dataclass, field

# 기본
@dataclass
class Program:
    """
    [전체 프로그램]
    I got this. ~ Pew 
    """
    body: list # Statement 리스트


# 값
@dataclass
class IntLiteral:
    """정수 리터럴  e.g. !!!@  → 2"""
    value: int


@dataclass
class VarGet:
    """변수 읽기  e.g. faah → 2번째 변수"""
    index: int


# 변수
@dataclass
class VarSet:
    """변수 대입  e.g. FaaH!!  → 2번째 변수에 2 대입"""
    index: int
    expr: object   # IntLiteral | VarGet | ...


# 출력
@dataclass
class PrintInt:
    """정수 출력  e.g. (Click)!!! → 3 출력"""
    expr: object   # IntLiteral | VarGet


@dataclass
class PrintChar:
    """문자 출력  e.g. F!@@@@@@!H → 'A' 출력 (2진수)"""
    binary: str   # ! = 1, @ = 0 로 구성된 문자열