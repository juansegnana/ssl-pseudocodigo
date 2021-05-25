import ply.lex as lex   # lexer -> tokens

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
    'IDENTIFICADOR'
]

# ply detecta variables que empiecen con 't_'   .
# def t_WHILE(t): r'while'; return t 
def t_ACCION(t): r'(accion|ACCION)'; return t 
#t_ACCION = r'accion'
def t_ES(t): r'(_es|_ES)'; return t 
#t_ES = r'_es'
def t_FIN_ACCION(t): r'(fin_accion|FIN_ACCION)'; return t 
#t_FIN_ACCION = r'fin_accion'
def t_AMBIENTE(t): r'(ambiente|AMBIENTE)'; return t 
#t_AMBIENTE = r'ambiente'

#t_NUMERICO = r''
def t_PROCESO(t): r'(proceso|PROCESO)'; return t 
#t_PROCESO = r'proceso'
def t_ESCRIBIR(t): r'(escribir|ESCRIBIR)'; return t 
#t_ESCRIBIR = r'escribir'
def t_LEE(t): r'(leer|LEER)'; return t 
#t_LEER = r'leer'
def t_PARENTESIS_ABIERTO(t): r'\('; return t 
#t_PARENTESIS_ABIERTO = r'\('
def t_PARENTESIS_CERRADO(t): r'\)'; return t 
#t_PARENTESIS_CERRADO = r'\)'

# t_O = r'_o'
def t_O(t): r'(_o|_O)'; return t
# t_Y = r'_y'
def t_Y(t): r'(_y|_Y)'; return t
# t_SI = r'si'
def t_SI(t): r'(si|SI)'; return t
# t_ENTONCES = r'entonces'
def t_ENTONCES(t): r'(entonces|ENTONCES)'; return t
# t_FIN_SI = r'fin_si'
def t_FIN_SI(t): r'(fin_si|FIN_SI)'; return t
def t_SINO(t): r'(sino|SINO)'; return t
# t_SINO = r'sino'
def t_NO(t): r'(_no|_NO)'; return t
# t_NO = r'_no'
def t_HACER(t): r'(hacer|HACER)'; return t
# t_HACER = r'hacer'
def t_SEGUN(t): r'(segun|SEGUN)'; return t
# t_SEGUN = r'segun'

##
def t_FIN_SEGUN(t): r'(fin_segun|FIN_SEGUN)'; return t
# t_FIN_SEGUN = r'fin_segun'
def t_MIENTRAS(t): r'(mientras|MIENTRAS)'; return t
# t_MIENTRAS = r'mientras'
def t_FIN_MIENTRAS(t): r'(fin_mientras|FIN_MIENTRAS)'; return t
# t_FIN_MIENTRAS = r'fin_mientras'
def t_OTRO(t): r'(_otro|_OTRO)'; return t
# t_OTRO = r'_otro'
def t_REPETIR(t): r'(repetir|REPETIR)'; return t
# t_REPETIR = r'repetir'
def t_HASTA_QUE(t): r'(hasta_que|HASTA_QUE)'; return t
# t_HASTA_QUE = r'hasta_que'
def t_PARA(t): r'(para|PARA)'; return t
# t_PARA = r'para'
def t_FIN_PARA(t): r'(fin_para|FIN_PARA)'; return t
# t_FIN_PARA = r'fin_para'
#def t_SUMA(t): r'\+'; return t
t_SUMA = r'\+'
#def t_RESTA(t): r'\-'; return t
t_RESTA = r'\-'
#def t_MULTIPLICACION(t): r'\*'; return t
t_MULTIPLICACION = r'\*'
#def t_DIVISION(t): r'\/'; return t
t_DIVISION = r'\/'
#def t_IGUAL(t): r'\='; return t
t_IGUAL = r'\='
#def t_MENOR_QUE(t): r'\<'; return t
t_MENOR_QUE = r'\<'
#def t_MAYOR_QUE(t): r'\>'; return t
t_MAYOR_QUE = r'\>'
def t_MENOR_O_IGUAL_QUE(t): r'<='; return t
# t_MENOR_O_IGUAL_QUE = r'<='
def t_MAYOR_O_IGUAL_QUE(t): r'>='; return t
# t_MAYOR_O_IGUAL_QUE = r'>='
def t_DISTINTO(t): r'<>'; return t
# t_DISTINTO = r'<>'
def COMENTARIO_ENCABEZADO(t): r''; return t 
def COMENTARIO_VARIASLINEAS(t): r''; return t 
#Probar
def COMENTARIO_LINEA(t): r'(\/ \/ [w]*\n)'; return t 
# ply ignorará espacios
t_ignore = r' '

# Terminos: 
# w = letras o numeros
# d = digitos.
# + = 1 o más.
# * = 0 o más.

# Como buscamos a los Terminales
def t_IDENTIFICADOR(t):
    r'(?!.*__.*)[A-Za-z][\w]*(?!_)\w'
    t.type = 'IDENTIFICADOR'
    return t

#def t_CADENA(t):
    r'".*"'
    t.value= t.value.replace('"', '')
    return t



def t_NUMERICO(t):
    r'([\d+]|[\d+\,\d+])+'
    if t.value.__contains__(','):
        t.value= t.value.replace(",", ".")
        t.value = float(t.value)
    else: 
        t.value = int(t.value)
    return t

def t_error(t):
    print('Caracter ilegal!')
    t.lexer.skip(1)




lexer = lex.lex()
s = input('>> ')
lexer.input(s)

## Leer txt
file = open("01-COMBINADO_InteracionesyCondicional2.txt","r")
strings = file.read();
file.close()
lexer.input(strings)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)