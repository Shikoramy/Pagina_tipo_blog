usuarios_registrados = []
comentarios = []
articulos = []

class Usuario:
    def __init__(self, id, nombre, apellido, telefono, username, email, contrasena, fecha_registro, avatar, estado, online, tipo_usuario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contrasena = contrasena
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = estado
        self.online = online
        self.tipo_usuario = tipo_usuario

    def login(self, username, contrasena):
        for usuario in usuarios_registrados:
            if usuario.username == username and usuario.contrasena == contrasena:
                print("Inicio de sesión exitoso")
                self.menu_1()
                return
        print("Nombre de usuario o contraseña incorrectos")

    def registrar(self):
        usuarios_registrados.append(self)

    def comentar(self, id_articulo, contenido):
        comentario = Comentario(len(comentarios) + 1, id_articulo, self.id, contenido)
        comentarios.append(comentario)
        print("Comentario agregado")

    def buscar_usuario_por_id(self, id_usuario):
        for usuario in usuarios_registrados:
            if usuario.id == id_usuario:
                return usuario

    def ver_comentarios(self, id_articulo):
        print("Comentarios del artículo:")
        for comentario in comentarios:
            if comentario.id_articulo == id_articulo:
                usuario = self.buscar_usuario_por_id(comentario.id_usuario)
                print(f"Usuario: {usuario.username}")
                print(f"Contenido: {comentario.contenido}")
                print("----------------------")


    def menu_1(self):
        while True:
            if isinstance(self, Colaborador):
                print("1. Comentar en un artículo")
                print("2. Publicar un artículo")
                print("3. Ver comentarios de un artículo")
                print("4. Volver atrás")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    id_articulo = int(input("Ingrese el ID del artículo: "))
                    contenido = input("Ingrese el contenido del comentario: ")
                    articulo_encontrado = False
                    for articulo in articulos:
                        if articulo.id == id_articulo:
                            self.comentar(id_articulo, contenido)
                            articulo_encontrado = True
                            break
                    if not articulo_encontrado:
                        print("Artículo no encontrado")
                elif opcion == "2" and isinstance(self, Colaborador):
                    titulo = input("Ingrese el título del artículo: ")
                    resumen = input("Ingrese el resumen del artículo: ")
                    contenido = input("Ingrese el contenido del artículo: ")
                    fecha_publicacion = input("Ingrese la fecha de publicación del artículo: ")
                    imagen = input("Ingrese la imagen del artículo: ")
                    articulo = Articulo(len(articulos) + 1, self.id, titulo, resumen, contenido, fecha_publicacion, imagen, "publicado")
                    articulos.append(articulo)
                    print("Artículo publicado")
                elif opcion == "3":
                    id_articulo = input("Ingrese el ID del artículo: ")
                    self.ver_comentarios(int(id_articulo))            
                elif opcion == "4":
                    break
            else:
                print("1. Comentar en un artículo")   
                print("2. Ver comentarios de un artículo")
                print("3. Volver atrás")
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    id_articulo = int(input("Ingrese el ID del artículo: "))
                    contenido = input("Ingrese el contenido del comentario: ")
                    articulo_encontrado = False
                    for articulo in articulos:
                        if articulo.id == id_articulo:
                            self.comentar(id_articulo, contenido)
                            articulo_encontrado = True
                            break
                    if not articulo_encontrado:
                        print("Artículo no encontrado")
                elif opcion == "2":
                    id_articulo = input("Ingrese el ID del artículo: ")
                    self.ver_comentarios(int(id_articulo))            
                elif opcion == "3":
                    break

class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido

class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado

class Colaborador(Usuario):
    pass

def menu():
    print("Bienvenido!")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        username = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        for usuario in usuarios_registrados:
            if usuario.username == username and usuario.contrasena == contrasena:
                usuario.login(username, contrasena)
                return
        print("Nombre de usuario o contraseña incorrectos")
    elif opcion == "2":
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = input("Ingrese su teléfono: ")
        username = input("Ingrese su nombre de usuario: ")
        email = input("Ingrese su email: ")
        contrasena = input("Ingrese su contraseña: ")
        fecha_registro = input("Ingrese su fecha de registro: ")
        avatar = input("Ingrese su avatar: ")
        estado = input("Ingrese su estado: ")
        online = input("¿Está en línea? (s/n): ") == "s"
        tipo_usuario = input("Ingrese su tipo de usuario (Colaborador/Público): ")
        if tipo_usuario.lower() == "colaborador":
            usuario = Colaborador(len(usuarios_registrados) + 1, nombre, apellido, telefono, username, email, contrasena, fecha_registro, avatar, estado, online, tipo_usuario)
        else:
            usuario = Usuario(len(usuarios_registrados) + 1, nombre, apellido, telefono, username, email, contrasena, fecha_registro, avatar, estado, online, tipo_usuario)
        usuario.registrar()
        print("Registro exitoso")
    elif opcion == "3":
        print("Saliendo")
    else:
        print("Opción inválida")


while True:
    menu()


#Integrantes:
#Fernando Javier Svoboda
# José A. Figueroa        
