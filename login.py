# Crear log in.

usuario = "Claus"
clave = "2023a"

print("Ingrese su usuario")
entrada = input()
print("Ingrese la clave")
password = input()

#Para validar datos
if(entrada == usuario and password == clave):
    print("¡Bienvenida Claus!")
else: 
    print("Clave y/o contraseña son incorrectos")