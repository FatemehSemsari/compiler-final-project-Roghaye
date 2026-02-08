from c_tokenize import Tokenizer
import os

def compare_codes(file1, file2):
    
    tokenizer = Tokenizer()

    tokens1 = tokenizer.tokenize_file(file1)
    tokens2 = tokenizer.tokenize_file(file2)
    
    text1 = [t["text"] for t in tokens1["tokens"]]
    text2 = [t["text"] for t in tokens2["tokens"]]
    
    set1 = set(text1)
    set2 = set(text2)
    
    common = len(set1 & set2)   
    total = len(set1 | set2)   
    
    if total == 0:
        score1 = 1.0  
    else:
        score1 = round(common / total,1)
    
    compare_len = min(50, len(text1), len(text2))
    
    if compare_len == 0:
        score2 = 0
    else:
        same_order = 0
        for i in range(compare_len):
            if text1[i] == text2[i]:
                same_order += 1
        score2 = round(same_order / compare_len,1)
 
    final_score = round((score1 + score2) / 2,1)
  
    result = {
        "token_numbers" : {
            "code_A": len(text1),
            "code_B": len(text2)
        }, 
        "common_tokens": common,
        "total": total,
        "common_tokens_score": score1,
        "Number_of_tokens_with_the_same_order":same_order,
        "same_order_score":score2,
        "final_score":final_score
    }
    
    return result