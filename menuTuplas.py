from funciones import *                                              # el * importa todo de el archivo funciones.py
menu =("agregar " , "editar" , "eliminar", "ver usuario", "salir ")
contador = 0
for i in menu:
    contador += 1
    print(f"[{contador}].-{i}")

while True:
    opcion = int(input("ingrese una opcion: "))
    if opcion  == 1:
        nombre = str(input("Ingrese un nombre: "))
        correo = str(input("Ingrese un correo: "))
        fechaderegistro = str(input("Ingrese un fecha de registro: "))
        agregarUsuario(nombre , correo, fechaderegistro)
    elif opcion == 2:
        usuarioID = int(input("ingrese la id de su usuario: "))
        nombre = str(input("Ingrese un nombre: "))
        correo = str(input("Ingrese un correo: "))
        fechaderegistro = str(input("Ingrese un fecha de registro: "))
        editarUsuario(usuarioID,nombre,correo,fechaderegistro)
    elif opcion == 3:
        idEliminar = int(input("ingrese la id que desea eliminar: "))
        eliminarUsuarios(idEliminar)
    elif opcion == 4:
        verUsuarios =str
        verUsuario(verUsuarios)
    elif opcion == 5:
        print("has salido del sistema de biblioteca")
        break


