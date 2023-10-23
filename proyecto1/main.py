""" CRUD notas y Usuarios """
from usuarios import acciones

print(""" 
Acciones disponibles:
      - Registro (r)
      - Login (l)

""")

hazEl = acciones.Acciones()

accion = input("Que quieres hacer?: ")
if accion == "r":
    hazEl.registro()

elif accion == "l":
    hazEl.login()