from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile
import os
from token_similarity import compare_codes
from parse_to_ast import parser_to_ast
from subtree_matching import sub_matching

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def send_result():
    data= request.get_json()
    code1= data["code1"]
    code2= data["code2"]

    with tempfile.NamedTemporaryFile(delete=False, suffix=".c") as f1:
        f1.write(code1.encode())
        path1 = f1.name
    with tempfile.NamedTemporaryFile(delete=False, suffix=".c") as f2:
        f2.write(code2.encode())
        path2 = f2.name
    TokenResult = compare_codes(path1,path2)
    AstResult= sub_matching(parser_to_ast(path1),parser_to_ast(path2))

    finalResult= {**TokenResult,**AstResult}
    os.remove(path1)
    os.remove(path2)

    return jsonify(finalResult)

if __name__ == "__main__":
    app.run(debug=True)