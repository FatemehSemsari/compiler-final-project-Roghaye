import json
from dataclasses import asdict, is_dataclass
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from antlr4 import FileStream, CommonTokenStream
from generated.CLiteLexer import CLiteLexer
from generated.CLiteParser import CLiteParser
from ast_builder import ASTBuilder
from dataclasses import fields, is_dataclass

def to_jsonable(x):
    if is_dataclass(x):
        d = {"_type": x.__class__.__name__}
        for f in fields(x):
            d[f.name] = to_jsonable(getattr(x, f.name))
        return d
    if isinstance(x, list):
        return [to_jsonable(i) for i in x]
    return x

def parser_to_ast(path):
    lexer = CLiteLexer(FileStream(path, encoding="utf-8"))
    tokens = CommonTokenStream(lexer)
    parser = CLiteParser(tokens)
    tree = parser.program()

    ast = ASTBuilder().visit(tree)
    return ast


# def main(path: str):
#     lexer = CLiteLexer(FileStream(path, encoding="utf-8"))
#     tokens = CommonTokenStream(lexer)
#     parser = CLiteParser(tokens)
#     tree = parser.program()

#     ast = ASTBuilder().visit(tree)
#     print(json.dumps(to_jsonable(ast), ensure_ascii=False, indent=2))

# if __name__ == "__main__":
#     main(sys.argv[1])
