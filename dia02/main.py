print("Bienvenido a la calculadora de propinas")
total_cuenta = float(input("Cual es el valor total de la cuenta? \n"))
porcentaje_propina = int(input("Cual es el porcetaje de propina que desear dar? \n"))
num_personas = int(input("Entre cuantas personas se dividirá la cuenta? \n"))
total_propina = (total_cuenta * porcentaje_propina) / 100
total_con_propina = total_cuenta + total_propina
propina_por_persona = total_propina / num_personas
print(f"El total de la propina es: {total_propina:.2f}")
print(f"Cada persona debe pagar de propina: {propina_por_persona:.2f}")
print(f"Cada persona debe pagar: {total_con_propina / num_personas:.2f}")
print(f"El total de la cuenta con propina es: {total_con_propina:.2f}")