"""
Interpreter: AST 실행

변수 저장소 : dict {int: int} 형태
지정 안 된 변수는 기본값 0.
"""

from .ast_nodes import *

class RuntimeError_(Exception):
    pass

class Interpreter:
    def __init__(self):
        self.variables: dict[int, int] = {}

    def get_var(self, index: int) -> int:
        return self.variables.get(index, 0)

    def set_var(self, index: int, value: int):
        self.variables[index] = value

    def run(self, program: Program):
        for stmt in program.body:
            self.exec_stmt(stmt)
