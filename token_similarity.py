from c_tokenize import Tokenizer
import os

def compare_codes(file1, file2):
    
    tokenizer = Tokenizer()

    tokens1 = tokenizer.tokenize_file(file1)
    tokens2 = tokenizer.tokenize_file(file2)
    
    text1 = [token.get("text", "") for token in tokens1]
    text2 = [token.get("text", "") for token in tokens2]
        
    set1 = set(text1)
    set2 = set(text2)
    
    common = len(set1 & set2)   
    total = len(set1 | set2)   
    
    if total == 0:
        score1 = 1.0  
    else:
        score1 = common / total
    
    compare_len = min(50, len(text1), len(text2))
    
    if compare_len == 0:
        score2 = 0
    else:
        same_order = 0
        for i in range(compare_len):
            if text1[i] == text2[i]:
                same_order += 1
        score2 = same_order / compare_len
 
    final_score = (score1 + score2) / 2
  
    result = {
        "token_numbers" : {
            "code A": len(text1),
            "code B": len(text2)
        }, 
        "common_tokens": common,
        "total": total,
        "common_tokens_score": score1,
        "Number_of_tokens_with_the_same_order":same_order,
        "same_order_score":score2,
        "final_score":final_score
    }
    
    return final_score