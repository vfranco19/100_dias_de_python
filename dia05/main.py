import random
print("Bienvenido al generador de contraseñas")
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "="]
while True:
    cant_letras = int(input("¿Cuántas letras quieres en tu contraseña? "))
    cant_numeros = int(input("¿Cuántos números quieres en tu contraseña? "))
    cant_simbolos = int(input("¿Cuántos símbolos quieres en tu contraseña? "))
    if cant_letras >= 0 and cant_numeros >= 0 and cant_simbolos >= 0:
        break
    else:        
        print("Por favor, ingresa datos válidos.")

contraseña = []
for _ in range(cant_letras):
    pos = random.randint(0, len(letras) - 1)
    contraseña.append(letras[pos])
for _ in range(cant_numeros):
    pos = random.randint(0, len(numeros) - 1)
    contraseña.append(numeros[pos])
for _ in range(cant_simbolos):
    pos = random.randint(0, len(simbolos) - 1)
    contraseña.append(simbolos[pos])
random.shuffle(contraseña)
print("Tu contraseña generada es: " + "".join(contraseña))
if len(contraseña) <= 6:
    print("Tu contraseña es débil. Considera agregar más caracteres.")
elif len(contraseña) > 6 and len(contraseña) <= 8:
    print("Tu contraseña es moderada. Considera agregar más caracteres para mayor seguridad.")
else:
    print("Tu contraseña es fuerte. ¡Buen trabajo!")
