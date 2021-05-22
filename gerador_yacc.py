import ply.yacc as yacc 
import fileinput
import sys
from gerador_lex import tokens 


#Production rules
def p_Comandos(p):
    "Comandos : Comandos Comando"
    p[0] = p[1] + p[2]
def p_Comando_unico(p):
    "Comandos : Comando"
    p[0] = p[1]

def p_Comando(p):
    """
    Comando : Ler
           |  Escrever
           |  Atrib
           |  Exp
           |  End
           |  Condition
           |  Cicle
    """
    p[0] = p[1]  

 

def p_Exp_add(p):
    "Exp : Exp '+' Termo" 
    p[0] = p[1]+ p[3]+ 'ADD\n'
    # file_vm.write(p[0])

def p_Exp_sub(p):
    "Exp : Exp '-' Termo" 
    p[0] = p[1]+ p[3]+ 'SUB\n'
    # file_vm.write(p[0])

def p_Exp_termo(p):
    "Exp : Termo"
    p[0] = p[1]
    # file_vm.write(p[0])

def p_Termo_mul(p):
    "Termo : Termo '*' Factor"
    p[0] = p[1]+ p[3] + 'MUL\n'
    # file_vm.write(p[0])

def p_Termo_div(p):
    "Termo : Termo '/' Factor"
    if(p[3] != 0):
        p[0] = p[1]+ p[3]+ 'DIV\n'
        # file_vm.write(p[0])
    else:
        print ("Erro: divisao por 0, a continuar com 0...)")
        p[0] = str(0)
        # file_vm.write(p[0])

def p_Termo_factor(p):
    "Termo : Factor"
    p[0] = p[1]
    # file_vm.write(p[0])

def p_Factor_id(p):
    "Factor : id"
    indice = p.parser.registers.get(p[1])
    p[0] = 'PUSHG ' + str(indice) + '\n'

def p_Factor_num(p):
    "Factor : num"
    p[0] = 'PUSHI ' + p[1] + '\n'
    # file_vm.write(p[0])

def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]
    # file_vm.write(p[0])

##############WORKING ON IT#####################3

def p_Ler(p):
    ##falta ler da vm e nao do python!!!
    "Ler : '?' id"
    global i
    flag=1
    valor = input("Introduza o valor inteiro: ")
    for key in p.parser.registers.keys():
        if key == p[2]:
            p[0] = 'PUSHI ' +valor+ '\n'+ 'STOREG '+ str(p.parser.registers.get(key)) +'\n'
            flag=0
            file_vm.write(p[0])
    if(flag==1):
        p.parser.registers.update({p[2]: i})
        p[0] = 'PUSHI 0\nPUSHI ' +valor+ '\n'+ 'STOREG '+ str(i) +'\n'
        i= i+1
        # file_vm.write(p[0])

def p_Escrever(p):
    "Escrever : '!' id"
    for key in p.parser.registers.keys():
        if key == p[2]:
            p[0]= 'PUSHG ' +(p.parser.registers.get(key)) +'\nWRITEI\n'
            # file_vm.write(p[0])

##############wORKING UNTIL HERE################
def p_Atrib(p):
    "Atrib : id '=' Exp"
    global i
    flag=1
    for key in p.parser.registers.keys():
            if key == p[1]:
                p[0] = p[3] + 'STOREG '+ str(p.parser.registers.get(key)) +'\n'
                flag=0
                # file_vm.write(p[0])
    if(flag==1):
            p.parser.registers.update({p[1]: i})
            p[0] = 'PUSHI 0\n' +p[3]+ 'STOREG '+ str(i) +'\n'
            i= i+1
            # file_vm.write(p[0])

def p_Condition_maior(p):
    "Condition : IF '(' Exp '>' Termo ')' THEN Comandos ELSE Comandos FI"
    # file_vm.write(p[0])

    p[0] = p[3] + p[5] +'SUP\n' +'JZ else\n' + (p[8])+ 'JUMP fim\n' + 'else:\n' + (p[10])+ 'fim:\n'
    # file_vm.write(p[0])

