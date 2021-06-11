
accion CICLOS _es
    ambiente
        a_1 : cadena // a_1 será el nombre
        a_2 : entero // a_2 será la edad
    proceso
        repetir
            escribir("escribir nombre")
            leer(a_1)
            escribir("su nombre es...", a_1)
            escribir("escribir edad")
            leer(a_2)
        hasta_que(a_1 = "salir") // repetira hasta que escriba "salir"
fin_accion