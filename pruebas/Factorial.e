/** Universidad Tecnologica Nacional
 Facultad Regional Resistencia
 Sintaxis y Semantica de los Lenguajes
 Ciclo:2021
 Autor:
 
Programa basico que calcula el factorial de un numero ingresado
Ademas la parte de comentario incluye caracteres ….
*/
ACCION factorial _es
Ambiente
res_factorial : entero
nro_calculo : entero
/* calcula el factorial de un numero,
pide ingresar un numero
y calcula cual es su factorial
finaliza imprimiendo el resultado
#*/
Proceso 
	escribir("Ingrese numero a calcular su factorial:")
	leer(nro_calculo);
	res_factorial := 1;
	mientras (nro_calculo <> 0) hacer;
		res_factorial := res_factorial * nro_calculo;
		nro_calculo := nro_calculo - 1;
	fin_mientras
	escribir("El factorial del numero ingresado es :", res_factorial);
fin_accion // ACA termina el programa. ;)