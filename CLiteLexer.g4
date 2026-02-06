lexer grammar CLiteLexer;

LBRACE  : '{' ;
RBRACE  : '}' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACK  : '[' ;
RBRACK  : ']' ;
SEMI    : ';' ;
COMMA   : ',' ;
ASSIGN  : '=' ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
MOD     : '%' ;
INC     : '++' ;
DEC     : '--' ;
ARROW   : '->' ;
DOT     : '.' ;
AND     : '&' ;
OR      : '|' ;
XOR     : '^' ;
NOT     : '!' ;
INV     : '~' ;
SHL     : '<<' ;
SHR     : '>>' ;
LE      : '<=' ;
GE      : '>=' ;
EQ      : '==' ;
NE      : '!=' ;
LT      : '<' ;
GT      : '>' ;
LAND    : '&&' ;
LOR     : '||' ;
QUES    : '?' ;
COLON   : ':' ;
Main    : 'main';
BREAK     : 'break' ;
CASE      : 'case' ;
CHAR      : 'char' ;
CONST     : 'const' ;
CONTINUE  : 'continue' ;
DEFAULT   : 'default' ;
DO        : 'do' ;
DOUBLE    : 'double' ;
ELSE      : 'else' ;
ENUM      : 'enum' ;
EXTERN    : 'extern' ;
FLOAT     : 'float' ;
FOR       : 'for' ;
GOTO      : 'goto' ;
IF        : 'if' ;
INLINE    : 'inline' ;
INT       : 'int' ;
LONG      : 'long' ;
REGISTER  : 'register' ;
RETURN    : 'return' ;
SHORT     : 'short' ;
SIGNED    : 'signed' ;
SIZEOF    : 'sizeof' ;
STATIC    : 'static' ;
STRUCT    : 'struct' ;
SWITCH    : 'switch' ;
UNION     : 'union' ;
UNSIGNED  : 'unsigned' ;
VOID      : 'void' ;
WHILE     : 'while' ;

ID : [a-zA-Z_][a-zA-Z_0-9]* ;

IntegerLiteral
  : HexConstant IntegerSuffix?
  | OctalConstant IntegerSuffix?
  | DecimalConstant IntegerSuffix?
  ;

fragment DecimalConstant : '0' | [1-9] [0-9]* ;
fragment HexConstant     : '0' [xX] [0-9a-fA-F]+ ;
fragment OctalConstant   : '0' [0-7]+ ;


fragment IntegerSuffix
  : [uU] [lL]? [lL]?    
  | [lL] [lL]? [uU]?    
  ;

FloatingLiteral
  : ([0-9]* '.' [0-9]+ | [0-9]+ '.' [0-9]*) ExponentPart? FloatSuffix?
  | [0-9]+ ExponentPart FloatSuffix?
  ;

fragment ExponentPart : [eE] [+-]? [0-9]+ ;
fragment FloatSuffix  : [fFlL] ;

CharLiteral
  : '\'' ( ESC | ~['\\\r\n] )+ '\''
  ;

STRING
  : '"' ( ESC | ~["\\\r\n] )* '"'
  ;

fragment ESC
  : '\\' (
        [btnfrva?"'\\]      
      | 'x' [0-9a-fA-F]+    
      | [0-7] [0-7]? [0-7]? 
    )
  ;

LINE_COMMENT  : '//' ~[\r\n]*      -> channel(HIDDEN) ;
BLOCK_COMMENT : '/*' .*? '*/'      -> channel(HIDDEN) ;
WS : [ \t\r\n\f]+ -> channel(HIDDEN) ;
