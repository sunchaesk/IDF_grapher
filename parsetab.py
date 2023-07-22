
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA SEMICOLON VALUEidffile : idfobjectlistidfobjectlist : idfobjectidfobjectlist : idfobject idfobjectlistidfobject : objectname SEMICOLONidfobject : objectname COMMA valuelist SEMICOLONobjectname : VALUEvaluelist : VALUEvaluelist : VALUE COMMA valuelist'
    
_lr_action_items = {'VALUE':([0,3,7,8,11,12,],[5,5,-4,10,-5,10,]),'$end':([1,2,3,6,7,11,],[0,-1,-2,-3,-4,-5,]),'SEMICOLON':([4,5,9,10,13,],[7,-6,11,-7,-8,]),'COMMA':([4,5,10,],[8,-6,12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'idffile':([0,],[1,]),'idfobjectlist':([0,3,],[2,6,]),'idfobject':([0,3,],[3,3,]),'objectname':([0,3,],[4,4,]),'valuelist':([8,12,],[9,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> idffile","S'",1,None,None,None),
  ('idffile -> idfobjectlist','idffile',1,'p_idffile','lp.py',68),
  ('idfobjectlist -> idfobject','idfobjectlist',1,'p_idfobjectlist','lp.py',77),
  ('idfobjectlist -> idfobject idfobjectlist','idfobjectlist',2,'p_idfobjectlist_multiple','lp.py',82),
  ('idfobject -> objectname SEMICOLON','idfobject',2,'p_idfobject','lp.py',87),
  ('idfobject -> objectname COMMA valuelist SEMICOLON','idfobject',4,'p_idfobject_with_values','lp.py',92),
  ('objectname -> VALUE','objectname',1,'p_objectname','lp.py',97),
  ('valuelist -> VALUE','valuelist',1,'p_valuelist','lp.py',102),
  ('valuelist -> VALUE COMMA valuelist','valuelist',3,'p_valuelist_multiple','lp.py',107),
]