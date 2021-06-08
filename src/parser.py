import ply.yacc as yacc # parser 
from lexer import tokens
import argparse

#Obtener path de texto por terminal
argParser = argparse.ArgumentParser(description='Procesa tokens de pseudocodigo.')
argParser.add_argument('-f', '-pathFile', nargs='?',type=str, help='especificar ruta de archivo de texto de entrada a analizar.')
argsParser = argParser.parse_args()
pathFile = argsParser.f
# Corregir ambiguedad  --> http://www.dabeaz.com/ply/ply.html#ply_nn27 

# precedence = (
#     ('nonassoc', 'MENOR_QUE', 'MENOR_O_IGUAL_QUE', 'MAYOR_QUE', 'MAYOR_O_IGUAL_QUE'),  # Nonassociative operators -> NO PERMITE a < b < c
#     ('left', 'PROCESO', 'IDENTIFICADOR'),
#     ('left', 'ASIGNACION'),
#     ('left', 'SUMA', 'RESTA'),
#     ('left', 'MULTIPLICACION', 'DIVISION', 'DIVISION_ENTERA', 'MODULO', 'POTENCIA'),
#     ('left', 'PARENTESIS_ABIERTO', 'PARENTESIS_CERRADO')
# )

precedence = (
    ('right','COMENTARIO_ENCABEZADO'),
    ('right','IDENTIFICADOR','PROCESO','SI','MIENTRAS', 'REPETIR'),
    ('right','ASIGNACION'),
    ('right','IGUAL'),
    ('left','DISTINTO'),
    ('left','MENOR_QUE','MENOR_O_IGUAL_QUE','MAYOR_QUE','MAYOR_O_IGUAL_QUE'),
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICACION','DIVISION'),
    ('left','PARENTESIS_ABIERTO','PARENTESIS_CERRADO'),
)

#MINUSCULA PRODUCCIONES
#MAYUSCULAS TOKENS
def p_sigma (p):
    ''' sigma : ejecucion '''
    print("SIGMA")
    print("Termino", p)
    

def p_ejecucion (p):
    '''ejecucion : COMENTARIO_ENCABEZADO nombre bloque FIN_ACCION
                | nombre bloque FIN_ACCION 
    '''
    print('Prod. Ejecucion', p)







def p_nombre(p): 
    '''nombre : ACCION IDENTIFICADOR ES'''
    print('Prod. Nombre accion', p)

def p_comentario_vl_l (p):
    '''comentario_vl_l : COMENTARIO_VARIASLINEAS
                    | COMENTARIO_LINEA
    '''
    print('Prod Comentario VL L', p)

def p_bloque(p):
    '''bloque : ambiente proceso'''
    
def p_ambiente (p):
    '''ambiente : AMBIENTE bloque_ambiente
                | AMBIENTE comentario_vl_l bloque_ambiente
    '''
    print('Prod Ambiente', p)

def p_bloque_ambiente_scr (p):
    '''
        bloque_ambiente : variable comentario_vl_l
                    | constante comentario_vl_l
                    | comentario_vl_l
                    | variable
                    | constante
    '''
    print('Prod. Bloque ambiente_sr', p)

def p_bloque_ambiente_cc (p):
    ''' bloque_ambiente : variable comentario_vl_l bloque_ambiente
                    | constante comentario_vl_l bloque_ambiente
                    | comentario_vl_l bloque_ambiente
                    | variable bloque_ambiente
                    | constante bloque_ambiente 
    '''
    print('Prod. Bloque ambiente_cr', p)

def p_variable (p):
    '''variable : IDENTIFICADOR DOS_PUNTOS ftd_amb'''
    print('Prod. Variable', p)

def p_constante (p):
    '''constante : IDENTIFICADOR IGUAL tipo_dato'''
    print('Prod. Constante', p)

def p_ftd_amb (p): 
    '''ftd_amb : TD_ALFANUMERICO 
            | TD_NUMERICO
            | TD_LOGICO '''
    print('Prod. Tipo dato', p)

def p_tipo_dato (p):
    '''tipo_dato : CADENA 
                | NUMERICO
    '''

def p_proceso (p):
    '''
        proceso : PROCESO comentario_vl_l conj_sentencia
            | PROCESO conj_sentencia
    '''
    print('Prod. proceso', p)

