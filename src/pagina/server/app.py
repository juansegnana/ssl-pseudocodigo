from importlib import reload              # Recargar un modulo
from flask import Flask, jsonify, request # Crea servidor
from flask_cors import CORS               # Habilita peticiones

import int.parser as parser

app = Flask(__name__)

CORS(app)
# Cuando alguien hace link/pseudo, hacer:
@app.route('/pseudo', methods=['GET'])
def getInfo():
    # link/pseudo?data=texto_pseudocodigo
    texto = request.args.get('data')
    print('texto recibido:', texto)
    if texto:
        # analiza con parser y devuelve:
        # True/False | Linea Error | Html | Analisis del Parser
        resultado = parser.analizarApi(texto)
        print('resultado:', resultado)
        reload(parser)
        return jsonify({'result': resultado['result'], 'errline':resultado['errline'],
            'html':resultado['html'], 'analisis': resultado['analisis']
        })
    else:
        return 'vacio', 400