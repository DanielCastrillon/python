from io import open #Manejo de archivos
import pathlib
import shutil #Copiar, Pegar y Mover archivos
import os # Eliminar archivos
import os.path # Comprobar si un archivo existe

#Abrir/crear archivo si no existe
archivo = open("fichero.txt", "a+")

#Abrir archivo
archivo_lectura = open("fichero.txt", "r")


#Escribir
archivo.write("*********Texto desde Python***********\n")

#Leer el arhivo
#contenido = archivo_lectura.read()
#print(contenido)

#Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
print(lista)

#Copiar
ruta_original = "C:/wamp64/www/python/sistema-archivos/fichero.txt"
ruta_nueva = "C:/wamp64/www/python/sistema-archivos/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

# Mover archivo
## shutil.move(ruta_original, ruta_nueva)

# Eliminar
## os.remove(ruta_nueva)

# Comprobar si un archivo existe o no
print(os.path.abspath("./"))
if os.path.isfile(os.path.abspath("./")+"/"+"ficheros.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")