import ply.yacc as yacc # parser 
from lexer import tokens
import argparse

#Obtener path de texto por terminal
argParser = argparse.ArgumentParser(description='Procesa tokens de pseudocodigo.')
argParser.add_argument('-f', '-pathFile', nargs='?',type=str, help='especificar ruta de archivo de texto de entrada a analizar.')
argsParser = argParser.parse_args()
pathFile = argsParser.f

def p_sigma (p):
    ''' sigma : COMENTARIO_ENCABEZADO ACCION IDENTIFICADOR ES ambiente FIN_ACCION
            | ACCION IDENTIFICADOR ES ambiente FIN_ACCION '''
    print("SIGMA")
    print("Termino")
    
def p_comentario_vl_l (p):
    '''comentario_vl_l : COMENTARIO_VARIASLINEAS
                    | COMENTARIO_LINEA'''
    print('Prod Comanterio VL L')

def p_ambiente (p):
    '''ambiente : AMBIENTE bloque_ambiente proceso 
                | AMBIENTE comentario_vl_l bloque_ambiente proceso'''
    print('Prod Ambiente')

def p_bloque_ambiente (p):
    '''
        bloque_ambiente : variable_comentario_vl_l
                    | constante comentario_vl_l
                    | variable comentario_vl_l bloque ambiente
                    | constante comentario_vl_l bloque_ambiente
                    | comentario_vl_l
                    | comentario_vl_l bloque ambiente
                    | variable bloque_ambiente
                    | constante bloque_ambiente
                    | variable
                    | constante
    '''
    print('Prod. Bloque ambiente')

def p_variable (p):
    '''variable : IDENTIFICADOR DOS_PUNTOS ftd_amb'''
    print('Prod. Variable')

def p_constante (p):
    '''constante : IDENTIFICADOR IGUAL tipo_dato'''
    print('Prod. Constante')

#def p_identificador (p): 
#    '''identificador : IDENTIFICADOR'''
#    print('Prod. Identificador')




def p_ftd_amb (p): 
    '''ftd_amb : TD_ALFANUMERICO 
                 | TD_NUMERICO
                 | TD_LOGICO '''
    print('Prod. Tipo dato')

def p_tipo_dato (p):
    '''tipo_dato : '''






def p_proceso (p):
    '''
        proceso : PROCESO comentario_vl_l conj_sentencia
            | PROCESO conj_sentencia
    '''
    print('Prod. proceso')

def p_conj_sentencia (p):
    '''conj_sentencia : s_escribir conj_sentencia 
                    | s_escribir comentario_vl_l conj_sentencia
                    | s_leer conj_sentencia 
                    | s_leer comentario_vl_l conj_sentencia 
                    | s_si conj_sentencia 
                    | s_si comentario_vl_l conj_sentencia 
                    | s_ciclos conj_sentencia 
                    | s_ciclos comentario_vl_l conj_sentencia 
                    | sentencia conj_sentencia 
                    | sentencia comentario_vl_l conj_sentencia 
                    | comentario_vl_l conj_sentencia 
                    | s_escribir comentario_vl_l 
                    | s_leer comentario_vl_l 
                    | s_si comentario_vl_l
                    | s_ciclos comentario_vl_l 
                    | sentencia comentario_vl_l 
                    | s_escribir 
                    | s_leer 
                    | s_si 
                    | s_ciclos 
                    | sentencia 
                    | comentario_vl_l'''
    print('Prod. Conjunto de sentencias')

def p_s_escribir (p):
    '''s_escribir : ESCRIBIR PARENTESIS_ABIERTO salida_esc PARENTESIS_CERRADO'''
    print('Prod. escribir')
    
def p_salida_esc (p):
    '''salida_esc : IDENTIFICADOR 
                | CADENA 
                | IDENTIFICADOR COMA salida_esc 
                | CADENA COMA salida_esc'''
    print('Prod. salida_esc')
    
def p_s_leer (p):
    '''s_leer : LEER PARENTESIS_ABIERTO entrada_leer PARENTESIS_CERRADO'''
    print('Prod. leer')
    
def p_entrada_leer (p):
    '''entrada_leer : IDENTIFICADOR'''
    print('Prod. entrada_leer')

def p_sentencia (p):
    '''
        sentencia : IDENTIFICADOR ASIGNACION tipo_dato
                | IDENTIFICADOR ASIGNACION op_aritmetica
    '''
    print('Prod. sentencia')

def p_id_tipodato (p):
    '''
        id_tipodato : IDENTIFICADOR
                | tipo_dato
    '''
    print('Prod. tipo dato')

def p_conj_operaciones (p):
    '''
        conj_operaciones : op_aritmetica
                        | relacionales
    '''
    print('Prod. conj. operaciones')
    
