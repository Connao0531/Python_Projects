
print("******************************************************")
print("* Programa que determina si un numero es par o impar *")
print("******************************************************\n")

numero_uno = int(input("Por favor, introduce un número entero: "))
resultado = numero_uno / 2
tipo_numero = type(resultado)

if resultado  == int(resultado):

    print("El numero", numero_uno, "es par")

else:

    print('El numero', numero_uno ,'es immpar')
