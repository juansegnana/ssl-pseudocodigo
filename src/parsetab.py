
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightCOMENTARIO_ENCABEZADOrightIDENTIFICADORPROCESOSIMIENTRASREPETIRFIN_ACCIONrightASIGNACIONrightIGUALleftDISTINTOleftMENOR_QUEMENOR_O_IGUAL_QUEMAYOR_QUEMAYOR_O_IGUAL_QUEleftSUMARESTAleftMULTIPLICACIONDIVISIONleftPARENTESIS_ABIERTOPARENTESIS_CERRADOACCION AMBIENTE ASIGNACION CADENA COMA COMENTARIO_ENCABEZADO COMENTARIO_LINEA COMENTARIO_VARIASLINEAS DISTINTO DIVISION DIVISION_ENTERA DOS_PUNTOS ENTONCES ES ESCRIBIR FIN_ACCION FIN_MIENTRAS FIN_PARA FIN_SEGUN FIN_SI HACER HASTA HASTA_QUE IDENTIFICADOR IGUAL LEER MAYOR_O_IGUAL_QUE MAYOR_QUE MENOR_O_IGUAL_QUE MENOR_QUE MIENTRAS MODULO MULTIPLICACION NO NUMERICO O OTRO PARA PARENTESIS_ABIERTO PARENTESIS_CERRADO POTENCIA PROCESO REPETIR RESTA SEGUN SEMICOLON SI SINO SUMA TD_ALFANUMERICO TD_LOGICO TD_NUMERICO Y sigma : ejecucion ejecucion : COMENTARIO_ENCABEZADO nombre bloque FIN_ACCION\n                | COMENTARIO_ENCABEZADO nombre bloque FIN_ACCION comentario_vl_l\n                | nombre bloque FIN_ACCION comentario_vl_l\n                | nombre bloque FIN_ACCION \n    nombre : ACCION IDENTIFICADOR EScomentario_vl_l : COMENTARIO_VARIASLINEAS\n                    | COMENTARIO_LINEA\n    bloque : ambiente procesoambiente : AMBIENTE bloque_ambiente\n                | AMBIENTE comentario_vl_l bloque_ambiente\n    \n        bloque_ambiente : variable comentario_vl_l\n                    | constante comentario_vl_l\n                    | comentario_vl_l\n                    | variable\n                    | constante\n     bloque_ambiente : variable comentario_vl_l bloque_ambiente\n                    | constante comentario_vl_l bloque_ambiente\n                    | comentario_vl_l bloque_ambiente\n                    | variable bloque_ambiente\n                    | constante bloque_ambiente \n    variable : IDENTIFICADOR DOS_PUNTOS ftd_ambconstante : IDENTIFICADOR IGUAL tipo_datoftd_amb : TD_ALFANUMERICO \n            | TD_NUMERICO\n            | TD_LOGICO tipo_dato : CADENA \n                | NUMERICO\n    \n        proceso : PROCESO comentario_vl_l conj_sentencia\n            | PROCESO conj_sentencia\n    conj_sentencia : s_escribir conj_sentencia \n                    | s_escribir comentario_vl_l conj_sentencia\n                    | s_leer conj_sentencia \n                    | s_leer comentario_vl_l conj_sentencia \n                    | s_si conj_sentencia \n                    | s_si comentario_vl_l conj_sentencia \n                    | s_segun conj_sentencia\n                    | s_segun comentario_vl_l conj_sentencia\n                    | s_ciclos conj_sentencia \n                    | s_ciclos comentario_vl_l conj_sentencia \n                    | sentencia conj_sentencia \n                    | sentencia comentario_vl_l conj_sentencia \n                    | comentario_vl_l conj_sentencia \n                    | s_escribir comentario_vl_l \n                    | s_leer comentario_vl_l \n                    | s_si comentario_vl_l\n                    | s_segun comentario_vl_l\n                    | s_ciclos comentario_vl_l \n                    | sentencia comentario_vl_l \n                    | s_escribir \n                    | s_leer \n                    | s_si \n                    | s_segun\n                    | s_ciclos \n                    | sentencia \n                    | comentario_vl_l\n    s_escribir : ESCRIBIR PARENTESIS_ABIERTO salida_esc PARENTESIS_CERRADOsalida_esc : IDENTIFICADOR \n                | CADENA \n                | IDENTIFICADOR COMA salida_esc \n                | CADENA COMA salida_escs_leer : LEER PARENTESIS_ABIERTO entrada_leer PARENTESIS_CERRADOentrada_leer : IDENTIFICADOR\n        sentencia : IDENTIFICADOR ASIGNACION tipo_dato\n                | IDENTIFICADOR ASIGNACION op_aritmetica\n    \n        id_tipodato : IDENTIFICADOR\n                | tipo_dato\n    \n        op_aritmetica : id_tipodato t_op_aritmetico id_tipodato\n                    | id_tipodato t_op_aritmetico\n    \n        t_op_aritmetico : SUMA\n                        | RESTA\n                        | DIVISION\n                        | MULTIPLICACION\n                        | DIVISION_ENTERA\n                        | MODULO\n                        | POTENCIA\n    \n        t_relacional : MENOR_QUE\n                    | MAYOR_QUE\n                    | MENOR_O_IGUAL_QUE\n                    | MAYOR_O_IGUAL_QUE\n                    | IGUAL\n                    | DISTINTO\n    \n        t_op_logico : O\n                | Y\n    s_si : SI PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO ENTONCES conj_s_si FIN_SIconj_s_si : conj_sentencia  \n                | conj_sentencia SINO conj_s_siconj_condiciones : condicion \n                        | condicion t_op_logico conj_condicionescondicion : expresion t_relacional expresion \n                | NO expresionexpresion : id_tipodato \n                | id_tipodato t_op_aritmetico id_tipodato \n                | id_tipodato t_op_aritmetico expresions_segun : SEGUN PARENTESIS_ABIERTO IDENTIFICADOR PARENTESIS_CERRADO HACER conj_cond_segun FIN_SEGUNconj_cond_segun : t_relacional id_tipodato DOS_PUNTOS conj_sentencia \n                    | t_relacional id_tipodato DOS_PUNTOS conj_sentencia conj_cond_segun \n                    | OTRO DOS_PUNTOS conj_sentencias_ciclos : c_para \n            | c_mientras \n            | c_repetir \n            | conj_sentencia\n        c_mientras : MIENTRAS PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO HACER conj_sentencia FIN_MIENTRAS\n    c_repetir : REPETIR conj_sentencia HASTA_QUE PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO\n        c_para : PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA id_tipodato HACER conj_sentencia FIN_PARA\n            | PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA HACER conj_sentencia FIN_PARA \n    idt_para : IDENTIFICADOR ASIGNACION id_tipodato \n            | IDENTIFICADOR\n    '
    
