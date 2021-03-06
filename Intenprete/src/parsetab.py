
# parsetab.py
# This file is automatically generated. Do not edit.

_lr_method = 'LALR'

_lr_signature = '\x16=\x8bH\xd4S7k\x9e\xb0\x98=g\x1f\xe7['

_lr_action_items = {'NUMBER':([2,9,11,24,28,30,39,41,42,43,44,45,46,47,48,49,50,51,52,53,],[-8,-7,18,18,33,18,18,18,-31,18,-29,18,-30,18,-26,18,-27,-25,18,-28,]),'MINUS':([18,36,38,],[-36,51,-35,]),'DOT':([18,21,22,25,32,33,34,37,54,56,57,58,59,60,61,],[-36,-35,27,31,-10,-9,40,-18,-17,-20,-23,-21,-24,-22,-19,]),'GTE':([18,36,38,],[-36,44,-35,]),'LPARENT':([1,5,35,38,],[11,-32,41,-32,]),'EQUALITY':([18,36,38,],[-36,43,-35,]),'DYNAMIC':([2,3,9,],[-8,12,-7,]),'LT':([18,36,38,],[-36,46,-35,]),'INEQUALITY':([18,36,38,],[-36,47,-35,]),'PLUS':([18,36,38,],[-36,48,-35,]),'RPARENT':([18,19,20,21,29,55,],[-36,-34,25,-35,-33,61,]),'COMMA':([18,19,20,21,22,29,32,33,34,37,54,55,56,57,58,59,60,61,],[-36,-34,24,-35,26,24,26,-9,39,-18,39,24,-20,-23,-21,-24,-22,-19,]),'ASSIGN':([0,4,7,8,10,17,18,25,27,31,36,38,40,],[9,-2,9,-4,-3,9,-36,30,-6,-15,9,-35,-16,]),'$end':([4,6,7,8,10,17,27,31,40,],[-2,0,-1,-4,-3,-5,-6,-15,-16,]),'GT':([18,36,38,],[-36,42,-35,]),'DIVIDE':([5,18,23,36,38,],[-32,-36,28,53,-35,]),'IS':([0,4,7,8,10,17,18,27,31,36,38,40,],[2,-2,2,-4,-3,2,-36,-6,-15,2,-35,-16,]),'TIMES':([18,36,38,],[-36,50,-35,]),'MULTIFILE':([2,3,9,],[-8,13,-7,]),'ID':([0,2,4,7,8,9,10,11,12,13,14,15,16,17,24,26,27,30,31,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[5,-8,-2,5,-4,-7,-3,21,-11,-13,-14,5,-12,5,21,5,-6,38,-15,38,-16,21,-31,21,-29,38,-30,21,-26,21,-27,-25,21,-28,]),'DISCONTIGUOUS':([2,3,9,],[-8,14,-7,]),'PUBLIC':([2,3,9,],[-8,16,-7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _lr_action.has_key(_x):  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'elements':([11,24,41,],[20,29,55,]),'goal':([30,39,],[34,54,]),'directive':([15,26,],[22,32,]),'factname':([0,7,15,17,26,30,39,45,],[1,1,23,1,23,35,35,35,]),'assing':([0,7,17,36,],[3,3,3,45,]),'rule':([0,7,17,],[4,4,4,]),'element':([11,24,30,39,41,43,45,47,49,52,],[19,19,36,36,19,56,36,58,59,60,]),'program':([0,],[6,]),'block':([0,7,17,],[7,17,17,]),'grules':([0,7,17,],[8,8,8,]),'goalRule':([30,39,45,],[37,37,57,]),'operator':([36,],[49,]),'property':([3,],[15,]),'check':([36,],[52,]),'fact':([0,7,17,],[10,10,10,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _lr_goto.has_key(_x): _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S'",1,None,None,None),
  ('program',1,'p_program','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',23),
  ('block',1,'p_block1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',28),
  ('block',1,'p_block2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',32),
  ('block',1,'p_block3','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',36),
  ('block',2,'p_block4','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',40),
  ('grules',4,'p_grules1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',44),
  ('assing',1,'p_assing1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',49),
  ('assing',1,'p_assing2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',54),
  ('directive',3,'p_directive1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',59),
  ('directive',3,'p_directive2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',64),
  ('property',1,'p_property1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',69),
  ('property',1,'p_property2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',74),
  ('property',1,'p_property3','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',79),
  ('property',1,'p_property4','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',84),
  ('fact',5,'p_fact','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',89),
  ('rule',7,'p_rule','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',94),
  ('goal',3,'p_goal1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',99),
  ('goal',1,'p_goal2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',104),
  ('goalRule',4,'p_goalrule1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',110),
  ('goalRule',3,'p_goalrule2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',115),
  ('goalRule',3,'p_goalrule3','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',119),
  ('goalRule',3,'p_goalrule4','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',123),
  ('goalRule',3,'p_goalrule5','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',127),
  ('goalRule',3,'p_goalrule6','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',131),
  ('operator',1,'p_operator1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',135),
  ('operator',1,'p_operator2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',139),
  ('operator',1,'p_operator3','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',143),
  ('operator',1,'p_operator4','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',147),
  ('check',1,'p_check1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',151),
  ('check',1,'p_check2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',155),
  ('check',1,'p_check3','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',159),
  ('factname',1,'p_factname1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',163),
  ('elements',3,'p_elements1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',169),
  ('elements',1,'p_elements2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',174),
  ('element',1,'p_element1','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',179),
  ('element',1,'p_element2','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',184),
  ('empty',0,'p_empty','E:\\Workspace\\git\\Interprete\\Intenprete\\src\\analizadorSintactico.py',188),
]
