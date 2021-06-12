/**
    Obtener porcentaje de un total X sobre una cantidad y
*/
ACCION porcentaje _ES
AMBIENTE
    total: real
    cantidad: numerico
    porcentaje: numerico
PROCESO
    escribir("Ingrese total")
    leer(total)
    escribir("Ingrese cantidad")
    leer(cantidad)

    porcentaje:= (cantidad*100)/porcentaje
    escribir("El porcentaje es de", porcentaAje, "%")

FIN_ACCION