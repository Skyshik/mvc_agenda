from model.model import Model
from view.view import View

class Controller:

    #Constructor

    def __init__(self):
        self.model = Model()
        self.view = View()
    
    #Contacto controllers--------------------------------------------------------------------------------------

    def agregar_contacto(self, id_contacto, nombre,tel,correo,direccion):
        v, c = self.model.agregar_contacto(id_contacto, nombre,tel,correo,direccion)
        if(v):
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if(e):
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self,id_contacto,nombre = '',tel = '',correo = '',direccion = ''):
        e = self.model.actualizar_contacto(id_contacto,nombre,tel,correo,direccion)
        if(e):
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if(e):
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contacto_letra(self,letra):
        c = self.model.leer_contacto_letra(letra)
        self.view.mostrar_contactos(c)

    #Citas controllers --------------------------------------------------------------------------------------
    def agregar_cita(self, id_cita, id_contacto, lugar,fecha,hora,asunto):
        v, c = self.model.agregar_cita(id_cita, id_contacto, lugar,fecha,hora,asunto)
        if(v):
            self.view.agregar_cita(c)
        elif(v == -1):
            self.view.cita_ya_existe(id_cita)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if(e):
            self.view.mostrar_cita(c)
        else:
            self.view.contacto_no_existe(id_cita)

    def leer_todas_citas(self):
        c = self.model.leer_todas_citas()
        self.view.mostrar_citas(c)

    def actualizar_cita(self,id_cita, id_contacto = '',lugar = '',fecha = '',hora = '',ausnto = ''):
        e = self.model.actualizar_cita(id_cita, id_contacto, lugar,fecha,hora,ausnto)
        if(e):
            self.view.actualizar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    def borrar_cita(self, id_cita):
        e, c = self.model.borrar_cita(id_cita)
        if(e):
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(c)

    def leer_citas_fecha(self,fecha):
        c = self.model.leer_citas_fecha(fecha)
        self.view.mostrar_citas(c)

    #General controllers

    def insertar_contactos(self):
        self.agregar_contacto(1,'Juan Perez','462-123-0012','juanperez@gmail.com','Buenavista 11587')
        self.agregar_contacto(2,'Marco Rodriguez','462-333-9992','mjrh54@gmail.com','Moctezuma 587')
        self.agregar_contacto(3,'Juanito Robles','462-223-1292','1aa54@hotmail.com','Rosas Secc. 3 25')
        self.agregar_contacto(4,'Maria Ramirez','462-832-9212','maria12@gmail.com','Ecualiptos 1532')
        self.agregar_contacto(5,'Pablo Picapiedra','462-093-1221','PabloPP@outlook.com','San pedro 10')
        self.agregar_contacto(6,'Jose Azul','462-323-0091','Jose41@hotmail.com','Apt. B S/N Encinos')

    def insertar_citas(self):
        self.agregar_cita(1,1,'Irapuato','03/05/2020','12:10','Comida')
        self.agregar_cita(2,2,'Salamanca','04/05/2020','12:00','Comida')
        self.agregar_cita(3,4,'Gto','03/05/2020','12:20','Comida')
    
    def menu(self):
        while(True):
            self.view.menu()
            o = input("Selecciona una opcion (1-13): ")
            if o == '1':
                dic = {"id": "", "Nombre" : "", "Telefono": "", "Correo": "", "Direccion": ""}
                for i in dic.keys():
                    print(i, "= ")
                    dic[i] = input("")
                values = []
                for i,j in dic.items():
                    values.append(j)
                self.agregar_contacto(int(values[0]),values[1],values[2],values[3],values[4])
            elif o == '2':
                dic = {"id": "", "Nombre" : "", "Telefono": "", "Correo": "", "Direccion": ""}
                for i in dic.keys():
                    print(i, "= ")
                    dic[i] = input("")
                values = []
                for i,j in dic.items():
                    values.append(j)
                self.actualizar_contacto(int(values[0]),values[1],values[2],values[3],values[4])
            elif o == '3':
                r = int(input("ID CONTACTO: "))
                self.leer_contacto(r)
            elif o == '4':
                r = int(input("ID CONTACTO: "))
                self.borrar_contacto(r)
            elif o == '5':
                dic = {"id": "","idContacto":"", "Lugar" : "", "Fecha": "", "Hora": "", "Asunto": ""}
                for i in dic.keys():
                    print(i, "= ")
                    dic[i] = input("")
                values = []
                for i,j in dic.items():
                    values.append(j)
                self.agregar_cita(int(values[0]),int(values[1]),values[2],values[3],values[4],values[5])
            elif o == '6':
                dic = {"id": "","idContacto":"", "Lugar" : "", "Fecha": "", "Hora": "", "Asunto": ""}
                for i in dic.keys():
                    print(i, "= ")
                    dic[i] = input("")
                values = []
                for i,j in dic.items():
                    values.append(j)
                self.actualizar_cita(int(values[0]),int(values[1]),values[2],values[3],values[4],values[5])
            elif o == '7':
                r = int(input("ID CITA: "))
                self.leer_cita(r)
            elif o == '8':
                r = int(input("ID CITA: "))
                self.borrar_cita(r)
            elif o == '9':
                r = input("Letra: ")
                self.leer_contacto_letra(r)
            elif o == '10':
                r = input("Fecha (dia/mes/año) :")  
                self.leer_citas_fecha(r)  
            elif o == '11':
                self.leer_todos_contactos()
            elif o == '12':
                self.leer_todas_citas()
            elif o == '13':
                self.view.end()
                break
            else: 
                print("Opcion invalida.\n")

    def  start(self):
        #Display a welcome message
        self.view.start()
        #Insert data in model
        self.insertar_contactos()
        self.insertar_citas()
        #Show all contacts in DB
        #self.leer_todos_contactos()
        #self.leer_contacto_letra('J')
        self.menu()
        