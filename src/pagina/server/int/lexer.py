import ply.lex as lex   # lexer -> tokens
import re

contadorErrores = 0
arregloHtml = []

# Terminales
tokens = [
    'ACCION',
    'ES',
    'FIN_ACCION',
    'AMBIENTE',
    'CADENA',
    'NUMERICO',
    'PROCESO',
    'ESCRIBIR',
    'LEER',
    'O',
    'Y',
    'SI',
    'ENTONCES',
    'FIN_SI',
    'SINO',
    'NO',
    #
    'HACER',
    'SEGUN',
    'FIN_SEGUN',
    'MIENTRAS',
    'FIN_MIENTRAS',
    'OTRO',
    'REPETIR',
    'HASTA_QUE',
    'HASTA',
    'PARA',
    'FIN_PARA',
    #
    'SUMA',
    'RESTA',
    'DIVISION',
    'MULTIPLICACION',
    'DIVISION_ENTERA',
    'MODULO',
    'POTENCIA',
    'IGUAL',
    'MENOR_QUE',
    'MENOR_O_IGUAL_QUE',
    'MAYOR_QUE',
    'MAYOR_O_IGUAL_QUE',
    'DISTINTO',
    'IDENTIFICADOR',
    'DOS_PUNTOS',
    'ASIGNACION',
    'COMA',
    #comentarios abajo
    'COMENTARIO_ENCABEZADO',
    'COMENTARIO_VARIASLINEAS',
    'COMENTARIO_LINEA',
    #tipos de llaves
    'PARENTESIS_ABIERTO',
    'PARENTESIS_CERRADO',
    #tipos de datos
    'TD_NUMERICO',
    'TD_ALFANUMERICO',
    'TD_LOGICO'
]

# ply detecta variables que empiecen con 't_'
# Terminos: 
# w = letras o numeros
# s = todo lo que sea espacios.
# S = contrario a 's'.
# d = digitos.
# * = 0 o más.
# + = 1 o más.

def t_COMENTARIO_ENCABEZADO(t): 
    r'\/\*\*[\s\S]*?\*\/';
    if t.value.__contains__('\n'):
        t.lexer.lineno += t.value.count('\n')
        t.value= t.value.replace('\n', ' ')
    if t.value.__contains__('\t'):
        t.value= t.value.replace('\t', ' ')
    cambio= t.value.replace('/**', '')
    cambio= cambio.replace('*/','')
    arregloHtml.append(['encabezado', cambio])
    return t 

def t_COMENTARIO_VARIASLINEAS(t): 
    r'\/\*[\s\S]*?\*\/'; 
    if t.value.__contains__('\n'):
        t.lexer.lineno += t.value.count('\n')
        t.value= t.value.replace('\n', ' ')
    cambio= t.value.replace('/*', '')
    cambio= cambio.replace('*/','')
    arregloHtml.append(['bloque', cambio])
    return t 

def t_COMENTARIO_LINEA(t): 
    r'((\/\/|\@)(\s|\S)*?(.*))';
    if t.value.__contains__('\n'):
        t.lexer.lineno += t.value.count('\n')
        t.value= t.value.replace('\n', '')
    if t.value.__contains__('@'):
        cambio= t.value.replace('@', '')
    else:
        if t.value.__contains__('//'):
            cambio= t.value.replace('//','')
    arregloHtml.append(['linea', cambio])
    return t 

def t_ACCION(t): r'\b(?:acci[oó]n)\b'; return t 

def t_ES(t): r'\b(?:_es)\b'; return t 

def t_FIN_ACCION(t): r'\b(?:fin_acci[oó]n)\b'; return t 

def t_AMBIENTE(t): r'\b(?:ambiente)\b'; return t 

def t_PROCESO(t): r'\b(?:proceso)\b'; return t 

def t_ESCRIBIR(t): r'\b(?:escribir)\b'; return t 

def t_LEER(t): r'\b(?:leer)\b'; return t 

def t_PARENTESIS_ABIERTO(t): r'\('; return t 

def t_PARENTESIS_CERRADO(t): r'\)'; return t 

def t_ASIGNACION(t): r':='; return t 

