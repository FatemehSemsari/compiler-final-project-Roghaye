# فاز ۲ پروژه کامپایلر - مقایسه دو کد C
# نسخه ساده و قابل فهم

from c_tokenize import Tokenizer
import os

def compare_codes(file1, file2):
    
    print(f"در حال مقایسه: {file1} با {file2}")
    
    tokenizer = Tokenizer()

    tokens1 = tokenizer.tokenize_file(file1)
    tokens2 = tokenizer.tokenize_file(file2)
    
    text1 = [token.get("text", "") for token in tokens1]
    text2 = [token.get("text", "") for token in tokens2]
    
    print(f"تعداد توکن‌ها: {len(text1)} و {len(text2)}")
    
    # روش اول: توکن‌های مشترک
    set1 = set(text1)
    set2 = set(text2)
    
    common = len(set1 & set2)   
    total = len(set1 | set2)   
    
    if total == 0:
        score1 = 1.0  
    else:
        score1 = common / total
    
    print(f"\nتوکن‌های مشترک: {common} از {total}")
    print(f"امتیاز مشترک: {score1:.1%}")
    
    # روش دوم: ترتیب توکن‌ها
    compare_len = min(50, len(text1), len(text2))
    
    if compare_len == 0:
        score2 = 0
    else:
        same_order = 0
        for i in range(compare_len):
            if text1[i] == text2[i]:
                same_order += 1
        score2 = same_order / compare_len
    
    print(f"\nمقایسه ترتیب (اولین {compare_len} توکن):")
    print(f"تعداد با ترتیب مشابه: {same_order}")
    print(f"امتیاز ترتیب: {score2:.1%}")
    
    # امتیاز نهایی: میانگین دو روش
    final_score = (score1 + score2) / 2
    
    print(f"\n امتیاز نهایی: {final_score:.1%}")
    
    if final_score > 0.7:
        print("💡 نتیجه: خیلی شبیه")
    elif final_score > 0.4:
        print("💡 نتیجه: نسبتاً شبیه")
    else:
        print("💡 نتیجه: متفاوت")
    
    return final_score

def main():

    print("=" * 40)
    print("مقایسه کدهای C - فاز ۲ پروژه کامپایلر")
    print("=" * 40)
    ه
    if os.path.exists("samples"):
        files = [f for f in os.listdir("samples") if f.endswith('.c')]
        
        if len(files) >= 2:
            print(f"\nفایل‌های پیدا شده در samples/:")
            for i, f in enumerate(files[:5], 1):
                print(f"  {i}. {f}")
            
            # از اولین دو فایل استفاده کن
            file1 = os.path.join("samples", files[0])
            file2 = os.path.join("samples", files[1])
            
            print(f"\nاستفاده از: {files[0]} و {files[1]}")
            
            try:
                # مقایسه
                score = compare_codes(file1, file2)
                
                # ذخیره نتیجه 
                with open("result.txt", "w", encoding="utf-8") as f:
                    f.write(f"شباهت: {score:.1%}\n")
                    f.write(f"بین: {file1} و {file2}\n")
                
                print(f"\n نتیجه در فایل 'result.txt' ذخیره شد")
                
            except Exception as e:
                print(f"\nخطا: {e}")
                
        else:
            print("فایل .c کافی در پوشه samples نیست")
    else:
        print("پوشه samples پیدا نشد")

if __name__ == "__main__":
    main()