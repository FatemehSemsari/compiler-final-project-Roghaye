from pathlib import Path
from c_tokenize import Tokenizer

def run(file_path: str):
    tokenizer = Tokenizer()
    result = tokenizer.tokenize_file(file_path)
    tokens = result["tokens"]
    errors = result["errors"]

    print("\n====", file_path, "====")
    print("tokens:", len(tokens), "errors:", len(errors))


    for t in tokens[:12]:
        print(f"{t['type']:>14}  text={t['text']!r}  norm={t['norm']!r}  @({t['line']}:{t['column']})")

    if errors:
        print("---- errors ----")
        for e in errors:
            print(f"line {e['line']} col {e['column']}: {e['message']}")

if __name__ == "__main__":
    for f in ["samples/ok1.c", "samples/ok_comments.c", "samples/ok_strings.c", "samples/bad1.c"]:
        run(f)
