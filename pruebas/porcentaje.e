/**
    Obtener porcentaje de un total X sobre una cantidad y
*/
ACCION porcentaje _ES
AMBIENTE
    total: numerico
    cantidad: numerico
    porcentaje: numerico
PROCESO
    escribir("Ingrese total")
    leer(total)
    escribir("Ingrese cantidad")
    leer(cantidad)

    porcentaje:= (cantidad*100)/porcentaje
    escribir("El porcentaje es de", porcentaje, "%")

FIN_ACCION