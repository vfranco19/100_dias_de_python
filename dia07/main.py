cadena = ""
def derecha(ultimo):
    global cadena
    if ultimo ==
    cadena = cadena + ">"
def izquierda(ultimo):    
    global cadena
    cadena = cadena + "<"
def abajo(ultimo):
    global cadena
    cadena = cadena + "v"
def arriba(ultimo):
    global cadena
    cadena = cadena + "^"

ultimo = ""
while True:
    movimiento = input("Ingrese un movimiento (derecha, izquierda, abajo, arriba) o 'salir' para terminar: ")
    if movimiento == "salir":
        break
    elif movimiento == "derecha":
        derecha(ultimo)
    elif movimiento == "izquierda":
        izquierda(ultimo)
    elif movimiento == "abajo":
        abajo(ultimo)
    elif movimiento == "arriba":
        arriba(ultimo)
    else:
        print("Movimiento no válido. Intente nuevamente.")
print("Secuencia de movimientos:", cadena)