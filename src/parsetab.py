
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACCION AMBIENTE ASIGNACION CADENA COMA COMENTARIO_ENCABEZADO COMENTARIO_LINEA COMENTARIO_VARIASLINEAS DISTINTO DIVISION DIVISION_ENTERA DOS_PUNTOS ENTONCES ES ESCRIBIR FIN_ACCION FIN_MIENTRAS FIN_PARA FIN_SEGUN FIN_SI HACER HASTA HASTA_QUE IDENTIFICADOR IGUAL LEER MAYOR_O_IGUAL_QUE MAYOR_QUE MENOR_O_IGUAL_QUE MENOR_QUE MIENTRAS MODULO MULTIPLICACION NO NUMERICO O OTRO PARA PARENTESIS_ABIERTO PARENTESIS_CERRADO POTENCIA PROCESO REPETIR RESTA SEGUN SEMICOLON SI SINO SUMA TD_ALFANUMERICO TD_LOGICO TD_NUMERICO Y sigma : COMENTARIO_ENCABEZADO ACCION IDENTIFICADOR ES ambiente FIN_ACCION\n            | ACCION IDENTIFICADOR ES ambiente FIN_ACCION comentario_vl_l : COMENTARIO_VARIASLINEAS\n                    | COMENTARIO_LINEAambiente : AMBIENTE bloque_ambiente proceso \n                | AMBIENTE comentario_vl_l bloque_ambiente proceso\n        bloque_ambiente : variable comentario_vl_l\n                    | constante comentario_vl_l\n                    | variable comentario_vl_l bloque_ambiente\n                    | constante comentario_vl_l bloque_ambiente\n                    | comentario_vl_l\n                    | comentario_vl_l bloque_ambiente\n                    | variable bloque_ambiente\n                    | constante bloque_ambiente\n                    | variable\n                    | constante\n    variable : IDENTIFICADOR DOS_PUNTOS ftd_ambconstante : IDENTIFICADOR IGUAL tipo_datoftd_amb : TD_ALFANUMERICO \n                 | TD_NUMERICO\n                 | TD_LOGICO tipo_dato : CADENA \n                | NUMERICO\n    \n        proceso : PROCESO comentario_vl_l conj_sentencia\n            | PROCESO conj_sentencia\n    conj_sentencia : s_escribir conj_sentencia \n                    | s_escribir comentario_vl_l conj_sentencia\n                    | s_leer conj_sentencia \n                    | s_leer comentario_vl_l conj_sentencia \n                    | s_si conj_sentencia \n                    | s_si comentario_vl_l conj_sentencia \n                    | s_ciclos conj_sentencia \n                    | s_ciclos comentario_vl_l conj_sentencia \n                    | sentencia conj_sentencia \n                    | sentencia comentario_vl_l conj_sentencia \n                    | comentario_vl_l conj_sentencia \n                    | s_escribir comentario_vl_l \n                    | s_leer comentario_vl_l \n                    | s_si comentario_vl_l\n                    | s_ciclos comentario_vl_l \n                    | sentencia comentario_vl_l \n                    | s_escribir \n                    | s_leer \n                    | s_si \n                    | s_ciclos \n                    | sentencia \n                    | comentario_vl_ls_escribir : ESCRIBIR PARENTESIS_ABIERTO salida_esc PARENTESIS_CERRADOsalida_esc : IDENTIFICADOR \n                | CADENA \n                | IDENTIFICADOR COMA salida_esc \n                | CADENA COMA salida_escs_leer : LEER PARENTESIS_ABIERTO entrada_leer PARENTESIS_CERRADOentrada_leer : IDENTIFICADOR\n        sentencia : IDENTIFICADOR ASIGNACION tipo_dato\n                | IDENTIFICADOR ASIGNACION op_aritmetica\n    \n        id_tipodato : IDENTIFICADOR\n                | tipo_dato\n    \n        conj_operaciones : op_aritmetica\n                        | relacionales\n    \n        op_aritmetica : id_tipodato t_op_aritmetico id_tipodato\n                    | id_tipodato t_op_aritmetico\n    \n        t_op_aritmetico : SUMA\n                        | RESTA\n                        | DIVISION\n                        | MULTIPLICACION\n                        | DIVISION_ENTERA\n                        | MODULO\n                        | POTENCIA\n    \n        relacionales : id_tipodato t_relacional id_tipodato\n                | id_tipodato t_relacional id_tipodato relacionales\n    \n        t_relacional : MENOR_QUE\n                    | MAYOR_QUE\n                    | MENOR_O_IGUAL_QUE\n                    | MAYOR_O_IGUAL_QUE\n                    | IGUAL\n                    | DISTINTO\n    \n        t_op_logico : O\n                | Y\n    s_si : SI PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO ENTONCES conj_s_si FIN_SIconj_s_si : conj_sentencia  \n                | conj_sentencia SINO conj_s_siconj_condiciones : condicion \n                        | condicion t_op_logico conj_condicionescondicion : expresion t_relacional expresion \n                | NO expresionexpresion : id_tipodato \n                | id_tipodato t_op_aritmetico id_tipodato \n                | id_tipodato t_op_aritmetico expresions_segun : SEGUN PARENTESIS_ABIERTO IDENTIFICADOR PARENTESIS_CERRADO HACER conj_cond_segun FIN_SEGUNconj_cond_segun : t_relacional id_tipodato DOS_PUNTOS conj_sentencia \n                    | t_relacional id_tipodato DOS_PUNTOS conj_sentencia conj_cond_segun \n                    | OTRO DOS_PUNTOS conj_sentencias_ciclos : c_para \n            | c_mientras \n            | c_repetir \n            | conj_sentencia\n        c_mientras : MIENTRAS PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO HACER conj_sentencia FIN_MIENTRAS\n    c_repetir : REPETIR conj_sentencia HASTA_QUE PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO\n        c_para : PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA id_tipodato HACER conj_sentencia FIN_PARA\n            | PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA HACER conj_sentencia FIN_PARA \n    idt_para : IDENTIFICADOR ASIGNACION id_tipodato \n            | IDENTIFICADOR\n    \n        empty :\n    '
    
