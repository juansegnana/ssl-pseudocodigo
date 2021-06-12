/**     Universidad Tecnologica Nacional
        Facultad Regional Resistencia
        Sintaxis y Semantica de los Lenguajes
        Ciclo:2021
    	Autor:

Programa basico que combina iteraciones y condicionales
*/

ACCION combinado2 _ES

AMBIENTE
/*
Declaramos algunas variables
no hay control de uso de las variables 
*/
nombre_usuario : CADENA;
	var1 : ENTERO;
var2 : REAL;
VAR_4: ENTERO;
A: ENTERO;
B: ENTERO;
C: ENTERO;

PROCESO

ESCRIBIR("Ingrese un numero");
LEER(var2);
var1 := 4;

MIENTRAS (contador <> 0) HACER                          @ Abrimos Miestras
	ESCRIBIR("=numero + * & ingresado es:",var2);
	

	SI ((var2+var1)>B _y (var2+var1)=10 _y var2 > 10.2) ENTONCES   //Abrimos condicional SI
		VAR_4 := var1 + var2;
		ESCRIBIR("El resultado es:", VAR_4);
		
		SINO SI (var2=var1) ENTONCES                                     // SINO SI
			ESCRIBIR("var1 es igual a var2");
			SINO SI (hey>B _y (A+B)<C _o var1 < B) ENTONCES                    //otro SINO SI
				ESCRIBIR("var1 es = a B");
			FIN_SI                                                           //Fin SI
		FIN_SI                                                           // Fin SI
	FIN_SI                                                         // Fin SI
	contador:= contador+1;
FIN_MIENTRAS                                            @ cerramos MIENTRAS

PARA A HASTA B HACER                                    @ Abrimos iteraciones PARA
	A:= A+1;
	ESCRIBIR("A vale ", A);
	REPETIR                                                @Abrimos iteraciones REPETIR
		var1:=var1*A;
		ESCRIBIR("var1 vale:", var1);
	HASTA_QUE (A=B)                                        @ Cierra REPETIR
FIN_PARA                                                @ Cierra PARA

FIN_ACCION
