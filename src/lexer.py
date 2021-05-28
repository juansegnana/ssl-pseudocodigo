import ply.lex as lex   # lexer -> tokens
import argparse
# Obtener path de texto por terminal
argParser = argparse.ArgumentParser(description='Procesa strings a tokens de pseudocodigo.')
argParser.add_argument('-f', '-pathFile', nargs='?',type=str, help='especificar ruta de archivo de texto de entrada a analizar.')
argsParser = argParser.parse_args()
pathFile = argsParser.f

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
    'PARENTESIS_ABIERTO',
    'PARENTESIS_CERRADO',
    'O',
    'Y',
    'SI',
    'ENTONCES',
    'FIN_SI',
    'SINO',
    'NO',
    'HACER',
    'SEGUN',
    #
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
    'SEMICOLON',
    #comentarios abajo
    'COMENTARIO_ENCABEZADO',
    'COMENTARIO_VARIASLINEAS',
    'COMENTARIO_LINEA'
]

# ply detecta variables que empiecen con 't_'   .

def t_COMENTARIO_ENCABEZADO(t): 
    r'\/\*\*[\s\S]*?\*\/';
    if t.value.__contains__('\n'):
        t.lexer.lineno += 1
        t.value= t.value.replace('\n', ' ')
    if t.value.__contains__('\t'):
        t.value= t.value.replace('\t', ' ')
    #formatear
    return t 

def t_COMENTARIO_VARIASLINEAS(t): 
    r'\/\*[\s\S]*?\*\/'; 
    if t.value.__contains__('\n'):
        t.lexer.lineno += 1
        t.value= t.value.replace('\n', ' ')
    #formatear
    return t 

def t_COMENTARIO_LINEA(t): 
    r'((\/\/|\@)(\s|\S)*?\n)'; 
    if t.value.__contains__('\n'):
        t.lexer.lineno += 1
        t.value= t.value.replace('\n', '')
    return t 

def t_ACCION(t): r'(accion|ACCION)'; return t 

def t_ES(t): r'(_es|_ES)'; return t 

def t_FIN_ACCION(t): r'(fin_accion|FIN_ACCION)'; return t 

def t_AMBIENTE(t): r'(ambiente|AMBIENTE)'; return t 

def t_PROCESO(t): r'(proceso|PROCESO)'; return t 

def t_ESCRIBIR(t): r'(escribir|ESCRIBIR)'; return t 

def t_LEER(t): r'(leer|LEER)'; return t 

def t_PARENTESIS_ABIERTO(t): r'\('; return t 

def t_PARENTESIS_CERRADO(t): r'\)'; return t 

def t_ASIGNACION(t): r':='; return t 

def t_O(t): r'(_o|_O)'; return t

def t_Y(t): r'(_y|_Y)'; return t

def t_SINO(t): r'(sino|SINO)'; return t

def t_FIN_SI(t): r'(fin_si|FIN_SI)'; return t

def t_SI(t): r'(si|SI)'; return t

def t_ENTONCES(t): r'(entonces|ENTONCES)'; return t

def t_NO(t): r'(_no|_NO)'; return t

def t_HACER(t): r'(hacer|HACER)'; return t

def t_SEGUN(t): r'(segun|SEGUN)'; return t

def t_FIN_SEGUN(t): r'(fin_segun|FIN_SEGUN)'; return t

def t_MIENTRAS(t): r'(mientras|MIENTRAS)'; return t

def t_FIN_MIENTRAS(t): r'(fin_mientras|FIN_MIENTRAS)'; return t

def t_OTRO(t): r'(_otro|_OTRO)'; return t

def t_REPETIR(t): r'(repetir|REPETIR)'; return t

def t_HASTA_QUE(t): r'(hasta_que|HASTA_QUE)'; return t

def t_PARA(t): r'(para|PARA)'; return t

def t_HASTA(t): r'(hasta|HASTA)'; return t

def t_FIN_PARA(t): r'(fin_para|FIN_PARA)'; return t

def t_MENOR_O_IGUAL_QUE(t): r'<='; return t

def t_MAYOR_O_IGUAL_QUE(t): r'>='; return t

def t_DISTINTO(t): r'<>'; return t

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_IGUAL = r'\='
t_MENOR_QUE = r'\<'
t_MAYOR_QUE = r'\>'
t_DOS_PUNTOS = r'\:'
t_SEMICOLON = r'\;'
t_COMA= r'\,'

# ply ignorará espacios
t_ignore = ' \t'

# Terminos: 
# w = letras o numeros
# d = digitos.
# + = 1 o más.
# * = 0 o más.

# Como buscamos a los Terminales
def t_IDENTIFICADOR(t):
    r'[a-zA-Z]+(?!.*__.*)(?!.*_(\s|[\n\r]|$))\w*'
    t.type = 'IDENTIFICADOR'
    return t

def t_CADENA(t):
    r'".*"'
    t.value= t.value.replace('"', '')
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

def t_new_line(t):
    r'\n'
    t.lexer.lineno += 1

def t_error(t):
    print(f'Caracter ilegal! : \'{t.value[0]}\'.')
    print(f'En linea: {t.lineno}. Posición: {t.lexpos}')
    t.lexer.skip(1)

lexer = lex.lex()

if not pathFile:
    print('Pasa salir escriba: _salir')
    while True:
        s = input('>> ')
        if s == '_salir': break

        lexer.input(s)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok)
else:
    # Leer txt
    file = open(pathFile,"r")
    strings = file.read()
    file.close()
    lexer.input(strings)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

