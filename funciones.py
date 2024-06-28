import json

def agregarUsuario(nombre:str,correo:str,fechaderegistro:str):
    with open("biblioteca.json", mode ='r') as agregarjson:  #as = ---> alias sin .
        leerJson = json.load(agregarjson)

        usuario={
            "usuarioID":len(leerJson["Usuario"])+1,
            "Nombre": nombre,
            "Email":  correo,
            "FechaRegistro": fechaderegistro
            }
        leerJson["Usuario"].append(usuario) #.append agrega lo requerido  al final de la lista

    with open("biblioteca.json", mode ='w') as agregarjson: 
        json.dump(leerJson , agregarjson , indent=4) #.dump escribe en una sona especifica del json 
    print("Cliente agregado ")

def editarUsuario(usuarioID:int , nombre:str,correo:str,fechaderegistro:str ): #para editar se tine que agregar una nueva variable de id del usuario 
    with open("biblioteca.json", mode ='r') as editarjson: 
        leerJson = json.load(editarjson)

        busquedadecliente = False                                              # la busqueda de cliente queda en False por q no emos encontrado el cliente aun
        for usuario in leerJson["Usuario"]:
            if usuario["UsuarioID"] == usuarioID:
                usuario["Nombre"] = nombre
                usuario["Email"] = correo
                usuario["FechaRegistro"] = fechaderegistro                      #para buscar al usuario a traves de la id
                busquedadecliente = True                                        # la busqueda del cliente queda en True por que lo encontramos 
                break
        if not busquedadecliente:
            print("No se a encontrado al cliente")                              #mensaje para q se vea mejor q no se a encontrado al cliente
        else:
            with open("biblioteca.json", mode ='w') as editarjson: 
                json.dump(leerJson , editarjson , indent=4)
            print("Cliente editado ")

def eliminarUsuarios(idEliminar):
   with open("biblioteca.json", mode ='r') as eliminarjson: 
        leerJson = json.load(eliminarjson)
        buscadorID = False
        for i , eliminar in enumerate(leerJson["Usuario"]):
            if eliminar ["UsuarioID"] == idEliminar:
                leerJson["Usuario"].pop(i)             #.pop es para eliminar
                buscadorID = True
                break
        if not  buscadorID:
            print("La id indicada no existe")
        else:
            for h in range(i, len(leerJson["Usuario"])):
                leerJson["Usuario"][h]["UsuarioID"]-= 1   #si borramos un usuario resta un valor al id 
            with open("biblioteca.json", mode ='w') as eliminarjson: 
                json.dump(leerJson , eliminarjson, indent=4)
            print("Cliente eliminado ")         

def verUsuario(verUsuarios:str):
    with open("biblioteca.json", mode ='r') as verusuariosjson: 
        leerJson = json.load(verusuariosjson)
        print(leerJson["Usuario"])


