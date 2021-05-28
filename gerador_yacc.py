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
    Comando :  Printing
           |  Reading
           |  Writing
           |  Start
           |  Exp
           |  Atrib
           |  Condition
           |  Cicle
           |  End
    """
    p[0] = p[1]  

 
def p_Printing(p):
    "Printing : PRINT frase"
    p[0] = 'PUSHS ' +p[2] +'\n' + 'WRITES\n' 

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
    global i 
    indice = p.parser.registers.get(p[1])
    if(str(indice) == 'None'):
        if(f==1):
            sys.exit("Erro: Impossivel declarar variavel")
        else:
            p.parser.registers.update({p[1]: i})
            p[0]= 'PUSHI 0\n' + 'PUSHG ' + str(i) + '\n' 
            i=i+1
    else:
        p[0] = 'PUSHG ' + str(indice) + '\n'

def p_Factor_num(p):
    "Factor : num"
    p[0] = 'PUSHI ' + p[1] + '\n'
    # file_vm.write(p[0])


def p_Factor_group(p):
    "Factor : '(' Exp ')'"
    p[0] = p[2]
    # file_vm.write(p[0])

def p_Factor_Array(p):
    "Factor : Array"
    p[0] = p[1]

def p_Factor_Matriz(p):
    "Factor : Matriz"
    p[0] = p[1]

def p_Reading(p):
    "Reading : READ id"
    global i
    flag=1
    for key in p.parser.registers.keys():
        if key == p[2]:
            p[0] = 'READ\nATOI\n'+ 'STOREG '+ str(p.parser.registers.get(key)) +'\n'
            flag=0
            file_vm.write(p[0])
    if(flag==1):
        if(f==1):
            sys.exit("Erro: Impossivel declarar variavel")
        else:
            p.parser.registers.update({p[2]: i})
            p[0] = 'PUSHI 0\nREAD\nATOI\n'+ 'STOREG '+ str(i) +'\n'
            i= i+1

def p_Writing(p):
    "Writing : WRITE id"
    indice= p.parser.registers.get(p[2])
    p[0]= 'PUSHI ' + str(indice) +'\n'+ 'WRITEI\n'

def p_Writing_Array(p):
    "Writing : WRITE id '[' num ']'"
    indice = p.parser.registers.get(p[2])
    p[0] = 'PUSHGP\n' + 'PUSHI ' + str(indice) +'\n' + 'PADD\n' + 'PUSHI ' + p[4] +'\n'+ 'LOADN\n' + 'WRITEI\n'


def p_Start(p):
    "Start : START"
    global f
    p[0]='START\n'
    f=1

def p_End(p):
    "End : END"
    p[0]='STOP'
    file_vm.write(p[0])
    file_vm.close()
    sys.exit("Programa compilado com sucesso!")

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
    global count
    p[0] = p[3] + p[5] +'SUP\n' +'JZ else' + str(count)+'\n' + (p[8])+ 'JUMP ' + 'fim'+str((count+1))+'\n' + 'else'+str(count)+':\n' + (p[10])+ 'fim'+str((count+1))+':\n'
    count=count+2


def p_Condition_menor(p):
    "Condition : IF '(' Exp '<' Termo ')' THEN Comandos ELSE Comandos FI" 
    global count
    p[0] = p[3] + p[5] +'INF\n' +'JZ else' + str(count)+'\n' + (p[8])+ 'JUMP ' +  'fim'+str((count+1))+'\n' + 'else'+str(count)+':\n' + (p[10])+ 'fim'+str((count+1))+':\n'
    count=count+2

def p_Condition_maiorigual(p):
    "Condition : IF '(' Exp '>' '=' Termo ')' THEN Comandos ELSE Comandos FI"
    global count
    p[0] = p[3] + p[6]+ 'SUPEQ\n' +'JZ else' + str(count)+'\n' + (p[9])+ 'JUMP ' +  'fim'+str((count+1))+'\n' + 'else'+str(count)+':\n' + (p[11])+ 'fim'+str((count+1))+':\n'
    count=count+2

def p_Condition_menorigual(p):
    "Condition : IF '(' Exp '<' '=' Termo ')' THEN Comandos ELSE Comandos FI"
    global count
    p[0] = p[3] + p[6] +'INFEQ\n' +'JZ else' + str(count)+'\n' + (p[9])+ 'JUMP ' +  'fim'+str((count+1))+'\n' + 'else'+str(count)+':\n' + (p[11])+ 'fim'+str((count+1))+':\n'
    count=count+2

def p_Condition_igual(p):
    "Condition : IF '(' Exp '=' '=' Termo ')' THEN Comandos ELSE Comandos FI"
    global count
    p[0] = p[3] + p[6] +'EQUAL\n' +'JZ else' + str(count)+'\n' + (p[9])+ 'JUMP ' +  'fim'+str((count+1))+'\n' + 'else'+str(count)+':\n' + (p[11])+ 'fim'+str((count+1))+':\n'
    count=count+2

def p_Condition_not_igual(p):
    "Condition : IF '(' Exp '!' '=' Termo ')' THEN Comandos ELSE Comandos FI"
    global count
    p[0] = p[3] + p[6] +'EQUAL\n'+'NOT\n' +'JZ else' + str(count)+'\n' + (p[9])+ 'JUMP ' +  'fim'+str((count+1))+'\n' + 'else'+str(count)+':\n' + (p[11])+ 'fim'+str((count+1))+':\n'
    count=count+2

def p_Cicle_menor(p):
    "Cicle : FOR '(' Atrib ';' Factor '<' Factor ';' Atrib ')' Comandos ROF"
    global count
    p[0] = p[3] + 'ciclo'+str(count)+':\n' + p[5] + p[7] + 'INF\n'  +'JZ fim'+str((count+1)) +'\n' + p[11] + p[9]  + 'JUMP ciclo'+str(count)+'\n' + 'fim'+str((count+1))+':\n' 
    count=count+2

def p_Cicle_maior(p):
    "Cicle : FOR '(' Atrib ';' Factor '>' Factor ';' Atrib ')' Comandos ROF"
    global count
    p[0] = p[3] + 'ciclo'+str(count)+':\n' + p[5] + p[7] + 'SUP\n'  +'JZ fim'+str((count+1)) +'\n' + p[11] + p[9]  + 'JUMP ciclo'+str(count)+'\n' + 'fim'+str((count+1))+':\n' 
    count=count+2

def p_Cicle_menor_igual(p):
    "Cicle : FOR '(' Atrib ';' Factor '<' '=' Factor ';' Atrib ')' Comandos ROF"
    global count
    p[0] = p[3] + 'ciclo'+str(count)+':\n' + p[5] + p[8] + 'INFEQ\n'  +'JZ fim'+str((count+1)) +'\n' + p[12] + p[10]  + 'JUMP ciclo'+str(count)+'\n' + 'fim'+str((count+1))+':\n'  
    count=count+2

def p_Cicle_maior_igual(p):
    "Cicle : FOR '(' Atrib ';' Factor '>' '=' Factor ';' Atrib ')' Comandos ROF"
    global count
    p[0] = p[3] + 'ciclo'+str(count)+':\n' + p[5] + p[8] + 'SUPEQ\n'  +'JZ fim'+str((count+1)) +'\n' + p[12] + p[10]  + 'JUMP ciclo'+str(count)+'\n' + 'fim'+str((count+1))+':\n' 
    count=count+2

def p_Cicle_igual(p):
    "Cicle : FOR '(' Atrib ';' Factor '=' '=' Factor ';' Atrib ')' Comandos ROF"
    global count
    p[0] = p[3] + 'ciclo'+str(count)+':\n' + p[5] + p[8] + 'EQUAL\n'  +'JZ fim'+str((count+1)) +'\n' + p[12] + p[10]  + 'JUMP ciclo'+str(count)+'\n' + 'fim'+str((count+1))+':\n' 
    count=count+2

def p_Cicle_not_igual(p):
    "Cicle : FOR '(' Atrib ';' Factor '!' '=' Factor ';' Atrib ')' Comandos ROF"
    global count
    p[0] = p[3] + 'ciclo'+str(count)+':\n' + p[5] + p[8] + 'EQUAL\n'+'NOT\n'  +'JZ fim'+str((count+1)) +'\n' + p[12] + p[10]  + 'JUMP ciclo'+str(count)+'\n' + 'fim'+str((count+1))+':\n' 
    count=count+2

def p_Array(p):
    "Array : id '[' num ']'"
    global i
    if(f==1):
        sys.exit("Erro: Impossivel declaral variavel")
    else:
        p.parser.registers.update({p[1]: i})
        p.parser.registers_array.update({p[1]: p[3]})
        p[0] = 'PUSHN ' +p[3]+ '\n'
        i= i+ int(p[3])

def p_Atrib_Array(p):
    "Atrib : id '[' num ']' '=' num"
    indice = p.parser.registers.get(p[1])
    if(str(indice)=='None' ):
        string = "ERRO: Variavel " +p[1] +" por declarar!"
        sys.exit(string)
    else:
        z=int(p.parser.registers_array.get(p[1]))
        y=int(p[3])
        if(z>y and y>=0):
            p[0] = 'PUSHGP\n' + 'PUSHI '+str(indice) +'\n' 'PADD\n' +'PUSHI '+ p[3]+'\n' +'PUSHI '+ p[6] +'\n'+ 'STOREN\n' 
        else:
            string = "Indexacao indisponivel! (" + str(z) +" menor ou igual a " + str(y) +")" 
            sys.exit(string)
            
def p_Matriz(p):
    "Matriz : id '[' num ']' '[' num ']'"
    global i
    # apenas para saber quantas celulas da matriz existem ao todo
    m = int(int(p[3])) *  int(int(p[6]))
    p.parser.registers_array.update({p[1]: m})
    p.parser.registers.update({p[1]: i})
    p.parser.registers_linhas.update({p[1]: p[3]})
    p.parser.registers_colunas.update({p[1]: p[6]})
    p[0] = 'PUSHN ' +str(m)+ '\n'
    i= i+ m


def p_Atrib_Matriz(p):
    "Atrib : id '[' num ']' '[' num ']' '=' num"
    # apenas para saber qual o indice maior que se pretende
    # para depois se comparar com o numero de celulas
    # subtrai-se um porque e de 0 a n-1
    m = (int(p[3])+1 *  int(p[6])+1) -1
    indice = p.parser.registers.get(p[1])
    if(str(indice) == 'None'):
        string = "ERRO: Variavel " +p[1] +" por declarar!"
        sys.exit(string)
    else:
        if(p.parser.registers_linhas.get(p[1])> int(p[3])
                and int(p[3])>=0
                and p.parser.registers_colunas.get(p[1])>int(p[6])
                and int(p[6])>=0):
            elementos_linha= p.parser.registers_linhas.get(p[1])
            p[0] = 'PUSHGP\n' + 'PUSHI '+str(indice) +'\n' 'PADD\n' +'PUSHI '+ p[3]+ '\n'+'PUSHI '+ str(elementos_linha)+'\n'+'MUL\n'+ 'PUSHI '+p[6]+'\n' +'ADD\n' +'PUSHI '+ p[9] +'\n'+ 'STOREN\n' 
        else:
            sys.exit("Indexacao indisponivel!")


#Error value for syntax errors
def p_error(token):
    if token is not None:
        print ("Illegal token: %s" % (token.value))
    else:
        print('Unexpected end of input')
#Build the parser
parser =  yacc.yacc()
# my state
# dicionario inicializado a vazio
parser.registers = {}
parser.registers_array = {}
parser.registers_linhas = {}
parser.registers_colunas = {}
#GENERATE file.vm
global i
global f
global count
i=0
f=0
count=0
file = 'file.vm'
file_vm = open(file, "w+")
# reading input
if(len(sys.argv)>1):
    for linha in fileinput.input(files= sys.argv[1]):
        result = parser.parse(linha)
        file_vm.write(str(result))
else:
    for linha in fileinput.input():
        result = parser.parse(linha)
        file_vm.write(str(result))
