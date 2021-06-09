/** Universidad Tecnologica Nacional
 Facultad Regional Resistencia
 Sintaxis y Semantica de los Lenguajes
 Ciclo:2021
 Autor:
 
Programa basico que imprime hola mundo
*/
ACCION HolaMundo _es

Ambiente 
 /* Definimos el ambiente
 variables que usamos
 */
	nombre_usuario : cadena

@ clasico algoritmo de Hola Mundo

Proceso
	escribir("Ingrese su nombre de usuario:") // Imprimir por pantalla
	leer(nombre_usuario) 		// Leer nombre usuario
	escribir("Hola Mundo") 	// Imprimir por pantalla
	escribir("Bienvenido al super lexer y parser del pseudocodigo", nombre_usuario)
	// Imprimir por pantalla
fin_accion 	// Fin de programa