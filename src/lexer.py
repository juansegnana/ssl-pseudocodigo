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

# ply detecta variables que empiecen con 't_'.
t_ACCION = r'accion'
t_ES = r'_ES'
t_FIN_ACCION = r'fin_accion'
t_AMBIENTE = r'ambiente'
#t_CADENA = r''
#t_NUMERICO = r''
t_PROCESO = r'proceso'
t_ESCRIBIR = r'escribir'
t_LEER = r'leer'
t_PARENTESIS_ABIERTO = r'\('
t_PARENTESIS_CERRADO = r'\)'
t_O = r'_o'
t_Y = r'_y'
t_SI = r'si'
t_ENTONCES = r'entonces'
t_FIN_SI = r'fin_si'
t_SINO = r'sino'
t_NO = r'_no'
t_HACER = r'hacer'
t_SEGUN = r'segun'

##
t_FIN_SEGUN = r'fin_segun'
t_MIENTRAS = r'mientras'
t_FIN_MIENTRAS = r'fin_mientras'
t_OTRO = r'_otro'
t_REPETIR = r'repetir'
t_HASTA_QUE = r'hasta_que'
t_PARA = r'para'
t_FIN_PARA = r'fin_para'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_IGUAL = r'\='
t_MENOR_QUE = r'\<'
t_MAYOR_QUE = r'\>'
t_MENOR_O_IGUAL_QUE = r'<='
t_MAYOR_O_IGUAL_QUE = r'>='
t_DISTINTO = r'<>'


# ply ignorará espacios
t_ignore = r' '

# Terminos: 
# d = digits.
# + = 1 or more.
# * = 0 or more.
# Como buscamos a los Terminales


# Identificadores válidos:
# dato, dato_1, dato_1_a
# Identificadores no válidos:
# _dato, dato_, dato__1

#Fijarse como encontrar la expresion regular que sirva 
def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = 'ID'
    return t

def t_CADENA(t):
    r'.'
    return t
    

# No guarda valor completo.
def t_NUMERICO(t):
    r'[\d+]|[\d+\.\d+]'
    t.value = float(t.value)
    return t
#def t_NAME(t):
#    r'[a-zA-Z_][a-zA-Z_0-9]*' # can be a to Z or '_'
#    t.type = 'NAME'
#    return t

def t_error(t):
    print('Illegal character!')
    t.lexer.skip(1)

lexer = lex.lex()


s = input('>> ')

lexer.input(s)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)