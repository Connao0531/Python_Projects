print("Calculadora con una sola variable\n")

print("********************")
print("* Menú de opciones *")
print("********************")

print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. División entera\n6. Exponente\n7. Modulo o resto\n")

numero = int(input("Eliga la opción deseada: "))

if numero == 1:

    print("Elegiste suma")

    numero = int(input("\nIntroduce el primer numero: "))

    numero += int(input("Introduce el segundo numero: "))

    print("El resultado de la suma es: ", numero)

elif numero == 2:

    print("Elegiste resta")

    numero = int(input("\nIntroduce el primer numero: "))

    numero -= int(input("Introduce el segundo numero: "))

    print("El resultado de la resta es: ", numero)

elif numero == 3:

    print("Elegiste multiplicación")

    numero = int(input("\nIntroduce el primer numero: "))

    numero *= int(input("Introduce el segundo numero: "))

    print("El resultado de la multiplicación es: ", numero)

elif numero == 4:

    print("Elegiste división")

    numero = float(input("\nIntroduce el primer numero: "))

    numero /= float(input("Introduce el segundo numero: "))

    print("El resultado de la división es: ", round(numero, 2))

elif numero == 5:

    print("Elegiste división entera")

    numero = int(input("\nIntroduce el primer numero: "))

    numero //= int(input("Introduce el segundo numero: "))

    print("El resultado de la división entera es: ", numero)

elif numero == 6:

    print("Elegiste exponente")

    numero = int(input("\nIntroduce el primer numero: "))

    numero **= int(input("Introduce el segundo numero: "))

    print("El resultado del exponente es: ", numero)

elif numero == 7:

    print("Elegiste división entera")

    numero = int(input("\nIntroduce el primer numero: "))

    numero %= int(input("Introduce el segundo numero: "))

    print("El resultado del modulo o resto es: ", numero)

else:

    print("\nEsta opción no existe")


print("\nFin.")
