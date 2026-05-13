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

    # 실행
    def run(self, program: Program):
        for stmt in program.body:
            self.exec_stmt(stmt)

    # 문장 실행
    def exec_stmt(self, node):
        if isinstance(node, VarSet):
            value = self.eval_expr(node.expr)
            self.set_var(node.index, value)

        elif isinstance(node, PrintInt):
            value = self.eval_expr(node.expr)
            print(value)

        else:
            raise RuntimeError_(f"알 수 없는 노드: {type(node)}")
        
    # 식 평
    def eval_expr(self, node) -> int:
        if isinstance(node, IntLiteral):
            return node.value

        if isinstance(node, VarGet):
            return self.get_var(node.index)

        raise RuntimeError_(f"알 수 없는 식 노드: {type(node)}")
