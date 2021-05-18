import ply.yacc as yacc 
import sys

from gerador_lex import tokens 

#Production rules
def p_Comandos(p):
    "Comandos : Comandos Comando"
    pass

def p_Comando_unico(p):
    "Comandos : Comando"
    pass

def p_Comando(p):
    """
    Comando : Ler
           |  Escrever
           |  Despejar
           |  Atrib
           |  Exp
    """
    pass

def p_Exp_add(p):
    "Exp : Exp '+' Termo" 
    p[0] = p[1] + p[3]
    print(p[0])
    ger = str(p[1]) + ' ADD ' + str(p[3])
    file_vm.write(ger)
    file_vm.close()

def p_Exp_sub(p):
    "Exp : Exp '-' Termo" 
    p[0] = p[1] - p[3]
    print(p[0])

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mul(p):
    "Termo : Termo '*' Factor"
    p[0] = p[1] * p[3]
    print(p[0])

def p_Termo_div(p):
    "Termo : Termo '/' Factor"
    if(p[3] != 0):
        p[0] = p[1] / p[3]
        print(p[0])
    else:
        print ("Erro: divisao por 0, a continuar com 0...)")
        p[0] =0

def p_Termo_factor(p):
    "Termo : Factor"
    p[0] = p[1]

def p_Factor_id(p):
    "Factor : id"
    p[0] = p.parser.registers.get(p[1])

def p_Factor_num(p):
    "Factor : num"
    p[0] = int(p[1])

def p_Factor_group(p):
    "Factor : '(' Exp ')' "
    p[0] = p[2]


def p_Ler(p):
    "Ler : '?' id"
    valor = input("Introduza o valor inteiro: ")
    p[0] = p.parser.registers.update({p[2]: int(valor)})
    print(p[0])

def p_Escrever(p):
    "Escrever : '!' id"
    print(p[2])

def p_Despejar(p):
    "Despejar : '!' '!'"
    print(p.parser.registers)

    
def p_Atrib(p):
    "Atrib : id '=' Exp"
    p.parser.registers.update({p[1]: p[3]})
    print(p[0])

#Error value for syntax errors
def p_error(p):
    print("Syntax error in input!")

#Build the parser
parser =  yacc.yacc()

# my state
# dicionario inicializado a vazio
parser.registers = {}

#GENERATE file.vm
file = 'file.vm'
file_vm = open(file, "w+")
# reading input
for linha in sys.stdin:
    result = parser.parse(linha)


