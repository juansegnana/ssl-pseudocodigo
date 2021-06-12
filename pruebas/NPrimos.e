/** Universidad Tecnologica Nacional
 Facultad Regional Resistencia
 Sintaxis y Semántica de los Lenguajes
 Ciclo:2021
 Autor:
 
Programa que calcula si un numero ingresado es un numero primos . 
*/
ACCION NumerosPrimos _es
Ambiente
// hey
nro_ingresado : numerico 
bool : numero
aux : numero
Proceso 
	escribir("ingresé número entero para saber si es número primo:");
	leer (nro_ingresado);
	para (aux := 2) hasta nro_ingresado, 1 hacer;
		modulo := 2;
		bool := 1;
		mientras (bool = 1 _y modulo < aux) hacer ;
			si (aux _mod modulo =0) entonces;
				bool := 0;
			sino;
				modulo := modulo + 1;
			fin_si;
		fin_mientras;
		si (bool = 1) entonces;
			escribir ("el numero es primo", aux);
		fin_si;
	fin_para
fin_accion @fin programa