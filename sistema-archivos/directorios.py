import os
import shutil #Copiar, Pegar y Mover archivos

#Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
    print("Carpeta creada")
else:
    print("La carpeta ya existe")

#Eliminar carpeta
## os.rmdir("./mi_carpeta")

#Copiar
ruta_original = "C:/wamp64/www/python/sistema-archivos/fichero.txt"
ruta_nueva = "C:/wamp64/www/python/sistema-archivos/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

# Mover archivo
## shutil.move(ruta_original, ruta_nueva)

#Contenido de carpeta
print("Contenido de carpeta")
contenido = os.listdir("./mi_carpeta")

for archivo in contenido:
    print("Archivo: "+archivo)

print(contenido)