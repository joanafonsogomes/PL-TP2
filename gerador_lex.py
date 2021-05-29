import ply.lex as lex

reserved = {
    'print' : 'PRINT',
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'for' : 'FOR',
    'fi' : 'FI',
    'rof' : 'ROF',
    'write' : 'WRITE',
    'read'  :'READ',
    'start' :'START',
    'end' : 'END',
 }
tokens = ['num','id','frase'] + list(reserved.values())
literals = ['(',')','!','>','<','+','-','*','/',';','=',']','[','%']

t_num = r'\d+'

def t_id(t):
     r'[a-z][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'id')    # Check for reserved words
     return t

def t_frase(t):
     r'\"[a-zA-Z_0-9 \\]+\"'
     t.type = reserved.get(t.value,'frase')    # Check for reserved words
     return t

t_ignore = "\t\n"

def t_error(t):
    #print("Carater ilegal: ", t.value[0])
    t.lexer.skip(1)

#build the lexer

lexer = lex.lex()
