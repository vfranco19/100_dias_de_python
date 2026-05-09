import random
print("Bienvenido al juego de piedra, papel o tijera")
while True:
    usuario = int(input("Elija una opción (1 => Piedra, 2 => Papel, 3 => Tijeras): "))
    if usuario in [1, 2, 3]:
        break
    else:
        print("Opción inválida. Por favor, elija 1, 2 o 3.")
computadora = random.randint(1, 3)
opciones = {1: "Piedra", 2: "Papel", 3: "Tijeras"}
print(f"Usuario eligió: {opciones[usuario]}")
print(f"Computadora eligió: {opciones[computadora]}")
if usuario == computadora:
    print("Empate")
elif (usuario == 1 and computadora == 3) or (usuario == 2 and computadora == 1) or (usuario == 3 and computadora == 2):
    print("¡Ganaste!")
else:    
    print("¡Perdiste!")
