import ply.lex as lex   # lexer -> tokens
import re
import argparse

#Obtener path de texto por terminal
argParser = argparse.ArgumentParser(description='Procesa strings a tokens de pseudocodigo.')
argParser.add_argument('-f', '-pathFile', nargs='?',type=str, help='especificar ruta de archivo de texto de entrada a analizar.')
argsParser = argParser.parse_args()
pathFile = argsParser.f

contadorErrores = 0

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
    'SEMICOLON',
    #comentarios abajo
    'COMENTARIO_ENCABEZADO',
    'COMENTARIO_VARIASLINEAS',
    'COMENTARIO_LINEA',
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
        t.value= t.value.replace('\n', ' ')
    if t.value.__contains__('\t'):
        t.value= t.value.replace('\t', ' ')
    return t 

def t_COMENTARIO_VARIASLINEAS(t): 
    r'\/\*[\s\S]*?\*\/'; 
    if t.value.__contains__('\n'):
        t.value= t.value.replace('\n', ' ')
    return t 

def t_COMENTARIO_LINEA(t): 
    r'((\/\/|\@)(\s|\S)*?(.*))'; 
    if t.value.__contains__('\n'):
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

def t_TD_NUMERICO(t): r'(entero|numero|numerico|real)'; return t 

def t_TD_ALFANUMERICO(t): r'(cadena|alfanumerico)'; return t 

def t_TD_LOGICO(t): r'(logico|booleano)'; return t

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
t_SEMICOLON = r'\;'
t_COMA= r'\,'

# ply ignorará espacios, saltos de lineas y tabs.
t_ignore = ' \n\t'

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

lexer = lex.lex(reflags=re.IGNORECASE) # Bandera para que ignore mayuscula/minuscula

def analizarTokens(modoEjecucion):
    exportArray = []
    while True:
            tok = lexer.token()
            if not tok:
                if (modoEjecucion == 'archivo'):
                    exportarTokens(exportArray)
                break
            print(tok)
            if (modoEjecucion == 'archivo'):
                exportArray.append([tok.type,tok.value]);

# Exportar a un txt 
def exportarTokens(arrAnalizar):
    global contadorErrores
    with open('tokens-analizados.txt', 'w', encoding='UTF8') as f:
        f.write('TOKEN | VALOR\n')
        f.write('-------------\n')
        contador = 0
        for line in arrAnalizar:
            contador += 1
            f.write(f'{contador}- {line[0]}: {line[1]}')
            f.write('\n')
        f.write('-------------\n')
        f.write(f'Total de tokens válidos analizados: {contador}.\n')
        if (contadorErrores > 0):
            f.write(f'Total de tokens NO válidos: {contadorErrores}.')
    f.close()
    print('(!) Se exportó un .txt con los tokens analizados.')

if not pathFile:
    # Ejecución "normal"
    print('Pasa salir pulse: [ctrl] + [C] | O escriba _salir')
    while True:
        s = input('>> ')
        if s == '_salir': break
        lexer.input(s)
        analizarTokens('normal')
else:
    # Ejecución "analisis de archivo de texto"
    try:
        file = open(pathFile,"r",encoding='utf8')
        strings = file.read()
        file.close()
        lexer.input(strings)
        analizarTokens('archivo')
    except IOError:
        print('Ocurrió un error leyendo archivo:', pathFile)