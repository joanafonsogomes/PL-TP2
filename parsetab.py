
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "id numComandos : Comandos ComandoComandos : Comando\n    Comando : Ler\n           |  Escrever\n           |  Despejar\n           |  Atrib\n           |  Exp\n           |  End\n    Exp : Exp '+' TermoExp : Exp '-' TermoExp : TermoTermo : Termo '*' FactorTermo : Termo '/' FactorTermo : FactorFactor : idFactor : numFactor : '(' Exp ')' Ler : '?' idEscrever : '!' idDespejar : '!' '!'Atrib : id '=' ExpEnd : '!' '!' '!'"
    
_lr_action_items = {'?':([0,1,2,3,4,5,6,7,8,10,12,13,14,16,19,21,22,26,27,28,29,30,31,32,33,],[9,9,-2,-3,-4,-5,-6,-7,-8,-15,-11,-14,-16,-1,-18,-20,-19,-15,-9,-10,-21,-22,-12,-13,-17,]),'!':([0,1,2,3,4,5,6,7,8,10,11,12,13,14,16,19,21,22,26,27,28,29,30,31,32,33,],[11,11,-2,-3,-4,-5,-6,-7,-8,-15,21,-11,-14,-16,-1,-18,30,-19,-15,-9,-10,-21,-22,-12,-13,-17,]),'id':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,],[10,10,-2,-3,-4,-5,-6,-7,-8,19,-15,22,-11,-14,-16,26,-1,26,26,-18,26,-20,-19,26,26,-15,-9,-10,-21,-22,-12,-13,-17,]),'num':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,],[14,14,-2,-3,-4,-5,-6,-7,-8,-15,-11,-14,-16,14,-1,14,14,-18,14,-20,-19,14,14,-15,-9,-10,-21,-22,-12,-13,-17,]),'(':([0,1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,],[15,15,-2,-3,-4,-5,-6,-7,-8,-15,-11,-14,-16,15,-1,15,15,-18,15,-20,-19,15,15,-15,-9,-10,-21,-22,-12,-13,-17,]),'$end':([1,2,3,4,5,6,7,8,10,12,13,14,16,19,21,22,26,27,28,29,30,31,32,33,],[0,-2,-3,-4,-5,-6,-7,-8,-15,-11,-14,-16,-1,-18,-20,-19,-15,-9,-10,-21,-22,-12,-13,-17,]),'+':([7,10,12,13,14,25,26,27,28,29,31,32,33,],[17,-15,-11,-14,-16,17,-15,-9,-10,17,-12,-13,-17,]),'-':([7,10,12,13,14,25,26,27,28,29,31,32,33,],[18,-15,-11,-14,-16,18,-15,-9,-10,18,-12,-13,-17,]),'=':([10,],[20,]),'*':([10,12,13,14,26,27,28,31,32,33,],[-15,23,-14,-16,-15,23,23,-12,-13,-17,]),'/':([10,12,13,14,26,27,28,31,32,33,],[-15,24,-14,-16,-15,24,24,-12,-13,-17,]),')':([12,13,14,25,26,27,28,31,32,33,],[-11,-14,-16,33,-15,-9,-10,-12,-13,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Comandos':([0,],[1,]),'Comando':([0,1,],[2,16,]),'Ler':([0,1,],[3,3,]),'Escrever':([0,1,],[4,4,]),'Despejar':([0,1,],[5,5,]),'Atrib':([0,1,],[6,6,]),'Exp':([0,1,15,20,],[7,7,25,29,]),'End':([0,1,],[8,8,]),'Termo':([0,1,15,17,18,20,],[12,12,12,27,28,12,]),'Factor':([0,1,15,17,18,20,23,24,],[13,13,13,13,13,13,31,32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Comandos","S'",1,None,None,None),
  ('Comandos -> Comandos Comando','Comandos',2,'p_Comandos','gerador_yacc.py',8),
  ('Comandos -> Comando','Comandos',1,'p_Comando_unico','gerador_yacc.py',12),
  ('Comando -> Ler','Comando',1,'p_Comando','gerador_yacc.py',17),
  ('Comando -> Escrever','Comando',1,'p_Comando','gerador_yacc.py',18),
  ('Comando -> Despejar','Comando',1,'p_Comando','gerador_yacc.py',19),
  ('Comando -> Atrib','Comando',1,'p_Comando','gerador_yacc.py',20),
  ('Comando -> Exp','Comando',1,'p_Comando','gerador_yacc.py',21),
  ('Comando -> End','Comando',1,'p_Comando','gerador_yacc.py',22),
  ('Exp -> Exp + Termo','Exp',3,'p_Exp_add','gerador_yacc.py',28),
  ('Exp -> Exp - Termo','Exp',3,'p_Exp_sub','gerador_yacc.py',35),
  ('Exp -> Termo','Exp',1,'p_Exp_termo','gerador_yacc.py',40),
  ('Termo -> Termo * Factor','Termo',3,'p_Termo_mul','gerador_yacc.py',44),
  ('Termo -> Termo / Factor','Termo',3,'p_Termo_div','gerador_yacc.py',49),
  ('Termo -> Factor','Termo',1,'p_Termo_factor','gerador_yacc.py',58),
  ('Factor -> id','Factor',1,'p_Factor_id','gerador_yacc.py',62),
  ('Factor -> num','Factor',1,'p_Factor_num','gerador_yacc.py',66),
  ('Factor -> ( Exp )','Factor',3,'p_Factor_group','gerador_yacc.py',70),
  ('Ler -> ? id','Ler',2,'p_Ler','gerador_yacc.py',75),
  ('Escrever -> ! id','Escrever',2,'p_Escrever','gerador_yacc.py',80),
  ('Despejar -> ! !','Despejar',2,'p_Despejar','gerador_yacc.py',84),
  ('Atrib -> id = Exp','Atrib',3,'p_Atrib','gerador_yacc.py',88),
  ('End -> ! ! !','End',3,'p_End','gerador_yacc.py',93),
]
