import ply.lex as lex

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'for' : 'FOR',
    'fi' : 'FI',
    'rof' : 'ROF',
    'write' : 'WRITE',
    'print' : 'PRINT',
    'read'  :'READ',
    'start' :'START',
    'end' : 'END',
 }
tokens = ['num','id','frase'] + list(reserved.values())
literals = ['(',')','>','<','+','-','*','/','?','!',';','=',']','[']

def t_id(t):
     r'[a-z][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'id')    # Check for reserved words
     return t
t_num = r'\d+'
t_frase = r'".*"'
t_ignore = "\t\n"

def t_error(t):
    #print("Carater ilegal: ", t.value[0])
    t.lexer.skip(1)

#build the lexer

lexer = lex.lex()
