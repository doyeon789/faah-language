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