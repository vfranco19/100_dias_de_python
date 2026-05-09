print("Bienvenido a la isla del tesoro")
print("Sigue la ruta y responde las opciones para encontrar el tesoro")

while True:
    primero = input("Frente a ti tienes dos caminos Derecha o Izquierda, cual eliges? \n (Escribre 'Derecha' o 'Izquierda'): ").lower()
    if primero in ["derecha", "izquierda"]:
        break
    
if primero == "derecha":
    print("Felicidades, la derecha siempre es la respuesta correcta, haz encontrado el mapa del tesoro, ahora sigue la ruta")
elif primero == "izquierda":
    print("La izquierda siempre lleva a la muerte, seguiras fallando mientras elijas a la izquierda, has caido en una trampa y has muerto, fin del juego")
    exit()
    
while True:
    segundo = input("Haz llegado a un lago, tienes dos opciones: Esperar en la orilla o Nadar a través del lago \n (Escribe 'Esperar' o 'Nadar'): ").lower()
    if segundo in ["esperar", "nadar"]:
        break

if segundo == "esperar":
    print("Has esperado pacientemente y un bote ha llegado, te has subido al bote y has cruzado el lago sin problemas")
elif segundo == "nadar":
    print("Has decidido nadar a través del lago, pero el agua es más profunda de lo que pensabas y te has ahogado, fin del juego")
    exit()

print("Felicitaciones, has encontrado el tesoro, eres un verdadero aventurero")