#def p_conj_sentencia (p):
#    '''conj_sentencia : sentencia conj_sentencia
#                    | sentencia
#    '''
#
#def p_sentencia_asig (p):
#        '''sentencia : IDENTIFICADOR ASIGNACION tipo_dato
#                | IDENTIFICADOR ASIGNACION op_aritmetica
#        '''
#
#def p_sentencia_leer (p):
#    '''sentencia : LEER PARENTESIS_ABIERTO IDENTIFICADOR PARENTESIS_CERRADO'''
#
#def p_sentencia_escribir (p):
#    '''sentencia : ESCRIBIR PARENTESIS_ABIERTO salida_esc PARENTESIS_CERRADO'''
#
#def p_sentencia_si (p):
#    '''sentencia : SI PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO ENTONCES conj_s_si FIN_SI'''
#    
#def p_sentencia_mientras (p):
#    '''sentencia : MIENTRAS PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO HACER conj_sentencia FIN_MIENTRAS'''
#
#def p_sentencia_repetir (p):
#    '''sentencia : REPETIR conj_sentencia HASTA_QUE PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO'''
#
#def p_sentencia_para (p):
#    ''' sentencia : PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA id_tipodato HACER conj_sentencia FIN_PARA
#            | PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA HACER conj_sentencia FIN_PARA'''

def p_conj_sentencia (p):
    '''conj_sentencia : s_escribir conj_sentencia 
                    | s_escribir comentario_vl_l conj_sentencia
                    | s_leer conj_sentencia 
                    | s_leer comentario_vl_l conj_sentencia 
                    | s_si conj_sentencia 
                    | s_si comentario_vl_l conj_sentencia 
                    | s_segun conj_sentencia
                    | s_segun comentario_vl_l conj_sentencia
                    | s_ciclos conj_sentencia 
                    | s_ciclos comentario_vl_l conj_sentencia 
                    | sentencia conj_sentencia 
                    | sentencia comentario_vl_l conj_sentencia 
                    | comentario_vl_l conj_sentencia 
                    | s_escribir comentario_vl_l 
                    | s_leer comentario_vl_l 
                    | s_si comentario_vl_l
                    | s_segun comentario_vl_l
                    | s_ciclos comentario_vl_l 
                    | sentencia comentario_vl_l 
                    | s_escribir 
                    | s_leer 
                    | s_si 
                    | s_segun
                    | s_ciclos 
                    | sentencia 
                    | comentario_vl_l
    '''
    print('Prod. Conjunto de sentencias', p)


def p_s_escribir (p):
    '''s_escribir : ESCRIBIR PARENTESIS_ABIERTO salida_esc PARENTESIS_CERRADO'''
    print('Prod. escribir', p)
    
def p_salida_esc (p):
    '''salida_esc : IDENTIFICADOR 
                | CADENA 
                | IDENTIFICADOR COMA salida_esc 
                | CADENA COMA salida_esc'''
    print('Prod. salida_esc', p)
    
def p_s_leer (p):
    '''s_leer : LEER PARENTESIS_ABIERTO entrada_leer PARENTESIS_CERRADO'''
    print('Prod. leer', p)
    
def p_entrada_leer (p):
    '''entrada_leer : IDENTIFICADOR'''
    print('Prod. entrada_leer', p)
def p_sentencia (p):
    '''
        sentencia : IDENTIFICADOR ASIGNACION tipo_dato
                | IDENTIFICADOR ASIGNACION op_aritmetica
    '''
    print('Prod. sentencia', p)

def p_id_tipodato (p):
    '''
        id_tipodato : IDENTIFICADOR
                | tipo_dato
    '''
    print('Prod. tipo dato', p)
    
def p_op_aritmetica (p):
    '''
        op_aritmetica : id_tipodato t_op_aritmetico id_tipodato
                    | id_tipodato t_op_aritmetico
    '''
    print('Prod. opAritmetica', p)

def p_t_op_aritmetico (p):
    '''
        t_op_aritmetico : SUMA
                        | RESTA
                        | DIVISION
                        | MULTIPLICACION
                        | DIVISION_ENTERA
                        | MODULO
                        | POTENCIA
    '''
    print('Prod. t_op_aritmetico', p)
    