def t_O(t): r'\b(?:_o)\b'; return t

def t_Y(t): r'\b(?:_y)\b'; return t

def t_SINO(t): r'\b(?:sino)\b'; return t

def t_FIN_SI(t): r'\b(?:fin_si)\b'; return t

def t_SI(t): r'\b(?:si)\b'; return t

def t_ENTONCES(t): r'\b(?:entonces)\b'; return t

def t_NO(t): r'\b(?:_no)\b'; return t

def t_HACER(t): r'\b(?:hacer)\b'; return t

def t_SEGUN(t): r'\b(?:segun)\b'; return t

def t_FIN_SEGUN(t): r'\b(?:fin_segun)\b'; return t

def t_MIENTRAS(t): r'\b(?:mientras)\b'; return t

def t_FIN_MIENTRAS(t): r'\b(?:fin_mientras)\b'; return t

def t_OTRO(t): r'\b(?:_otro)\b'; return t

def t_REPETIR(t): r'\b(?:repetir)\b'; return t

def t_HASTA_QUE(t): r'\b(?:hasta_que)\b'; return t

def t_PARA(t): r'\b(?:para)\b'; return t

def t_HASTA(t): r'\b(?:hasta)\b'; return t

def t_FIN_PARA(t): r'\b(?:fin_para)\b'; return t

def t_MENOR_O_IGUAL_QUE(t): r'<='; return t

def t_MAYOR_O_IGUAL_QUE(t): r'>='; return t

def t_DISTINTO(t): r'<>'; return t

def t_TD_NUMERICO(t): r'\b(?:num[eé]rico|n[uú]mero|entero|real)\b'; return t 

def t_TD_ALFANUMERICO(t): r'\b(?:cadena|alfanum[eé]rico)\b'; return t 

def t_TD_LOGICO(t): r'\b(?:l[oó]gico|booleano)\b'; return t

def t_MODULO(t): r'(_mod)'; return t

def t_DIVISION_ENTERA(t): r'(_div)'; return t

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_POTENCIA = r'\*\*'
t_DIVISION = r'\/'
t_IGUAL = r'\='
t_MENOR_QUE = r'\<'
t_MAYOR_QUE = r'\>'
t_DOS_PUNTOS = r'\:'
t_COMA= r'\,'

# ply ignorará espacios, saltos de lineas y tabs.
t_ignore = ' \t;'

def t_IDENTIFICADOR(t):
    r'[_a-zA-Z][_a-zA-Z0-9]*'
    t.type = 'IDENTIFICADOR'
    if not(t.value[0].__contains__('_')) and not(t.value[-1].__contains__('_')) and not(t.value.__contains__('__')) and not(t.value.__contains__('"')):
        return t
    else: 
        print(f'Identificador ilegal! : \'{t.value}\'.')
        global contadorErrores
        contadorErrores += 1

def t_error(t):
    global contadorErrores
    print(f'Caracter ilegal! : \'{t.value[0]}\'.')
    print(f'En linea: {t.lineno}. Posición: {t.lexpos}')
    contadorErrores += 1
    t.lexer.skip(1)

def t_CADENA(t):
    r'\\?"(?:[^"\\]|\\.)*"?'
    if not(t.value[-1] == '"') or (t.value[0] == '\\') or (t.value[-2] == '\\'):
        print(f'Cadena ilegal! : \'{t.value}\'.')
        global contadorErrores
        contadorErrores += 1
    else:
        t.value= t.value.replace('"', '')
        if t.value.__contains__('\\'):
            t.value = t.value.replace('\\', '"')
        if t.value.__contains__('\n'):
            t.value= t.value.replace('\n', ' ')
        if t.value.__contains__('\t'):
            t.value= t.value.replace('\t', ' ')
        return t

def t_NUMERICO(t): # acepta . o , como decimal.
    r'([\d]+(,|\.)[\d]+|[\d]+)'
    if t.value.__contains__(','):
        t.value= t.value.replace(",", ".")
        t.value = float(t.value)
    elif t.value.__contains__('.'):
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex(reflags=re.IGNORECASE) # Bandera para que ignore mayuscula/minuscula