def p_Condition_menor(p):
    "Condition : IF '(' Exp '<' Termo ')' THEN Comandos ELSE Comandos FI" 
    p[0] = p[3] + p[5] +'INF\n' +'JZ else\n' + p[8]+'JUMP fim\n' + 'else:\n' + p[10] + 'fim:\n'
    # file_vm.write(p[0])

def p_Condition_maiorigual(p):
    "Condition : IF '(' Exp '>' '=' Termo ')' THEN Comandos ELSE Comandos FI"
    p[0] = p[3] + p[6]+ 'SUPEQ\n' +'JZ else\n' + p[9]+'JUMP fim\n'  + 'else:\n' + p[11]+ 'fim:\n' 
    # file_vm.write(p[0])

def p_Condition_menorigual(p):
    "Condition : IF '(' Exp '<' '=' Termo ')' THEN Comandos ELSE Comandos FI"
    p[0] = p[3] + p[6] +'INFEQ\n' +'JZ else\n' + p[9]+'JUMP fim\n'  + 'else:\n' + p[11] + 'fim:\n'
    # file_vm.write(p[0])

def p_Condition_igual(p):
    "Condition : IF '(' Exp '=' '=' Termo ')' THEN Comandos ELSE Comandos FI"
    p[0] = p[3] + p[6] +'EQUAL\n' +'JZ else\n' + p[9]+'JUMP fim\n'  + 'else:\n' + p[11] + 'fim:\n'
    # print(p[0])     
    # file_vm.write(p[0])

def p_Cicle_menor(p):
    "Cicle : FOR '(' Atrib ';' Factor '<' Factor ';' Atrib ')' Comandos ROF"
    p[0] = p[3] + 'ciclo1:\n' + p[5] + p[7] + 'INF\n'  +'JZ fim\n' + p[11] + p[9]  + 'JUMP ciclo1\n' + 'fim:\n' 

def p_Cicle_maior(p):
    "Cicle : FOR '(' Atrib ';' Factor '>' Factor ';' Atrib ')' Comandos ROF"
    p[0] = p[3] + 'ciclo1:\n' + p[5] + p[7] + 'SUP\n'  +'JZ fim\n' + p[11] + p[9]  + 'JUMP ciclo1\n' + 'fim:\n' 

def p_Cicle_menor_igual(p):
    "Cicle : FOR '(' Atrib ';' Factor '<''=' Factor ';' Atrib ')' Comandos ROF"
    p[0] = p[3] + 'ciclo1:\n' + p[5] + p[7] + 'INFEQ\n'  +'JZ fim\n' + p[11] + p[9]  + 'JUMP ciclo1\n' + 'fim:\n' 

def p_Cicle_maior_igual(p):
    "Cicle : FOR '(' Atrib ';' Factor '<' Factor ';' Atrib ')' Comandos ROF"
    p[0] = p[3] + 'ciclo1:\n' + p[5] + p[7] + 'SUPEQ\n'  +'JZ fim\n' + p[11] + p[9]  + 'JUMP ciclo1\n' + 'fim:\n' 


def p_Cicle_igual(p):
    "Cicle : FOR '(' Atrib ';' Factor '<' Factor ';' Atrib ')' Comandos ROF"
    p[0] = p[3] + 'ciclo1:\n' + p[5] + p[7] + 'EQUAL\n'  +'JZ fim\n' + p[11] + p[9]  + 'JUMP ciclo1\n' + 'fim:\n' 


def p_End(p):
    "End : '!' '!' '!'"
    # da erro fp=sp, os apontadores vao para o mesmo sitio
    p[0]='STOP'
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
for linha in fileinput.input():
    result = parser.parse(linha)
    file_vm.write(str(result))

