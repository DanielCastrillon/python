#Capturar y manejar errores en codigo

try:
    nombre = input("Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es: " + nombre
    print(nombre)
    print(nombre_usuario)
except:
    print("Ha ocurrido un error")

else:
    print("Todo es correcto")

finally:
    print("Fin de la iteracion")