_lr_action_items = {'COMENTARIO_ENCABEZADO':([0,],[2,]),'ACCION':([0,2,],[3,4,]),'$end':([1,12,20,],[0,-2,-1,]),'IDENTIFICADOR':([3,4,10,14,15,16,17,18,22,23,25,27,31,32,33,34,35,36,37,41,42,43,47,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,92,94,95,96,97,103,104,105,106,108,109,110,111,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,129,131,134,139,140,142,145,147,148,149,150,151,152,155,156,157,158,159,160,],[5,6,19,19,19,19,-3,-4,44,19,19,19,44,-97,44,44,44,44,44,-94,-95,-96,44,-17,-19,-20,-21,-18,-22,-23,44,-36,-26,44,-28,44,-30,44,-32,44,-34,44,85,88,94,94,100,94,-97,-36,-27,-29,-31,-33,-35,94,-57,-58,-55,-56,-48,85,85,-53,94,-78,-79,94,-72,-73,-74,-75,-76,-77,94,-63,-64,-65,-66,-67,-68,-69,94,94,94,44,-61,94,44,-97,-97,-99,-80,44,94,-98,44,44,-97,-97,-101,-100,]),'ES':([5,6,],[7,8,]),'AMBIENTE':([7,8,],[10,10,]),'FIN_ACCION':([9,11,17,18,21,31,32,33,34,35,36,37,41,42,43,49,57,58,59,60,61,62,63,64,65,66,67,68,69,70,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,139,148,149,152,159,160,],[12,20,-3,-4,-5,-47,-25,-42,-43,-44,-45,-46,-94,-95,-96,-6,-22,-23,-47,-24,-26,-37,-28,-38,-30,-39,-32,-40,-34,-41,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,-61,-99,-80,-98,-101,-100,]),'COMENTARIO_VARIASLINEAS':([10,14,15,16,17,18,22,23,25,27,31,32,33,34,35,36,37,41,42,43,47,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,134,139,142,145,147,148,149,150,152,155,156,157,158,159,160,],[17,17,17,17,-3,-4,17,17,17,17,17,-97,17,17,17,17,17,-94,-95,-96,17,-17,-19,-20,-21,-18,-22,-23,17,-36,-26,17,-28,17,-30,17,-32,17,-34,17,-97,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,17,-61,17,-97,-97,-99,-80,17,-98,17,17,-97,-97,-101,-100,]),'COMENTARIO_LINEA':([10,14,15,16,17,18,22,23,25,27,31,32,33,34,35,36,37,41,42,43,47,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,134,139,142,145,147,148,149,150,152,155,156,157,158,159,160,],[18,18,18,18,-3,-4,18,18,18,18,18,-97,18,18,18,18,18,-94,-95,-96,18,-17,-19,-20,-21,-18,-22,-23,18,-36,-26,18,-28,18,-30,18,-32,18,-34,18,-97,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,18,-61,18,-97,-97,-99,-80,18,-98,18,18,-97,-97,-101,-100,]),'PROCESO':([13,14,15,16,17,18,23,24,25,26,27,28,48,50,51,52,53,54,55,56,57,58,],[22,-11,-15,-16,-3,-4,-11,22,-7,-13,-8,-14,-12,-9,-10,-17,-19,-20,-21,-18,-22,-23,]),'ESCRIBIR':([17,18,22,31,32,33,34,35,36,37,41,42,43,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,134,139,142,145,147,148,149,150,152,155,156,157,158,159,160,],[-3,-4,38,38,-97,38,38,38,38,38,-94,-95,-96,38,-22,-23,38,-36,-26,38,-28,38,-30,38,-32,38,-34,38,-97,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,38,-61,38,-97,-97,-99,-80,38,-98,38,38,-97,-97,-101,-100,]),'LEER':([17,18,22,31,32,33,34,35,36,37,41,42,43,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,134,139,142,145,147,148,149,150,152,155,156,157,158,159,160,],[-3,-4,39,39,-97,39,39,39,39,39,-94,-95,-96,39,-22,-23,39,-36,-26,39,-28,39,-30,39,-32,39,-34,39,-97,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,39,-61,39,-97,-97,-99,-80,39,-98,39,39,-97,-97,-101,-100,]),'SI':([17,18,22,31,32,33,34,35,36,37,41,42,43,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,134,139,142,145,147,148,149,150,152,155,156,157,158,159,160,],[-3,-4,40,40,-97,40,40,40,40,40,-94,-95,-96,40,-22,-23,40,-36,-26,40,-28,40,-30,40,-32,40,-34,40,-97,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,40,-61,40,-97,-97,-99,-80,40,-98,40,40,-97,-97,-101,-100,]),'PARA':([17,18,22,31,32,33,34,35,36,37,41,42,43,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,134,139,142,145,147,148,149,150,152,155,156,157,158,159,160,],[-3,-4,45,45,-97,45,45,45,45,45,-94,-95,-96,45,-22,-23,45,-36,-26,45,-28,45,-30,45,-32,45,-34,45,-97,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,45,-61,45,-97,-97,-99,-80,45,-98,45,45,-97,-97,-101,-100,]),'MIENTRAS':([17,18,22,31,32,33,34,35,36,37,41,42,43,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,134,139,142,145,147,148,149,150,152,155,156,157,158,159,160,],[-3,-4,46,46,-97,46,46,46,46,46,-94,-95,-96,46,-22,-23,46,-36,-26,46,-28,46,-30,46,-32,46,-34,46,-97,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,46,-61,46,-97,-97,-99,-80,46,-98,46,46,-97,-97,-101,-100,]),'REPETIR':([17,18,22,31,32,33,34,35,36,37,41,42,43,47,57,58,59,60,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,134,139,142,145,147,148,149,150,152,155,156,157,158,159,160,],[-3,-4,47,47,-97,47,47,47,47,47,-94,-95,-96,47,-22,-23,47,-36,-26,47,-28,47,-30,47,-32,47,-34,47,-97,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,47,-61,47,-97,-97,-99,-80,47,-98,47,47,-97,-97,-101,-100,]),'HASTA_QUE':([17,18,33,34,35,36,37,41,42,43,57,58,59,61,62,63,64,65,66,67,68,69,70,77,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,139,148,149,152,159,160,],[-3,-4,-42,-43,-44,-45,-46,-94,-95,-96,-22,-23,-47,-26,-37,-28,-38,-30,-39,-32,-40,-34,-41,102,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,-61,-99,-80,-98,-101,-100,]),'SINO':([17,18,33,34,35,36,37,41,42,43,57,58,59,61,62,63,64,65,66,67,68,69,70,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,139,145,148,149,152,159,160,],[-3,-4,-42,-43,-44,-45,-46,-94,-95,-96,-22,-23,-47,-26,-37,-28,-38,-30,-39,-32,-40,-34,-41,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,-61,150,-99,-80,-98,-101,-100,]),'FIN_SI':([17,18,33,34,35,36,37,41,42,43,57,58,59,61,62,63,64,65,66,67,68,69,70,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,139,144,145,148,149,152,153,159,160,],[-3,-4,-42,-43,-44,-45,-46,-94,-95,-96,-22,-23,-47,-26,-37,-28,-38,-30,-39,-32,-40,-34,-41,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,-61,149,-81,-99,-80,-98,-82,-101,-100,]),'FIN_MIENTRAS':([17,18,33,34,35,36,37,41,42,43,57,58,59,61,62,63,64,65,66,67,68,69,70,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,139,147,148,149,152,159,160,],[-3,-4,-42,-43,-44,-45,-46,-94,-95,-96,-22,-23,-47,-26,-37,-28,-38,-30,-39,-32,-40,-34,-41,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,-61,152,-99,-80,-98,-101,-100,]),'FIN_PARA':([17,18,33,34,35,36,37,41,42,43,57,58,59,61,62,63,64,65,66,67,68,69,70,78,79,80,81,82,83,94,95,96,97,103,106,120,121,122,123,124,125,126,127,139,148,149,152,157,158,159,160,],[-3,-4,-42,-43,-44,-45,-46,-94,-95,-96,-22,-23,-47,-26,-37,-28,-38,-30,-39,-32,-40,-34,-41,-36,-27,-29,-31,-33,-35,-57,-58,-55,-56,-48,-53,-63,-64,-65,-66,-67,-68,-69,-62,-61,-99,-80,-98,159,160,-101,-100,]),'DOS_PUNTOS':([19,],[29,]),'IGUAL':([19,57,58,91,93,94,95,137,138,],[30,-22,-23,116,-87,-57,-58,-87,-89,]),'TD_ALFANUMERICO':([29,],[53,]),'TD_NUMERICO':([29,],[54,]),'TD_LOGICO':([29,],[55,]),'CADENA':([30,71,73,74,76,92,104,105,108,109,110,111,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,129,131,140,151,],[57,86,57,57,57,57,86,86,57,-78,-79,57,-72,-73,-74,-75,-76,-77,57,-63,-64,-65,-66,-67,-68,-69,57,57,57,57,57,]),'NUMERICO':([30,73,74,76,92,108,109,110,111,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,129,131,140,151,],[58,58,58,58,58,58,-78,-79,58,-72,-73,-74,-75,-76,-77,58,-63,-64,-65,-66,-67,-68,-69,58,58,58,58,58,]),'PARENTESIS_ABIERTO':([38,39,40,45,46,102,],[71,72,73,75,76,131,]),'ASIGNACION':([44,100,],[74,129,]),'SUMA':([57,58,93,94,95,96,98,137,],[-22,-23,120,-57,-58,-58,120,120,]),'RESTA':([57,58,93,94,95,96,98,137,],[-22,-23,121,-57,-58,-58,121,121,]),'DIVISION':([57,58,93,94,95,96,98,137,],[-22,-23,122,-57,-58,-58,122,122,]),'MULTIPLICACION':([57,58,93,94,95,96,98,137,],[-22,-23,123,-57,-58,-58,123,123,]),'DIVISION_ENTERA':([57,58,93,94,95,96,98,137,],[-22,-23,124,-57,-58,-58,124,124,]),'MODULO':([57,58,93,94,95,96,98,137,],[-22,-23,125,-57,-58,-58,125,125,]),'POTENCIA':([57,58,93,94,95,96,98,137,],[-22,-23,126,-57,-58,-58,126,126,]),'MENOR_QUE':([57,58,91,93,94,95,137,138,],[-22,-23,112,-87,-57,-58,-87,-89,]),'MAYOR_QUE':([57,58,91,93,94,95,137,138,],[-22,-23,113,-87,-57,-58,-87,-89,]),'MENOR_O_IGUAL_QUE':([57,58,91,93,94,95,137,138,],[-22,-23,114,-87,-57,-58,-87,-89,]),'MAYOR_O_IGUAL_QUE':([57,58,91,93,94,95,137,138,],[-22,-23,115,-87,-57,-58,-87,-89,]),'DISTINTO':([57,58,91,93,94,95,137,138,],[-22,-23,117,-87,-57,-58,-87,-89,]),'O':([57,58,90,93,94,95,118,136,137,138,],[-22,-23,109,-87,-57,-58,-86,-85,-87,-89,]),'Y':([57,58,90,93,94,95,118,136,137,138,],[-22,-23,110,-87,-57,-58,-86,-85,-87,-89,]),'PARENTESIS_CERRADO':([57,58,84,85,86,87,88,89,90,93,94,95,99,100,101,118,132,133,135,136,137,138,141,143,],[-22,-23,103,-49,-50,106,-54,107,-83,-87,-57,-58,128,-103,130,-86,-51,-52,-84,-85,-87,-89,-102,148,]),'COMA':([57,58,85,86,94,95,146,],[-22,-23,104,105,-57,-58,151,]),'HACER':([57,58,94,95,130,151,154,],[-22,-23,-57,-58,142,155,156,]),'NO':([73,76,108,109,110,131,],[92,92,92,-78,-79,92,]),'ENTONCES':([107,],[134,]),'HASTA':([128,],[140,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sigma':([0,],[1,]),'ambiente':([7,8,],[9,11,]),'bloque_ambiente':([10,14,15,16,23,25,27,],[13,24,26,28,48,50,51,]),'comentario_vl_l':([10,14,15,16,22,23,25,27,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[14,23,25,27,31,23,23,23,59,62,64,66,68,70,59,59,59,59,59,59,59,59,59,59,59,59,]),'variable':([10,14,15,16,23,25,27,],[15,15,15,15,15,15,15,]),'constante':([10,14,15,16,23,25,27,],[16,16,16,16,16,16,16,]),'proceso':([13,24,],[21,49,]),'conj_sentencia':([22,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[32,60,61,63,65,67,69,77,78,79,80,81,82,83,145,147,145,157,158,]),'s_escribir':([22,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'s_leer':([22,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'s_si':([22,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'s_ciclos':([22,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'sentencia':([22,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'c_para':([22,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'c_mientras':([22,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'c_repetir':([22,31,33,34,35,36,37,47,59,62,64,66,68,70,134,142,150,155,156,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'ftd_amb':([29,],[52,]),'tipo_dato':([30,73,74,76,92,108,111,119,127,129,131,140,151,],[56,95,96,95,95,95,95,95,95,95,95,95,95,]),'salida_esc':([71,104,105,],[84,132,133,]),'entrada_leer':([72,],[87,]),'conj_condiciones':([73,76,108,131,],[89,101,135,143,]),'condicion':([73,76,108,131,],[90,90,90,90,]),'expresion':([73,76,92,108,111,119,131,],[91,91,118,91,136,138,91,]),'id_tipodato':([73,74,76,92,108,111,119,127,129,131,140,151,],[93,98,93,93,93,93,137,139,141,93,146,154,]),'op_aritmetica':([74,],[97,]),'idt_para':([75,],[99,]),'t_op_logico':([90,],[108,]),'t_relacional':([91,],[111,]),'t_op_aritmetico':([93,98,137,],[119,127,119,]),'conj_s_si':([134,150,],[144,153,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sigma","S'",1,None,None,None),
  ('sigma -> COMENTARIO_ENCABEZADO ACCION IDENTIFICADOR ES ambiente FIN_ACCION','sigma',6,'p_sigma','parser.py',12),
  ('sigma -> ACCION IDENTIFICADOR ES ambiente FIN_ACCION','sigma',5,'p_sigma','parser.py',13),
  ('comentario_vl_l -> COMENTARIO_VARIASLINEAS','comentario_vl_l',1,'p_comentario_vl_l','parser.py',18),
  ('comentario_vl_l -> COMENTARIO_LINEA','comentario_vl_l',1,'p_comentario_vl_l','parser.py',19),
  ('ambiente -> AMBIENTE bloque_ambiente proceso','ambiente',3,'p_ambiente','parser.py',23),
  ('ambiente -> AMBIENTE comentario_vl_l bloque_ambiente proceso','ambiente',4,'p_ambiente','parser.py',24),
  ('bloque_ambiente -> variable comentario_vl_l','bloque_ambiente',2,'p_bloque_ambiente','parser.py',29),
  ('bloque_ambiente -> constante comentario_vl_l','bloque_ambiente',2,'p_bloque_ambiente','parser.py',30),
  ('bloque_ambiente -> variable comentario_vl_l bloque_ambiente','bloque_ambiente',3,'p_bloque_ambiente','parser.py',31),
  ('bloque_ambiente -> constante comentario_vl_l bloque_ambiente','bloque_ambiente',3,'p_bloque_ambiente','parser.py',32),
  ('bloque_ambiente -> comentario_vl_l','bloque_ambiente',1,'p_bloque_ambiente','parser.py',33),
  ('bloque_ambiente -> comentario_vl_l bloque_ambiente','bloque_ambiente',2,'p_bloque_ambiente','parser.py',34),
  ('bloque_ambiente -> variable bloque_ambiente','bloque_ambiente',2,'p_bloque_ambiente','parser.py',35),
  ('bloque_ambiente -> constante bloque_ambiente','bloque_ambiente',2,'p_bloque_ambiente','parser.py',36),
  ('bloque_ambiente -> variable','bloque_ambiente',1,'p_bloque_ambiente','parser.py',37),
  ('bloque_ambiente -> constante','bloque_ambiente',1,'p_bloque_ambiente','parser.py',38),
  ('variable -> IDENTIFICADOR DOS_PUNTOS ftd_amb','variable',3,'p_variable','parser.py',43),
  ('constante -> IDENTIFICADOR IGUAL tipo_dato','constante',3,'p_constante','parser.py',47),
  ('ftd_amb -> TD_ALFANUMERICO','ftd_amb',1,'p_ftd_amb','parser.py',58),
  ('ftd_amb -> TD_NUMERICO','ftd_amb',1,'p_ftd_amb','parser.py',59),
  ('ftd_amb -> TD_LOGICO','ftd_amb',1,'p_ftd_amb','parser.py',60),
  ('tipo_dato -> CADENA','tipo_dato',1,'p_tipo_dato','parser.py',64),
  ('tipo_dato -> NUMERICO','tipo_dato',1,'p_tipo_dato','parser.py',65),
  ('proceso -> PROCESO comentario_vl_l conj_sentencia','proceso',3,'p_proceso','parser.py',75),
  ('proceso -> PROCESO conj_sentencia','proceso',2,'p_proceso','parser.py',76),
  ('conj_sentencia -> s_escribir conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',81),
  ('conj_sentencia -> s_escribir comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',82),
  ('conj_sentencia -> s_leer conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',83),
  ('conj_sentencia -> s_leer comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',84),
  ('conj_sentencia -> s_si conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',85),
  ('conj_sentencia -> s_si comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',86),
  ('conj_sentencia -> s_ciclos conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',87),
  ('conj_sentencia -> s_ciclos comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',88),
  ('conj_sentencia -> sentencia conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',89),
  ('conj_sentencia -> sentencia comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',90),
  ('conj_sentencia -> comentario_vl_l conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',91),
  ('conj_sentencia -> s_escribir comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',92),
  ('conj_sentencia -> s_leer comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',93),
  ('conj_sentencia -> s_si comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',94),
  ('conj_sentencia -> s_ciclos comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',95),
  ('conj_sentencia -> sentencia comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',96),
  ('conj_sentencia -> s_escribir','conj_sentencia',1,'p_conj_sentencia','parser.py',97),
  ('conj_sentencia -> s_leer','conj_sentencia',1,'p_conj_sentencia','parser.py',98),
  ('conj_sentencia -> s_si','conj_sentencia',1,'p_conj_sentencia','parser.py',99),
  ('conj_sentencia -> s_ciclos','conj_sentencia',1,'p_conj_sentencia','parser.py',100),
  ('conj_sentencia -> sentencia','conj_sentencia',1,'p_conj_sentencia','parser.py',101),
  ('conj_sentencia -> comentario_vl_l','conj_sentencia',1,'p_conj_sentencia','parser.py',102),
  ('s_escribir -> ESCRIBIR PARENTESIS_ABIERTO salida_esc PARENTESIS_CERRADO','s_escribir',4,'p_s_escribir','parser.py',106),
  ('salida_esc -> IDENTIFICADOR','salida_esc',1,'p_salida_esc','parser.py',110),
  ('salida_esc -> CADENA','salida_esc',1,'p_salida_esc','parser.py',111),
  ('salida_esc -> IDENTIFICADOR COMA salida_esc','salida_esc',3,'p_salida_esc','parser.py',112),
  ('salida_esc -> CADENA COMA salida_esc','salida_esc',3,'p_salida_esc','parser.py',113),
  ('s_leer -> LEER PARENTESIS_ABIERTO entrada_leer PARENTESIS_CERRADO','s_leer',4,'p_s_leer','parser.py',117),
  ('entrada_leer -> IDENTIFICADOR','entrada_leer',1,'p_entrada_leer','parser.py',121),
  ('sentencia -> IDENTIFICADOR ASIGNACION tipo_dato','sentencia',3,'p_sentencia','parser.py',126),
  ('sentencia -> IDENTIFICADOR ASIGNACION op_aritmetica','sentencia',3,'p_sentencia','parser.py',127),
  ('id_tipodato -> IDENTIFICADOR','id_tipodato',1,'p_id_tipodato','parser.py',133),
  ('id_tipodato -> tipo_dato','id_tipodato',1,'p_id_tipodato','parser.py',134),
  ('conj_operaciones -> op_aritmetica','conj_operaciones',1,'p_conj_operaciones','parser.py',140),
  ('conj_operaciones -> relacionales','conj_operaciones',1,'p_conj_operaciones','parser.py',141),
  ('op_aritmetica -> id_tipodato t_op_aritmetico id_tipodato','op_aritmetica',3,'p_op_aritmetica','parser.py',147),
  ('op_aritmetica -> id_tipodato t_op_aritmetico','op_aritmetica',2,'p_op_aritmetica','parser.py',148),
  ('t_op_aritmetico -> SUMA','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',154),
  ('t_op_aritmetico -> RESTA','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',155),
  ('t_op_aritmetico -> DIVISION','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',156),
  ('t_op_aritmetico -> MULTIPLICACION','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',157),
  ('t_op_aritmetico -> DIVISION_ENTERA','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',158),
  ('t_op_aritmetico -> MODULO','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',159),
  ('t_op_aritmetico -> POTENCIA','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',160),
  ('relacionales -> id_tipodato t_relacional id_tipodato','relacionales',3,'p_relacionales','parser.py',166),
  ('relacionales -> id_tipodato t_relacional id_tipodato relacionales','relacionales',4,'p_relacionales','parser.py',167),
  ('t_relacional -> MENOR_QUE','t_relacional',1,'p_t_relacional','parser.py',173),
  ('t_relacional -> MAYOR_QUE','t_relacional',1,'p_t_relacional','parser.py',174),
  ('t_relacional -> MENOR_O_IGUAL_QUE','t_relacional',1,'p_t_relacional','parser.py',175),
  ('t_relacional -> MAYOR_O_IGUAL_QUE','t_relacional',1,'p_t_relacional','parser.py',176),
  ('t_relacional -> IGUAL','t_relacional',1,'p_t_relacional','parser.py',177),
  ('t_relacional -> DISTINTO','t_relacional',1,'p_t_relacional','parser.py',178),
  ('t_op_logico -> O','t_op_logico',1,'p_t_op_logico','parser.py',184),
  ('t_op_logico -> Y','t_op_logico',1,'p_t_op_logico','parser.py',185),
  ('s_si -> SI PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO ENTONCES conj_s_si FIN_SI','s_si',7,'p_s_si','parser.py',190),
  ('conj_s_si -> conj_sentencia','conj_s_si',1,'p_conj_s_si','parser.py',194),
  ('conj_s_si -> conj_sentencia SINO conj_s_si','conj_s_si',3,'p_conj_s_si','parser.py',195),
  ('conj_condiciones -> condicion','conj_condiciones',1,'p_conj_condiciones','parser.py',199),
  ('conj_condiciones -> condicion t_op_logico conj_condiciones','conj_condiciones',3,'p_conj_condiciones','parser.py',200),
  ('condicion -> expresion t_relacional expresion','condicion',3,'p_condicion','parser.py',204),
  ('condicion -> NO expresion','condicion',2,'p_condicion','parser.py',205),
  ('expresion -> id_tipodato','expresion',1,'p_expresion','parser.py',209),
  ('expresion -> id_tipodato t_op_aritmetico id_tipodato','expresion',3,'p_expresion','parser.py',210),
  ('expresion -> id_tipodato t_op_aritmetico expresion','expresion',3,'p_expresion','parser.py',211),
  ('s_segun -> SEGUN PARENTESIS_ABIERTO IDENTIFICADOR PARENTESIS_CERRADO HACER conj_cond_segun FIN_SEGUN','s_segun',7,'p_s_segun','parser.py',215),
  ('conj_cond_segun -> t_relacional id_tipodato DOS_PUNTOS conj_sentencia','conj_cond_segun',4,'p_conj_cond_segun','parser.py',217),
  ('conj_cond_segun -> t_relacional id_tipodato DOS_PUNTOS conj_sentencia conj_cond_segun','conj_cond_segun',5,'p_conj_cond_segun','parser.py',218),
  ('conj_cond_segun -> OTRO DOS_PUNTOS conj_sentencia','conj_cond_segun',3,'p_conj_cond_segun','parser.py',219),
  ('s_ciclos -> c_para','s_ciclos',1,'p_s_ciclos','parser.py',223),
  ('s_ciclos -> c_mientras','s_ciclos',1,'p_s_ciclos','parser.py',224),
  ('s_ciclos -> c_repetir','s_ciclos',1,'p_s_ciclos','parser.py',225),
  ('s_ciclos -> conj_sentencia','s_ciclos',1,'p_s_ciclos','parser.py',226),
  ('c_mientras -> MIENTRAS PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO HACER conj_sentencia FIN_MIENTRAS','c_mientras',7,'p_c_mientras','parser.py',234),
  ('c_repetir -> REPETIR conj_sentencia HASTA_QUE PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO','c_repetir',6,'p_c_repetir','parser.py',239),
  ('c_para -> PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA id_tipodato HACER conj_sentencia FIN_PARA','c_para',11,'p_c_para','parser.py',243),
  ('c_para -> PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA HACER conj_sentencia FIN_PARA','c_para',10,'p_c_para','parser.py',244),
  ('idt_para -> IDENTIFICADOR ASIGNACION id_tipodato','idt_para',3,'p_idt_para','parser.py',248),
  ('idt_para -> IDENTIFICADOR','idt_para',1,'p_idt_para','parser.py',249),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',258),
]
