import ply.lex as lex

tokens = ['num','id']
literals = ['(',')','+','-','*','/','?','!','=']

t_num = r'\d+'
t_id = r'[a-z]' #apenas 26 registos

t_ignore = "\t\n"

def t_error(t):
    print("Carater ilegal: ", t.value[0])
    t.lexer.skip(1)

#build the lexer

lexer = lex.lex()