def p_op_aritmetica (p):
    '''
        op_aritmetica : id_tipodato t_op_aritmetico id_tipodato
                    | id_tipodato t_op_aritmetico
    '''
    print('Prod. opAritmetica')

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
    print('Prod. t_op_aritmetico')
    
def p_relacionales (p):
    '''
        relacionales : id_tipodato t_relacional id_tipodato
                | id_tipodato t_relacional id_tipodato relacionales
    '''
    print('Prod. relacionales')
    
def p_t_relacional (p):
    '''
        t_relacional : MENOR_QUE
                    | MAYOR_QUE
                    | MENOR_O_IGUAL_QUE
                    | MAYOR_O_IGUAL_QUE
                    | IGUAL
                    | DISTINTO
    '''
    print('prod. t_relacional')
    
def p_op_logico (p):
    '''
        op_logico : O
                | Y
    '''
    print('Prod. op logico')

def p_s_si (p):
    '''s_si : SI PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO ENTONCES conj_s_si FIN_SI'''
    print('Prod. SI')
    
def p_conj_s_si (p):
    '''conj_s_si : conj_sentencia  
                | conj_sentencia SINO conj_s_si'''
    print('Prod. sentencias del SI')
    
def p_conj_condiciones (p):
    '''conj_condiciones : condicion 
                        | condicion t_op_logico conj_condiciones'''
    print('Prod. conj de condiciones')
    
def p_condicion (p):
    '''condicion : expresion t_relacional expresion 
                | NO expresion'''
    print('Prod. condicion')
    
def p_expresion (p):
    '''expresion : id_tipodato 
                | id_tipodato t_op_aritmetico id_tipodato 
                | id_tipodato t_op_aritmetico expresion'''
    print('Prod. expresion')
    
def p_s_segun (p):
    '''s_segun : SEGUN PARENTESIS_ABIERTO IDENTIFICADOR PARENTESIS_CERRADO HACER conj_cond_segun FIN_SEGUN'''
def p_conj_cond_segun (p):
    '''conj_cond_segun : t_relacional id_tipodato DOS_PUNTOS conj_sentencia 
                    | t_relacional id_tipodato DOS_PUNTOS conj_sentencia conj_cond_segun 
                    | OTRO DOS_PUNTOS conj_sentencia'''
    print('Prod. conj. cond. segun')

def p_s_ciclo (p):
    '''s_ciclo : c_para 
            | c_mientras 
            | c_repetir 
            | conj_sentencia'''
    print('Prod. de ciclos')




def p_c_mientras (p):
    '''
        c_mientras : MIENTRAS PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO HACER conj_sentencia FIN_MIENTRAS
    '''
    print('Prod. c_mientras')
    
def p_c_repetir (p):
    '''c_repetir : REPETIR conj_sentencia HASTA_QUE PARENTESIS_ABIERTO conj_condiciones PARENTESIS_CERRADO'''
    print('Prod. Repetir')
def p_para (p):
    '''
        para : PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA id_tipodato HACER conj_sentencia FIN_PARA
            | PARA PARENTESIS_ABIERTO idt_para PARENTESIS_CERRADO HASTA id_tipodato COMA HACER conj_sentencia FIN_PARA 
    '''
    print('Prod. Para')
def p_idt_para (p):
    '''idt_para : IDENTIFICADOR ASIGNACION id_tipodato 
            | IDENTIFICADOR
    '''
    print('Prod. idt Para')

def p_error (p):
    print('Error parser', p)

def p_empty(p):
    '''
        empty :
    '''
    # p[0] = None
    print('Prod empty')
        
parser = yacc.yacc()
print('Parser pseudocodigo.')
while True:
    try:
        s = input('>> ')
    except ValueError as e:
        print(e)
    except EOFError:
        break
    result = parser.parse(s)
    print(result)


# VER DESPUÉS DE ARREGLAR ERRORES
# def analizarTokens():
#     while True:
#         tok = parser.parse()
#         if not tok:
#             break
#         print(tok)

# if not pathFile:
#     # Ejecución "normal"
#     print('Parser Pseudocodigo | Grupo 15. SSL 2021.')
#     print('Pasa salir pulse: [ctrl] + [C] | O escriba _salir')
#     while True:
#         s = input('>> ')
#         if s == '_salir': break
#         # lexer.input(s)
#         analizarTokens()
# else:
#     # Ejecución "analisis de archivo de texto"
#     try:
#         file = open(pathFile,"r",encoding='utf8')
#         strings = file.read()
#         file.close()
#         # lexer.input(strings)
#         analizarTokens()
#     except IOError:
#         print('Ocurrió un error leyendo archivo:', pathFile)