import usuarios.usuario as modelo

class Acciones:
    def registro(self):
        print("\nOK!! Registrate")
        nombre = input("Cual es tu nombre: ")
        apellido = input("Cuales son tus apellidos: ")
        email = input("Cual es tu email: ")
        password = input("Cual es tu password: ")

        """ SEPASAN LOS ONJETOS A LA CLASE """
        usuario = modelo.Usuario(nombre, apellido, email, password)

        """ SE REGISTRA EL USUARIO """
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Correcto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print(f"Error en el registro.")
    
    def login(self):
        print("\nLogin del sistema")
        try:
            email = input("Cual es tu email: ")
            password = input("Cual es tu password: ")

            usuario = modelo.Usuario('','',email, password)
            login = usuario.idenificar()

            print(login)
            print(email)
            if email == login[3]:
                print(f"Bienvenido {login[1]}, fecha registro {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto")

    def proximasAcciones(self, usuario):
        print(f"""\nHola Que deseas hacer:
              \n 1. Crear nota
              \n 2. Mostrar notas
              \n 3. Eliminar notas
              \n 4. Salir
              """)
        accion = input("Digita una opcion: ")

        if accion == "1":
            print("Crear nota")
            self.proximasAcciones(usuario)

        elif accion == "2":
            print("Mostrar nota")
            self.proximasAcciones(usuario)

        elif accion == "3":
            print("Eliminar nota")
            self.proximasAcciones(usuario)

        elif accion == "4":
            print("Salir")
            exit()
        
        else:
            print("No valida")

        return None