#def p_relacionales (p):
#    '''
#        relacionales : id_tipodato t_relacional id_tipodato
#                | id_tipodato t_relacional id_tipodato relacionales
#    '''
#    print('Prod. relacionales')
    
def p_t_relacional (p):
    '''
        t_relacional : MENOR_QUE
                    | MAYOR_QUE
                    | MENOR_O_IGUAL_QUE
                    | MAYOR_O_IGUAL_QUE
                    | IGUAL
                    | DISTINTO
    '''
    print('prod. t_relacional', p)
    
def p_t_op_logico (p):
    '''
        t_op_logico : O
                | Y
    '''
    print('Prod. op logico', p)

def p_s_si (p):
    '''s_si : SI PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO ENTONCES conj_s_si FIN_SI'''
    print('Prod. SI', p)
    
def p_conj_s_si (p):
    '''conj_s_si : conj_sentencia  
                | conj_sentencia SINO conj_s_si'''
    print('Prod. sentencias del SI', p)
    
def p_conj_condiciones (p):
    '''conj_condiciones : condicion 
                        | condicion t_op_logico conj_condiciones'''
    print('Prod. conj de condiciones', p)
    
def p_condicion (p):
    '''condicion : expresion t_relacional expresion 
                | NO expresion'''
    print('Prod. condicion', p)
    
def p_expresion (p):
    '''expresion : id_tipodato 
                | id_tipodato t_op_aritmetico id_tipodato 
                | id_tipodato t_op_aritmetico expresion'''
    print('Prod. expresion', p)
    
def p_s_segun (p):
    '''s_segun : SEGUN PARENTESIS_ABIERTO IDENTIFICADOR PARENTESIS_CERRADO HACER conj_cond_segun FIN_SEGUN'''
def p_conj_cond_segun (p):
    '''conj_cond_segun : t_relacional id_tipodato DOS_PUNTOS conj_sentencia 
                    | t_relacional id_tipodato DOS_PUNTOS conj_sentencia conj_cond_segun 
                    | OTRO DOS_PUNTOS conj_sentencia'''
    print('Prod. conj. cond. segun', p)
    
def p_s_ciclos (p):
    '''s_ciclos : c_para 
            | c_mientras 
            | c_repetir 
            | conj_sentencia'''
    print('Prod. de ciclos', p)



def p_c_mientras (p):
    '''
        c_mientras : MIENTRAS PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO HACER conj_sentencia FIN_MIENTRAS
    '''
    print('Prod. c_mientras', p)
   
def p_c_repetir (p):
    '''c_repetir : REPETIR conj_sentencia HASTA_QUE PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO'''
    print('Prod. Repetir', p)
def p_c_para (p):
    '''
        c_para : PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA id_tipodato HACER conj_sentencia FIN_PARA
            | PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA HACER conj_sentencia FIN_PARA 
    '''
    print('Prod. Para', p)
def p_idt_para (p):
    '''idt_para : IDENTIFICADOR ASIGNACION id_tipodato 
            | IDENTIFICADOR
    '''
    print('Prod. idt Para', p)

def p_error (p):
    print('Error parser', p)

#def p_empty(p):
#    '''
#        empty :
#    '''
#    # p[0] = None
#    print('Prod empty')
        
parser = yacc.yacc()
# print('Parser pseudocodigo.')
# while True:
#     try:
#         s = input('>> ')
#     except ValueError as e:
#         print(e)
#     except EOFError:
#         break
#     result = parser.parse(s)
#     print(result)


# VER DESPUÉS DE ARREGLAR ERRORES


if not pathFile:
    # Ejecución "normal"
    print('Parser Pseudocodigo | Grupo 15. SSL 2021.')
    print('Pasa salir pulse: [ctrl] + [C] | O escriba _salir')
    while True:
        s = input('>> ')
        if s == '_salir': break
    result = parser.parse(s)
    print(result)
        
else:
    # Ejecución "analisis de archivo de texto"
    try:
        file = open(pathFile,"r",encoding='utf8')
        strings = file.read()
        file.close()
        result = parser.parse(strings)
        print(result)
    except IOError:
        print('Ocurrió un error leyendo archivo:', pathFile)