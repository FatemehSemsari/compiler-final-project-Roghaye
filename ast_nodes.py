from dataclasses import dataclass
from typing import Optional, List, Union

@dataclass
class Program:
    decls: List["Decl"]
    stmts: List["Stmt"]

@dataclass
class Decl:
    type_name: str
    name: str
    init: Optional["Expr"]

@dataclass
class Assign:
    name: str
    value: "Expr"

@dataclass
class Return:
    value: Optional["Expr"]

@dataclass
class If:
    cond: "Expr"
    then_branch: "Stmt"
    else_branch: Optional["Stmt"]

@dataclass
class While:
    cond: "Expr"
    body: "Stmt"

@dataclass
class Block:
    stmts: List["Stmt"]

@dataclass
class Empty:
    pass

@dataclass
class BinOp:
    op: str
    left: "Expr"
    right: "Expr"

@dataclass
class UnaryOp:
    op: str
    operand: "Expr"

@dataclass
class Var:
    name: str

@dataclass
class IntLit:
    value: int

@dataclass
class FloatLit:
    value: float

Stmt = Union[Assign, Return, If, While, Block, Empty]
Expr = Union[BinOp, UnaryOp, Var, IntLit, FloatLit]
