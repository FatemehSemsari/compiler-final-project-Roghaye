from antlr4 import FileStream, CommonTokenStream, Token
from CLiteLexer import CLiteLexer


class Tokenizer:

    def __init__(self):
        pass

    _NORM_BY_TYPE = {
        "ID": "<ID>",
        "IntegerLiteral": "<INT>",
        "FloatingLiteral": "<FLOAT>",
        "STRING": "<STR>",
        "CharLiteral": "<CHAR>",
    }


    def token_to_dict(self, tok, lexer: CLiteLexer):
        token_name = None
        if 0 <= tok.type < len(lexer.symbolicNames):
            token_name = lexer.symbolicNames[tok.type]
        if not token_name:
            token_name = str(tok.type)

        return {
            "type": token_name,
            "type_id": tok.type,
            "text": tok.text,
            "line": tok.line,
            "column": tok.column,
            "start": tok.start,
            "stop": tok.stop,
            "channel": tok.channel,
        }


    def normalize_tokens(self, tokens: list[dict]):
        normal_tokens = []
        for t in tokens:
            tok_dict = dict(t)
            token_type = tok_dict.get("type")
            raw_text = tok_dict.get("text")

            norm = Tokenizer._NORM_BY_TYPE.get(token_type, raw_text)
            tok_dict["norm"] = norm

            normal_tokens.append(tok_dict)

        return normal_tokens


    def tokenize_file(self, input_path):
        lexer = CLiteLexer(FileStream(input_path, encoding="utf-8"))
        stream = CommonTokenStream(lexer)
        stream.fill()

        tokens = []
        errors = []

        for t in stream.tokens:
            if t.type == Token.EOF:
                continue
            if t.text is not None and getattr(lexer, "symbolicNames", None):
                tname = lexer.symbolicNames[t.type] if 0 <= t.type < len(lexer.symbolicNames) else str(t.type)
                if tname == "ERROR_CHAR":
                    errors.append({
                        "message": f"Invalid character: {t.text!r}",
                        "text": t.text,
                        "line": t.line,
                        "column": t.column,
                    })
                    continue
            if t.channel != Token.DEFAULT_CHANNEL:
                continue
            tokens.append(self.token_to_dict(t, lexer))

        tokens = self.normalize_tokens(tokens)

        return {"tokens": tokens, "errors": errors}
