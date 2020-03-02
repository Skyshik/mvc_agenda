class View:

    #Contactos ----------------------------------
    def mostrar_contacto(self,contacto):
        print("******* Datos del contacto ********")
        print("Nombre:",contacto.nombre)
        print("telefono:",contacto.tel)
        print("Correo:",contacto.correo)
        print("Direccion:",contacto.direccion)
        print("***********************************")

    def mostrar_contactos(self,contactos):
        print("****** Contactos definidos ********")
        for c in contactos:
            print(c.nombre,c.tel,c.correo,c.direccion)
        print("***********************************")

    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha agregado a la base de datos!')

    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'Se ha borrado de la base de datos!')

    def actualizar_contacto(self, id_contacto):
        print(id_contacto, 'Se ha modificado correctamente!')

    def contacto_ya_existe(self, contacto):
        print('EL CONTACTO: ',contacto.id_contacto, 'YA EXISTE EN LA BASE DE DATOS')
    
    def contacto_no_existe(self, id_contacto):
        print('EL CONTACTO: ',id_contacto, 'NO EXISTE EN LA BASE DE DATOS')
    
    
    #General methods
    def start(self):
        print("Esto es un ejemplo de vista sencilla")
    
    def end(self):
        print("Hasta la vista!")

    def menu(self):
        print("1. Agregar contacto")
        print("2. Actualizar contacto")
        print("3. Ver contacto")
        print("4. Borrar contacto")
        print("5. Agregar cita")
        print("6. Actualizar cita")
        print("7. Ver cita")
        print("8. Borrar cita")
        print("9. Buscar contactos por letra")
        print("10. Bucar citas por fecha")
        print("11. Ver todos los contactos")
        print("12. Ver todas las citas")
        print("13. Terminar")
    #Citas ----------------------------------
    def mostrar_cita(self, cita):
        print("******* Datos de la cita ********")
        print("id_contacto:",cita.id_contacto)
        print("telefono:",cita.lugar)
        print("Correo:",cita.fecha)
        print("Direccion:",cita.hora)
        print("Direccion:",cita.asunto)
        print("***********************************")

    def mostrar_citas(self,citas):
        print("*************** CITAS ACTUALES ***************")
        for c in citas:
            print(c.id_contacto, c.lugar,c.fecha,c.hora,c.asunto)
        print("-----------------------------------------------")

    def agregar_cita(self, cita):
        print(cita.id_cita, 'Se ha agregado a la base de datos!')

    def borrar_cita(self, cita):
        print(cita.id_cita, 'Se ha borrado de la base de datos!')

    def actualizar_cita(self, id_cita):
        print(id_cita, 'Se ha modificado correctamente!')

    def cita_ya_existe(self, cita):
        print(cita.id_cita, 'YA EXISTE EN LA BASE DE DATOS')
    
    def cita_no_existe(self, id_cita):
        print(id_cita, 'NO EXISTE EN LA BASE DE DATOS')

    