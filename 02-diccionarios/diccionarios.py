import datetime
contactos = [
    {
        'nombre':'Daniel',
        'email':'daniel@mail.com'
    },
    {
        'nombre':'Carlos',
        'email':'carlos@mail.com'
    },
    {
        'nombre':'Arturo',
        'email':'arturo@mail.com'
    },
    {
        'nombre':'Luis',
        'email':'luis@mail.com'
    },
    {
        'nombre':'Alberto',
        'email':'alberto@mail.com'
    }
    
]

for contacto in contactos:
    print("-----------------")
    print(f"Nombre: {contacto['nombre']}")
    print(f"Email: {contacto['email']}")

print(datetime.date.today())