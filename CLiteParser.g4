parser grammar CLiteParser;

options { tokenVocab=CLiteLexer; }

program
  : INT Main LPAREN RPAREN LBRACE declarations statements RBRACE EOF
  ;

declarations
  : declaration*
  ;

declaration
  : typeSpec ID (ASSIGN expression)? SEMI
  ;

typeSpec
  : INT
  | FLOAT
  | CHAR
  | BOOL
  ;

statements
  : statement*
  ;

statement
  : SEMI
  | block
  | assignment
  | ifStatement
  | whileStatement
  | returnStatement
  ;

returnStatement
  : RETURN expression? SEMI
  ;


block
  : LBRACE statements RBRACE
  ;

assignment
  : ID ASSIGN expression SEMI
  ;

ifStatement
  : IF LPAREN expression RPAREN statement (ELSE statement)?
  ;

whileStatement
  : WHILE LPAREN expression RPAREN statement
  ;

expression
  : conjunction (LOR conjunction)*
  ;

conjunction
  : equality (LAND equality)*
  ;

equality
  : relation ((EQ | NE) relation)?
  ;

relation
  : addition ((LT | LE | GT | GE) addition)?
  ;

addition
  : term ((PLUS | MINUS) term)*
  ;

term
  : factor ((MUL | DIV | MOD) factor)*
  ;

factor
  : (MINUS | NOT)? primary
  ;

primary
  : ID
  | IntegerLiteral
  | FloatingLiteral
  | LPAREN expression RPAREN
  ;
