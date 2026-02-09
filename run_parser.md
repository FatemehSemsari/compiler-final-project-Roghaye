<div dir=rtl>
برای اینکه بتونین parse tree رو ببینین این دستور ها رو اجرا کنین :
<br>
<div dir=ltr>
1)cd java
</div>
<br>
<div dir=ltr>
2)javac -cp "C:\Users\Asus\Downloads\Antler\Antler\antlr-4.13.2-complete.jar;." *.java
</div>
<br>
<div dir=ltr>
3)java -cp "C:\Users\Asus\Downloads\Antler\Antler\antlr-4.13.2-complete.jar;." org.antlr.v4.gui.TestRig CLite program -gui ..\samples\ok1.c
</div>
<br>
داخل کوتیشن ها آدرس فایل .jar خودتون رو بنویسین
<br>
برای اینکه کد AST رو به صورت json ببینین این دستورات رو بزنین :
<br>
<div dir=ltr>
1)cd..
</div>
<br>
<div dir=ltr>
2)python parse_to_ast.py samples/ok1.c
</div>
<br>
</div>