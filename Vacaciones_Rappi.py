print("*************************************")
print("*Sistema de control vacacional Rappi*")
print("*************************************\n")

nombre_trabajador = input("Por favor, ingrese su nombre: ")
clave_departamento = int(input("Por favor, ingrese la clave de su departamento: "))
antiguedad_trabajador = int(input("Por favor, ingrese cuantos años tiene trabajando en el departamento: "))

antiguedad_1 = 6
antiguedad_2_a_6 = 14
antiguedad_7 = 20



print("\nNombre: " + nombre_trabajador)

if clave_departamento == 1:

    print("Departamento: Atención al cliente")
    print("Antigüedad:", antiguedad_trabajador, "años")
    print("")

    if antiguedad_trabajador == 1:

        print(nombre_trabajador + "," , "usted tiene", antiguedad_1, "dias de vacaciones")

    elif antiguedad_trabajador >= 2 and antiguedad_trabajador  <= 6:

        print(nombre_trabajador + "," , "usted tiene", antiguedad_2_a_6, "dias de vacaciones")

    elif antiguedad_trabajador >= 7:

        print(nombre_trabajador + "," , "usted tiene", antiguedad_7, "dias de vacaciones")

    
    
elif clave_departamento == 2:

    print("Departamento: Logística")
    print("Antigüedad:", antiguedad_trabajador, "años")
    
    print("")
    
    antiguedad_1 = 7
    antiguedad_2_a_6 = 15
    antiguedad_7 = 22

    if antiguedad_trabajador == 1:

        print(nombre_trabajador + "," , "usted tiene", antiguedad_1, "dias de vacaciones")

    elif antiguedad_trabajador >= 2 and antiguedad_trabajador  <= 6:

        print(nombre_trabajador + "," , "usted tiene", antiguedad_2_a_6, "dias de vacaciones")

    elif antiguedad_trabajador >= 7:

        print(nombre_trabajador + "," , "usted tiene", antiguedad_7, "dias de vacaciones")

    
elif clave_departamento == 3:

    print("Departamento: Gerencia")
    print("Antigüedad:", antiguedad_trabajador, "años")

    print("")

    antiguedad_1 = 10
    antiguedad_2_a_6 = 20
    antiguedad_7 = 30


    if antiguedad_trabajador == 1:

        print(nombre_trabajador + "," , "usted tiene", antiguedad_1, "dias de vacaciones")

    elif antiguedad_trabajador >= 2 and antiguedad_trabajador  <= 6:

        print(nombre_trabajador + "," , "usted tiene", antiguedad_2_a_6, "dias de vacaciones")

    elif antiguedad_trabajador >= 7:

        print(nombre_trabajador + "," , "usted tiene", antiguedad_7, "dias de vacaciones")


else:

    print("La clave del departamento no existe, por favor vuelva a intentarlo.")

print("\nFin.")

    
