import { useEffect, useRef, useState } from 'react';
import { saveAs } from 'file-saver'; // Para descargar resultados
import './App.css';                 // Estilos visuales
import AceEditor from 'react-ace'; // Editor de código

function App() {

  const baseUrl = 'http://127.0.0.1:5000/pseudo?data='

  // Guarda archivo actual.
  const [selectedFile, setSelectedFile] = useState()

  // Se seleccionó un archivo? "Booleano".
  const [isFileSelected, setIsFileSelected] = useState(false)

  // Texto extraído del archivo o escrito en editor. "String"
  const [textReaded, setTextReaded] = useState('');

  // Resultados del server. "Object": resultado, lineaError, html, analisis
  const [results, setResults] = useState(null);

  // Se envía y espera respuesta del servidor. "Booleano"
  const [sending, setSending] = useState(false);

  /**
   * 
   * @param {String} descarga Elige qué resultado descargar. 'html' o 'analisis'.
   */
  const exportResults = (descarga) => {
    
    const { html, analisis } = results;
    // Unir arreglo en un solo string. Luego exportar a archivo.
    const textHtml = html.join('');
    const textAnalisis = analisis.join('');

    if (descarga === 'html') {
      const blob = new Blob([textHtml], {type: "text/plain;charset=utf-8"});
      saveAs(blob, "export.html");

    } else {
      const blob = new Blob([textAnalisis], {type: "text/plain;charset=utf-8"});
      saveAs(blob, "analisis.txt");
    }

  }

  /**
   * Envia petición con pseudocódigo. Lo que devuelve se carga a "results"
   * @returns Si NO hay texto, sale de función. Sino manda a servidor.
   */
  const handleRead = async () => {

    setSending(true);
    // Enviar petición solo si hay texto o se cargó un archivo
    if (!isFileSelected && !textReaded) {
      setSending(false)
      return;
    }

    const sendToApi = () => {
      // Enviar petición a servidor.
      fetch(baseUrl+ encodeURIComponent(textReaded))
      .then((resp) => {
        resp.json().then(({result, errline, html, analisis}) => {

          if (errline !== 0) {
            inputEl.current.editor.gotoLine(errline) // Enviar a linea erronea
          }
          setResults({result: result, errline: errline, html: html, analisis: analisis})
          setSending(false)

        })
      })
      .catch(data => {
        console.log('Error!', data)
        setSending(false)
      })
    }

    sendToApi();

  }

  // Apunta al editor de codigo,
  // se usa para luego remarcar la línea de código
  // donde haya error.
  const inputEl = useRef(null);

  // Cada vez que se carga un archivo
  // se debe leer y colocar como "texto actual"
  // Agregandolo en el editor.
  useEffect(() => {

    function readFileAsync(file) {
      return new Promise((resolve, reject) => {
        let reader = new FileReader();
    
        reader.onload = () => {
          resolve(reader.result);
        };
        reader.onerror = reject;
        reader.readAsText(file);
      })
    }
    const newFile = async() => {
      try {
        const file = await readFileAsync(selectedFile)
        setTextReaded(file);
      } catch (err) {
        console.log('Error leyendo:', err);
      }
    }
    selectedFile && newFile()
  
  }, [isFileSelected, selectedFile])

  /**
   * Cuando se selecciona nuevo archivo se debe modificar el "selectedFile".
   * @param {Object} e Objeto donde esté el archivo seleccionado
   * @returns true|false
   */
  const handleFile = async(e) => {
    // Si no se seleccionó nada:
    if (e.target.files.length < 1) {
      return setIsFileSelected(false);
    }
    setSelectedFile(e.target.files[0])
    setIsFileSelected(true);
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Intérprete de Pseudocódigo</h1>
        <p>SSL 2021. Grupo 15.</p>
        <div className="main_container">

          <div>
            <p>Seleccione su archivo:</p>
            <input
              type="file"
              accept=".txt,.e"
              onChange={handleFile}
            />
            <br />
            <button onClick={handleRead} disabled={sending}>Enviar</button>
          </div>
          {/* Esta sección solo aparece si existen resultados obtenidos */}
          <div>
            {results && (
              <div>
                <h1>Resultados</h1>
                {(results.result) ? (<h2 className="bien">Correcto</h2>) : <h2 className="mal">Incorrecto</h2>}
                {(!results.result) && <p>Error en línea: {results.errline}</p>}
                <button onClick={()=> exportResults('html')}>Descargar HTML</button>
                <button onClick={()=> exportResults('analisis')}>Descargar Análisis</button>
              </div>
            )}
          </div>
          {/* Fin sección Resultados */}
        </div>
        <div className="editor">
          {/* AceEditor --> Editor de código. */}
          <h2>Editor</h2>
          <AceEditor
            ref={inputEl}
            style={{
              height: '500px',
              width: '80%',
            }}
            placeholder='Start Coding'
            mode="python"
            fontSize={18}
            showPrintMargin={true}
            showGutter={true}
            highlightActiveLine={true}
            onChange={code => setTextReaded(code)}
            value={textReaded}
          />
        </div>

      </header>
    </div>
  );
}

export default App;
