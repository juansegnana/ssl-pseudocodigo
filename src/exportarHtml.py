# $ Nombre de archivo: igual al archivo fuente con extensión HTM o HTML.
# $ Comentarios de Inicio: encerrados entre tags <H2> y negrita.
# $ Comentarios de bloque: encerrados entre tags <H4>
# $ Comentarios de linea: párrafo común .<p>
# k530 / shrapnel
#from parser import arregloHtml
# 
# <!DOCTYPE html>
# <html>
#   <head>
#     <meta charset="utf-8">
#     <title>TITULO TXT</title>
#   </head>
#   <body>
#       <h2>ENCABEZADO</h2>
#       <h4>Comentario bloque</h4>
#       <p>Comentario Linea</p>
#   </body>
# </html>

arrayHtml = [
"""<!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title> </title>
        </head>
        <body>
    """
]

## Viene del lexer o parser
importado = [
    {
        'tipo': 'encabezado',
        'valor': 'hola'
    }
]
#diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

def exportarHtml (importado):
    for line in importado:
        if line.tipo == 'encabezado':
            arrayHtml.append(f'<h2>{line.valor}</h2>')
        if line.tipo == 'linea':
            arrayHtml.append(f'<p>{line.valor}</p>')
        if line.tipo == 'bloque':
            arrayHtml.append(f'<h4>{line.valor}</h4>')
        