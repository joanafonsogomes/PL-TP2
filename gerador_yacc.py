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
           |  End
    """
    pass
    

def p_Exp_add(p):
    "Exp : Exp '+' Termo" 
    p[0] = p[1] + p[3]
    print(p[0])
    ger = 'PUSHI ' + str(p[1])+ '\n'+ 'PUSHI ' +str(p[3])+ '\n'+ 'ADD\n'
    file_vm.write(ger)

def p_Exp_sub(p):
    "Exp : Exp '-' Termo" 
    p[0] = p[1] - p[3]
    print(p[0])
    ger = 'PUSHI ' + str(p[1])+ '\n'+ 'PUSHI ' +str(p[3])+ '\n'+ 'SUB\n'
    file_vm.write(ger)

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]

def p_Termo_mul(p):
    "Termo : Termo '*' Factor"
    p[0] = p[1] * p[3]
    print(p[0])
    ger = 'PUSHI ' + str(p[1])+ '\n'+ 'PUSHI ' +str(p[3])+ '\n'+ 'MUL\n'
    file_vm.write(ger)
def p_Termo_div(p):
    "Termo : Termo '/' Factor"
    if(p[3] != 0):
        p[0] = p[1] / p[3]
        print(p[0])
        ger = 'PUSHI ' + str(p[1])+ '\n'+ 'PUSHI ' +str(p[3])+ '\n'+ 'DIV\n'
        file_vm.write(ger)
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
    global i
    flag=1
    valor = input("Introduza o valor inteiro: ")
    for key in p.parser.registers.keys():
        if key == p[2]:
            ger = 'PUSHI 0\nPUSHI ' +valor+ '\n'+ 'STOREG '+ str(p.parser.registers.get(key)) +'\n'
            flag=0
            file_vm.write(ger)
    if(flag==1):
        p.parser.registers.update({p[2]: i})
        ger = 'PUSHI 0\nPUSHI ' +valor+ '\n'+ 'STOREG '+ str(i) +'\n'
        i= i+1
        file_vm.write(ger)

def p_Escrever(p):
    "Escrever : '!' id"
    for key in p.parser.registers.keys():
        if key == p[2]:
            ger= 'PUSHG ' +str(p.parser.registers.get(key)) +'\nWRITEI\n'
            file_vm.write(ger)

def p_Despejar(p):
    "Despejar : '!' '!'"
    print(p.parser.registers)

def p_Atrib(p):
    "Atrib : id '=' Exp"
    p.parser.registers.update({p[1]: p[3]})
    

def p_End(p):
    "End : '!' '!' '!'"
    # dá erro fp=sp, os apontadores vao para o mesmo sitio
    file_vm.write('STOP')
    file_vm.close()

#Error value for syntax errors
def p_error(p):
# get formatted representation of stack
    stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])

    print('Syntax error in input! Parser State:{} {} . {}'
          .format(parser.state,
                  stack_state_str,
                  p))

#Build the parser
parser =  yacc.yacc()
# my state
# dicionario inicializado a vazio
parser.registers = {}



#GENERATE file.vm
global i
i=0
file = 'file.vm'
file_vm = open(file, "w+")
file_vm.write('START\n')
# reading input
for linha in sys.stdin:
    result = parser.parse(linha)