_lr_action_items = {'COMENTARIO_ENCABEZADO':([0,],[3,]),'ACCION':([0,3,],[5,5,]),'$end':([1,2,12,19,20,23,24,52,],[0,-1,-5,-7,-8,-2,-4,-3,]),'AMBIENTE':([4,6,22,],[9,9,-6,]),'IDENTIFICADOR':([5,9,14,16,17,18,19,20,25,26,27,28,29,30,31,32,38,39,40,43,44,46,48,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,100,102,103,105,106,112,113,114,115,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,137,139,141,144,150,151,153,156,158,161,162,163,164,165,167,168,169,171,172,174,175,176,177,179,180,181,],[10,21,37,21,21,21,-7,-8,37,-102,37,37,37,37,37,37,-99,-100,-101,37,21,21,21,37,-43,-31,37,-33,37,-35,37,-37,37,-39,37,-41,37,93,96,102,104,102,109,102,-102,-22,-24,-25,-26,-23,-27,-28,-43,-32,-34,-36,-38,-40,-42,102,-66,-67,-64,-65,-57,93,93,-62,102,-83,-84,102,-77,-78,-79,-80,-81,-82,102,-70,-71,-72,-73,-74,-75,-76,102,102,102,37,-68,102,37,-102,102,-102,-104,-85,37,-95,37,102,-103,37,-102,37,-102,37,-102,-102,-106,-105,]),'FIN_ACCION':([7,11,13,19,20,25,26,27,28,29,30,31,32,38,39,40,53,54,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,150,162,163,165,169,180,181,],[12,23,-9,-7,-8,-56,-30,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-29,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-68,-104,-85,-95,-103,-106,-105,]),'PROCESO':([8,15,16,17,18,19,20,44,45,46,47,48,49,75,76,77,78,79,80,81,82,83,84,],[14,-10,-14,-15,-16,-7,-8,-14,-11,-12,-20,-13,-21,-19,-17,-18,-22,-24,-25,-26,-23,-27,-28,]),'COMENTARIO_VARIASLINEAS':([9,12,14,16,17,18,19,20,23,25,26,27,28,29,30,31,32,38,39,40,43,44,46,48,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,144,150,153,156,161,162,163,164,165,167,169,171,172,174,175,176,177,179,180,181,],[19,19,19,19,19,19,-7,-8,19,19,-102,19,19,19,19,19,19,-99,-100,-101,19,19,19,19,19,-43,-31,19,-33,19,-35,19,-37,19,-39,19,-41,19,-102,-22,-24,-25,-26,-23,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,19,-68,19,-102,-102,-104,-85,19,-95,19,-103,19,-102,19,-102,19,-102,-102,-106,-105,]),'COMENTARIO_LINEA':([9,12,14,16,17,18,19,20,23,25,26,27,28,29,30,31,32,38,39,40,43,44,46,48,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,144,150,153,156,161,162,163,164,165,167,169,171,172,174,175,176,177,179,180,181,],[20,20,20,20,20,20,-7,-8,20,20,-102,20,20,20,20,20,20,-99,-100,-101,20,20,20,20,20,-43,-31,20,-33,20,-35,20,-37,20,-39,20,-41,20,-102,-22,-24,-25,-26,-23,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,20,-68,20,-102,-102,-104,-85,20,-95,20,-103,20,-102,20,-102,20,-102,-102,-106,-105,]),'ES':([10,],[22,]),'ESCRIBIR':([14,19,20,25,26,27,28,29,30,31,32,38,39,40,43,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,144,150,153,156,161,162,163,164,165,167,169,171,172,174,175,176,177,179,180,181,],[33,-7,-8,33,-102,33,33,33,33,33,33,-99,-100,-101,33,33,-43,-31,33,-33,33,-35,33,-37,33,-39,33,-41,33,-102,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,33,-68,33,-102,-102,-104,-85,33,-95,33,-103,33,-102,33,-102,33,-102,-102,-106,-105,]),'LEER':([14,19,20,25,26,27,28,29,30,31,32,38,39,40,43,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,144,150,153,156,161,162,163,164,165,167,169,171,172,174,175,176,177,179,180,181,],[34,-7,-8,34,-102,34,34,34,34,34,34,-99,-100,-101,34,34,-43,-31,34,-33,34,-35,34,-37,34,-39,34,-41,34,-102,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,34,-68,34,-102,-102,-104,-85,34,-95,34,-103,34,-102,34,-102,34,-102,-102,-106,-105,]),'SI':([14,19,20,25,26,27,28,29,30,31,32,38,39,40,43,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,144,150,153,156,161,162,163,164,165,167,169,171,172,174,175,176,177,179,180,181,],[35,-7,-8,35,-102,35,35,35,35,35,35,-99,-100,-101,35,35,-43,-31,35,-33,35,-35,35,-37,35,-39,35,-41,35,-102,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,35,-68,35,-102,-102,-104,-85,35,-95,35,-103,35,-102,35,-102,35,-102,-102,-106,-105,]),'SEGUN':([14,19,20,25,26,27,28,29,30,31,32,38,39,40,43,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,144,150,153,156,161,162,163,164,165,167,169,171,172,174,175,176,177,179,180,181,],[36,-7,-8,36,-102,36,36,36,36,36,36,-99,-100,-101,36,36,-43,-31,36,-33,36,-35,36,-37,36,-39,36,-41,36,-102,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,36,-68,36,-102,-102,-104,-85,36,-95,36,-103,36,-102,36,-102,36,-102,-102,-106,-105,]),'PARA':([14,19,20,25,26,27,28,29,30,31,32,38,39,40,43,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,144,150,153,156,161,162,163,164,165,167,169,171,172,174,175,176,177,179,180,181,],[41,-7,-8,41,-102,41,41,41,41,41,41,-99,-100,-101,41,41,-43,-31,41,-33,41,-35,41,-37,41,-39,41,-41,41,-102,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,41,-68,41,-102,-102,-104,-85,41,-95,41,-103,41,-102,41,-102,41,-102,-102,-106,-105,]),'MIENTRAS':([14,19,20,25,26,27,28,29,30,31,32,38,39,40,43,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,144,150,153,156,161,162,163,164,165,167,169,171,172,174,175,176,177,179,180,181,],[42,-7,-8,42,-102,42,42,42,42,42,42,-99,-100,-101,42,42,-43,-31,42,-33,42,-35,42,-37,42,-39,42,-41,42,-102,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,42,-68,42,-102,-102,-104,-85,42,-95,42,-103,42,-102,42,-102,42,-102,-102,-106,-105,]),'REPETIR':([14,19,20,25,26,27,28,29,30,31,32,38,39,40,43,53,54,55,56,57,58,59,60,61,62,63,64,65,66,74,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,144,150,153,156,161,162,163,164,165,167,169,171,172,174,175,176,177,179,180,181,],[43,-7,-8,43,-102,43,43,43,43,43,43,-99,-100,-101,43,43,-43,-31,43,-33,43,-35,43,-37,43,-39,43,-41,43,-102,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,43,-68,43,-102,-102,-104,-85,43,-95,43,-103,43,-102,43,-102,43,-102,-102,-106,-105,]),'HASTA_QUE':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,74,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,150,162,163,165,169,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,111,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-68,-104,-85,-95,-103,-106,-105,]),'SINO':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,150,156,162,163,165,169,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-68,164,-104,-85,-95,-103,-106,-105,]),'FIN_SI':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,150,155,156,162,163,165,169,170,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-68,163,-86,-104,-85,-95,-103,-87,-106,-105,]),'FIN_MIENTRAS':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,150,161,162,163,165,169,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-68,169,-104,-85,-95,-103,-106,-105,]),'FIN_SEGUN':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,150,157,162,163,165,169,172,175,178,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-68,165,-104,-85,-95,-103,-98,-96,-97,-106,-105,]),'OTRO':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,149,150,162,163,165,169,175,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,159,-68,-104,-85,-95,-103,159,-106,-105,]),'MENOR_QUE':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,99,101,102,103,105,106,112,115,129,130,131,132,133,134,135,137,147,148,149,150,162,163,165,169,175,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,121,-92,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-92,-94,121,-68,-104,-85,-95,-103,121,-106,-105,]),'MAYOR_QUE':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,99,101,102,103,105,106,112,115,129,130,131,132,133,134,135,137,147,148,149,150,162,163,165,169,175,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,122,-92,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-92,-94,122,-68,-104,-85,-95,-103,122,-106,-105,]),'MENOR_O_IGUAL_QUE':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,99,101,102,103,105,106,112,115,129,130,131,132,133,134,135,137,147,148,149,150,162,163,165,169,175,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,123,-92,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-92,-94,123,-68,-104,-85,-95,-103,123,-106,-105,]),'MAYOR_O_IGUAL_QUE':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,99,101,102,103,105,106,112,115,129,130,131,132,133,134,135,137,147,148,149,150,162,163,165,169,175,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,124,-92,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-92,-94,124,-68,-104,-85,-95,-103,124,-106,-105,]),'IGUAL':([19,20,21,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,99,101,102,103,105,106,112,115,129,130,131,132,133,134,135,137,147,148,149,150,162,163,165,169,175,180,181,],[-7,-8,51,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,125,-92,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-92,-94,125,-68,-104,-85,-95,-103,125,-106,-105,]),'DISTINTO':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,99,101,102,103,105,106,112,115,129,130,131,132,133,134,135,137,147,148,149,150,162,163,165,169,175,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,126,-92,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-92,-94,126,-68,-104,-85,-95,-103,126,-106,-105,]),'FIN_PARA':([19,20,27,28,29,30,31,32,38,39,40,53,55,56,57,58,59,60,61,62,63,64,65,66,83,84,85,86,87,88,89,90,91,102,103,105,106,112,115,129,130,131,132,133,134,135,137,150,162,163,165,169,177,179,180,181,],[-7,-8,-50,-51,-52,-53,-54,-55,-99,-100,-101,-56,-31,-44,-33,-45,-35,-46,-37,-47,-39,-48,-41,-49,-27,-28,-43,-32,-34,-36,-38,-40,-42,-66,-67,-64,-65,-57,-62,-70,-71,-72,-73,-74,-75,-76,-69,-68,-104,-85,-95,-103,180,181,-106,-105,]),'DOS_PUNTOS':([21,83,84,102,103,159,166,],[50,-27,-28,-66,-67,167,171,]),'PARENTESIS_ABIERTO':([33,34,35,36,41,42,111,],[67,68,69,70,72,73,141,]),'ASIGNACION':([37,109,],[71,139,]),'TD_ALFANUMERICO':([50,],[79,]),'TD_NUMERICO':([50,],[80,]),'TD_LOGICO':([50,],[81,]),'CADENA':([51,67,69,71,73,100,113,114,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,137,139,141,151,158,168,],[83,94,83,83,83,83,94,94,83,-83,-84,83,-77,-78,-79,-80,-81,-82,83,-70,-71,-72,-73,-74,-75,-76,83,83,83,83,83,83,]),'NUMERICO':([51,69,71,73,100,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,137,139,141,151,158,168,],[84,84,84,84,84,84,-83,-84,84,-77,-78,-79,-80,-81,-82,84,-70,-71,-72,-73,-74,-75,-76,84,84,84,84,84,84,]),'NO':([69,73,117,118,119,141,],[100,100,100,-83,-84,100,]),'SUMA':([83,84,101,102,103,105,107,147,],[-27,-28,129,-66,-67,-67,129,129,]),'RESTA':([83,84,101,102,103,105,107,147,],[-27,-28,130,-66,-67,-67,130,130,]),'DIVISION':([83,84,101,102,103,105,107,147,],[-27,-28,131,-66,-67,-67,131,131,]),'MULTIPLICACION':([83,84,101,102,103,105,107,147,],[-27,-28,132,-66,-67,-67,132,132,]),'DIVISION_ENTERA':([83,84,101,102,103,105,107,147,],[-27,-28,133,-66,-67,-67,133,133,]),'MODULO':([83,84,101,102,103,105,107,147,],[-27,-28,134,-66,-67,-67,134,134,]),'POTENCIA':([83,84,101,102,103,105,107,147,],[-27,-28,135,-66,-67,-67,135,135,]),'O':([83,84,98,101,102,103,127,146,147,148,],[-27,-28,118,-92,-66,-67,-91,-90,-92,-94,]),'Y':([83,84,98,101,102,103,127,146,147,148,],[-27,-28,119,-92,-66,-67,-91,-90,-92,-94,]),'PARENTESIS_CERRADO':([83,84,92,93,94,95,96,97,98,101,102,103,104,108,109,110,127,142,143,145,146,147,148,152,154,],[-27,-28,112,-58,-59,115,-63,116,-88,-92,-66,-67,136,138,-108,140,-91,-60,-61,-89,-90,-92,-94,-107,162,]),'COMA':([83,84,93,94,102,103,160,],[-27,-28,113,114,-66,-67,168,]),'HACER':([83,84,102,103,136,140,168,173,],[-27,-28,-66,-67,149,153,174,176,]),'ENTONCES':([116,],[144,]),'HASTA':([138,],[151,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sigma':([0,],[1,]),'ejecucion':([0,],[2,]),'nombre':([0,3,],[4,6,]),'bloque':([4,6,],[7,11,]),'ambiente':([4,6,],[8,8,]),'proceso':([8,],[13,]),'bloque_ambiente':([9,16,17,18,44,46,48,],[15,45,47,49,75,76,77,]),'comentario_vl_l':([9,12,14,16,17,18,23,25,27,28,29,30,31,32,43,44,46,48,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[16,24,25,44,46,48,52,53,56,58,60,62,64,66,53,44,44,44,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'variable':([9,16,17,18,44,46,48,],[17,17,17,17,17,17,17,]),'constante':([9,16,17,18,44,46,48,],[18,18,18,18,18,18,18,]),'conj_sentencia':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[26,54,55,57,59,61,63,65,74,85,86,87,88,89,90,91,156,161,156,172,175,177,179,]),'s_escribir':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'s_leer':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'s_si':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'s_segun':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'s_ciclos':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'sentencia':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'c_para':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'c_mientras':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'c_repetir':([14,25,27,28,29,30,31,32,43,53,56,58,60,62,64,66,144,153,164,167,171,174,176,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'ftd_amb':([50,],[78,]),'tipo_dato':([51,69,71,73,100,117,120,128,137,139,141,151,158,168,],[82,103,105,103,103,103,103,103,103,103,103,103,103,103,]),'salida_esc':([67,113,114,],[92,142,143,]),'entrada_leer':([68,],[95,]),'conj_condiciones':([69,73,117,141,],[97,110,145,154,]),'condicion':([69,73,117,141,],[98,98,98,98,]),'expresion':([69,73,100,117,120,128,141,],[99,99,127,99,146,148,99,]),'id_tipodato':([69,71,73,100,117,120,128,137,139,141,151,158,168,],[101,107,101,101,101,101,147,150,152,101,160,166,173,]),'op_aritmetica':([71,],[106,]),'idt_para':([72,],[108,]),'t_op_logico':([98,],[117,]),'t_relacional':([99,149,175,],[120,158,158,]),'t_op_aritmetico':([101,107,147,],[128,137,128,]),'conj_s_si':([144,164,],[155,170,]),'conj_cond_segun':([149,175,],[157,178,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sigma","S'",1,None,None,None),
  ('sigma -> ejecucion','sigma',1,'p_sigma','parser.py',39),
  ('ejecucion -> COMENTARIO_ENCABEZADO nombre bloque FIN_ACCION','ejecucion',4,'p_ejecucion','parser.py',45),
  ('ejecucion -> COMENTARIO_ENCABEZADO nombre bloque FIN_ACCION comentario_vl_l','ejecucion',5,'p_ejecucion','parser.py',46),
  ('ejecucion -> nombre bloque FIN_ACCION comentario_vl_l','ejecucion',4,'p_ejecucion','parser.py',47),
  ('ejecucion -> nombre bloque FIN_ACCION','ejecucion',3,'p_ejecucion','parser.py',48),
  ('nombre -> ACCION IDENTIFICADOR ES','nombre',3,'p_nombre','parser.py',60),
  ('comentario_vl_l -> COMENTARIO_VARIASLINEAS','comentario_vl_l',1,'p_comentario_vl_l','parser.py',67),
  ('comentario_vl_l -> COMENTARIO_LINEA','comentario_vl_l',1,'p_comentario_vl_l','parser.py',68),
  ('bloque -> ambiente proceso','bloque',2,'p_bloque','parser.py',74),
  ('ambiente -> AMBIENTE bloque_ambiente','ambiente',2,'p_ambiente','parser.py',77),
  ('ambiente -> AMBIENTE comentario_vl_l bloque_ambiente','ambiente',3,'p_ambiente','parser.py',78),
  ('bloque_ambiente -> variable comentario_vl_l','bloque_ambiente',2,'p_bloque_ambiente_scr','parser.py',85),
  ('bloque_ambiente -> constante comentario_vl_l','bloque_ambiente',2,'p_bloque_ambiente_scr','parser.py',86),
  ('bloque_ambiente -> comentario_vl_l','bloque_ambiente',1,'p_bloque_ambiente_scr','parser.py',87),
  ('bloque_ambiente -> variable','bloque_ambiente',1,'p_bloque_ambiente_scr','parser.py',88),
  ('bloque_ambiente -> constante','bloque_ambiente',1,'p_bloque_ambiente_scr','parser.py',89),
  ('bloque_ambiente -> variable comentario_vl_l bloque_ambiente','bloque_ambiente',3,'p_bloque_ambiente_cc','parser.py',95),
  ('bloque_ambiente -> constante comentario_vl_l bloque_ambiente','bloque_ambiente',3,'p_bloque_ambiente_cc','parser.py',96),
  ('bloque_ambiente -> comentario_vl_l bloque_ambiente','bloque_ambiente',2,'p_bloque_ambiente_cc','parser.py',97),
  ('bloque_ambiente -> variable bloque_ambiente','bloque_ambiente',2,'p_bloque_ambiente_cc','parser.py',98),
  ('bloque_ambiente -> constante bloque_ambiente','bloque_ambiente',2,'p_bloque_ambiente_cc','parser.py',99),
  ('variable -> IDENTIFICADOR DOS_PUNTOS ftd_amb','variable',3,'p_variable','parser.py',105),
  ('constante -> IDENTIFICADOR IGUAL tipo_dato','constante',3,'p_constante','parser.py',110),
  ('ftd_amb -> TD_ALFANUMERICO','ftd_amb',1,'p_ftd_amb','parser.py',115),
  ('ftd_amb -> TD_NUMERICO','ftd_amb',1,'p_ftd_amb','parser.py',116),
  ('ftd_amb -> TD_LOGICO','ftd_amb',1,'p_ftd_amb','parser.py',117),
  ('tipo_dato -> CADENA','tipo_dato',1,'p_tipo_dato','parser.py',122),
  ('tipo_dato -> NUMERICO','tipo_dato',1,'p_tipo_dato','parser.py',123),
  ('proceso -> PROCESO comentario_vl_l conj_sentencia','proceso',3,'p_proceso','parser.py',130),
  ('proceso -> PROCESO conj_sentencia','proceso',2,'p_proceso','parser.py',131),
  ('conj_sentencia -> s_escribir conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',166),
  ('conj_sentencia -> s_escribir comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',167),
  ('conj_sentencia -> s_leer conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',168),
  ('conj_sentencia -> s_leer comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',169),
  ('conj_sentencia -> s_si conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',170),
  ('conj_sentencia -> s_si comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',171),
  ('conj_sentencia -> s_segun conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',172),
  ('conj_sentencia -> s_segun comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',173),
  ('conj_sentencia -> s_ciclos conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',174),
  ('conj_sentencia -> s_ciclos comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',175),
  ('conj_sentencia -> sentencia conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',176),
  ('conj_sentencia -> sentencia comentario_vl_l conj_sentencia','conj_sentencia',3,'p_conj_sentencia','parser.py',177),
  ('conj_sentencia -> comentario_vl_l conj_sentencia','conj_sentencia',2,'p_conj_sentencia','parser.py',178),
  ('conj_sentencia -> s_escribir comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',179),
  ('conj_sentencia -> s_leer comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',180),
  ('conj_sentencia -> s_si comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',181),
  ('conj_sentencia -> s_segun comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',182),
  ('conj_sentencia -> s_ciclos comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',183),
  ('conj_sentencia -> sentencia comentario_vl_l','conj_sentencia',2,'p_conj_sentencia','parser.py',184),
  ('conj_sentencia -> s_escribir','conj_sentencia',1,'p_conj_sentencia','parser.py',185),
  ('conj_sentencia -> s_leer','conj_sentencia',1,'p_conj_sentencia','parser.py',186),
  ('conj_sentencia -> s_si','conj_sentencia',1,'p_conj_sentencia','parser.py',187),
  ('conj_sentencia -> s_segun','conj_sentencia',1,'p_conj_sentencia','parser.py',188),
  ('conj_sentencia -> s_ciclos','conj_sentencia',1,'p_conj_sentencia','parser.py',189),
  ('conj_sentencia -> sentencia','conj_sentencia',1,'p_conj_sentencia','parser.py',190),
  ('conj_sentencia -> comentario_vl_l','conj_sentencia',1,'p_conj_sentencia','parser.py',191),
  ('s_escribir -> ESCRIBIR PARENTESIS_ABIERTO salida_esc PARENTESIS_CERRADO','s_escribir',4,'p_s_escribir','parser.py',198),
  ('salida_esc -> IDENTIFICADOR','salida_esc',1,'p_salida_esc','parser.py',203),
  ('salida_esc -> CADENA','salida_esc',1,'p_salida_esc','parser.py',204),
  ('salida_esc -> IDENTIFICADOR COMA salida_esc','salida_esc',3,'p_salida_esc','parser.py',205),
  ('salida_esc -> CADENA COMA salida_esc','salida_esc',3,'p_salida_esc','parser.py',206),
  ('s_leer -> LEER PARENTESIS_ABIERTO entrada_leer PARENTESIS_CERRADO','s_leer',4,'p_s_leer','parser.py',211),
  ('entrada_leer -> IDENTIFICADOR','entrada_leer',1,'p_entrada_leer','parser.py',216),
  ('sentencia -> IDENTIFICADOR ASIGNACION tipo_dato','sentencia',3,'p_sentencia','parser.py',222),
  ('sentencia -> IDENTIFICADOR ASIGNACION op_aritmetica','sentencia',3,'p_sentencia','parser.py',223),
  ('id_tipodato -> IDENTIFICADOR','id_tipodato',1,'p_id_tipodato','parser.py',230),
  ('id_tipodato -> tipo_dato','id_tipodato',1,'p_id_tipodato','parser.py',231),
  ('op_aritmetica -> id_tipodato t_op_aritmetico id_tipodato','op_aritmetica',3,'p_op_aritmetica','parser.py',238),
  ('op_aritmetica -> id_tipodato t_op_aritmetico','op_aritmetica',2,'p_op_aritmetica','parser.py',239),
  ('t_op_aritmetico -> SUMA','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',246),
  ('t_op_aritmetico -> RESTA','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',247),
  ('t_op_aritmetico -> DIVISION','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',248),
  ('t_op_aritmetico -> MULTIPLICACION','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',249),
  ('t_op_aritmetico -> DIVISION_ENTERA','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',250),
  ('t_op_aritmetico -> MODULO','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',251),
  ('t_op_aritmetico -> POTENCIA','t_op_aritmetico',1,'p_t_op_aritmetico','parser.py',252),
  ('t_relacional -> MENOR_QUE','t_relacional',1,'p_t_relacional','parser.py',266),
  ('t_relacional -> MAYOR_QUE','t_relacional',1,'p_t_relacional','parser.py',267),
  ('t_relacional -> MENOR_O_IGUAL_QUE','t_relacional',1,'p_t_relacional','parser.py',268),
  ('t_relacional -> MAYOR_O_IGUAL_QUE','t_relacional',1,'p_t_relacional','parser.py',269),
  ('t_relacional -> IGUAL','t_relacional',1,'p_t_relacional','parser.py',270),
  ('t_relacional -> DISTINTO','t_relacional',1,'p_t_relacional','parser.py',271),
  ('t_op_logico -> O','t_op_logico',1,'p_t_op_logico','parser.py',278),
  ('t_op_logico -> Y','t_op_logico',1,'p_t_op_logico','parser.py',279),
  ('s_si -> SI PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO ENTONCES conj_s_si FIN_SI','s_si',7,'p_s_si','parser.py',285),
  ('conj_s_si -> conj_sentencia','conj_s_si',1,'p_conj_s_si','parser.py',290),
  ('conj_s_si -> conj_sentencia SINO conj_s_si','conj_s_si',3,'p_conj_s_si','parser.py',291),
  ('conj_condiciones -> condicion','conj_condiciones',1,'p_conj_condiciones','parser.py',296),
  ('conj_condiciones -> condicion t_op_logico conj_condiciones','conj_condiciones',3,'p_conj_condiciones','parser.py',297),
  ('condicion -> expresion t_relacional expresion','condicion',3,'p_condicion','parser.py',302),
  ('condicion -> NO expresion','condicion',2,'p_condicion','parser.py',303),
  ('expresion -> id_tipodato','expresion',1,'p_expresion','parser.py',308),
  ('expresion -> id_tipodato t_op_aritmetico id_tipodato','expresion',3,'p_expresion','parser.py',309),
  ('expresion -> id_tipodato t_op_aritmetico expresion','expresion',3,'p_expresion','parser.py',310),
  ('s_segun -> SEGUN PARENTESIS_ABIERTO IDENTIFICADOR PARENTESIS_CERRADO HACER conj_cond_segun FIN_SEGUN','s_segun',7,'p_s_segun','parser.py',315),
  ('conj_cond_segun -> t_relacional id_tipodato DOS_PUNTOS conj_sentencia','conj_cond_segun',4,'p_conj_cond_segun','parser.py',320),
  ('conj_cond_segun -> t_relacional id_tipodato DOS_PUNTOS conj_sentencia conj_cond_segun','conj_cond_segun',5,'p_conj_cond_segun','parser.py',321),
  ('conj_cond_segun -> OTRO DOS_PUNTOS conj_sentencia','conj_cond_segun',3,'p_conj_cond_segun','parser.py',322),
  ('s_ciclos -> c_para','s_ciclos',1,'p_s_ciclos','parser.py',327),
  ('s_ciclos -> c_mientras','s_ciclos',1,'p_s_ciclos','parser.py',328),
  ('s_ciclos -> c_repetir','s_ciclos',1,'p_s_ciclos','parser.py',329),
  ('s_ciclos -> conj_sentencia','s_ciclos',1,'p_s_ciclos','parser.py',330),
  ('c_mientras -> MIENTRAS PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO HACER conj_sentencia FIN_MIENTRAS','c_mientras',7,'p_c_mientras','parser.py',338),
  ('c_repetir -> REPETIR conj_sentencia HASTA_QUE PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO','c_repetir',6,'p_c_repetir','parser.py',344),
  ('c_para -> PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA id_tipodato HACER conj_sentencia FIN_PARA','c_para',11,'p_c_para','parser.py',350),
  ('c_para -> PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA HACER conj_sentencia FIN_PARA','c_para',10,'p_c_para','parser.py',351),
  ('idt_para -> IDENTIFICADOR ASIGNACION id_tipodato','idt_para',3,'p_idt_para','parser.py',357),
  ('idt_para -> IDENTIFICADOR','idt_para',1,'p_idt_para','parser.py',358),
]
