from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller
#c1 = Contacto(1,'Juan Perez','462-123-9992','mjrhv354@gmail.com','Moctezuma 11587')
#c2 = Contacto(2,'Marco Rodriguez','462-333-9992','mjrh54@gmail.com','Moctezuma 587')
#print(c1.nombre,"\n",c1.tel,"\n",c1.correo,"\n",c1.dir)

#cita = Cita(1,1,'Irapuato, Gto.', '17/02/2020', '15:48','Clase de sistemas de información')

#print(cita.id_cita)
#print(cita.id_contacto)
#print(cita.lugar)
#print(cita.fecha)
#print(cita.hora)
#print(cita.asunto)
"""
contactos = []
contactos.append(c1)
contactos.append(c2)

respuesta = input("Ingrese un nombre: ")
for i in contactos:
    if(i.nombre.lower() == respuesta.lower()):
        print("Si esta.")
        break
else:
    print("No esta.")
s = m.leer_contacto(2)
print(s.nombre,s.tel)

m.actualizar_contacto(2, 'Marco R','462-333-9992','mjrh54@gmail.com','Moctezuma 587')
s = m.leer_contacto(2)
print(s.nombre)

c = m.leer_cita(1)
print(c.id_contacto,c.lugar,c.hora,c.fecha,c.asunto)

m.actualizar_cita(1,2,'Irapuato','07/03/2020','5:00','Comida')
c = m.leer_cita(1)
print(c.id_contacto,c.lugar,c.hora,c.fecha,c.asunto)
c = m.borrar_cita(2)
print(c)

for i in range(20):
    print("-",end=" ")
print("\nEliminando al Contacto 2")
s = m.leer_contacto(2)
print(s.nombre)
s = m.borrar_contacto(2)
print(s)

c = m.borrar_cita(2)
print(c)
#Actualizar ciertos elementos de la lista.
dic = {"idcita": "", "idcontacto" : "", "lugar": "", "fecha": "", "hora": "", "asunto":"" }

for i in dic.keys():
    print(i, "= ")
    dic[i] = input("")


m.agregar_cita(1,1,'Irapuato','03/05/2020','12:10','Comida')
m.agregar_cita(2,2,'Salamanca','04/05/2020','12:00','Comida')

values = []
for i,j in dic.items():
    values.append(j)
s = m.actualizar_cita_1(values)
print(s)
s = m.leer_cita(2)
print(s.id_cita,s.id_contacto,s.lugar,s.fecha,s.hora,s.asunto)


#Busqueda por una letra...
letra = input("")
letra = letra.lower()
s = m.busqueda_contacto(letra)
print(s)

#Regresar por fecha
m.agregar_cita(1,1,'Irapuato','03/05/2020','12:10','Comida')
m.agregar_cita(2,2,'Salamanca','04/05/2020','12:00','Comida')
m.agregar_cita(3,2,'Gto','03/05/2020','12:20','Comida')
fecha = input("")
s = m.busqueda_cita_fecha_1(fecha)
print(s)
"""
"""

m = Model()
m.agregar_contacto(1,'Juan Perez','462-123-9992','mjrhv354@gmail.com','Moctezuma 11587')
m.agregar_contacto(2,'Marco Rodriguez','462-333-9992','mjrh54@gmail.com','Moctezuma 587')
m.agregar_contacto(3,'Juanito Robles','462-123-9992','mjrhv354@gmail.com','Moctezuma 11587')
m.agregar_contacto(4,'Maria Ramirez','462-333-9992','mjrh54@gmail.com','Moctezuma 587')
m.agregar_contacto(5,'Pablo Picapiedra','462-123-9992','mjrhv354@gmail.com','Moctezuma 11587')
m.agregar_contacto(6,'Jose Azul','462-333-9992','mjrh54@gmail.com','Moctezuma 587')
m.agregar_cita(1,1,'Irapuato','03/05/2020','12:10','Comida')
m.agregar_cita(2,2,'Salamanca','04/05/2020','12:00','Comida')
m.agregar_cita(3,4,'Gto','03/05/2020','12:20','Comida')
v = View()
s = m.leer_todos_contactos()
v.mostrar_contactos(s)
c = m.leer_contacto(6)
v.mostrar_contacto(c)


f,c = m.borrar_contacto(6)
if (f):
    v.borrar_contacto(c)
else:
    v.contacto_no_existe(1)

q = m.leer_todas_citas()
v.mostrar_citas(q)
q = m.leer_cita(3)
v.mostrar_cita(q)

f,c = m.borrar_cita(1)
if (f):
    v.borrar_cita(q)
else:
    v.cita_no_existe(1)
"""
"""
#Menu de opciones
m = Model()
m.agregar_contacto(1,'Juan Perez','462-123-9992','mjrhv354@gmail.com','Moctezuma 11587')
m.agregar_contacto(2,'Marco Rodriguez','462-333-9992','mjrh54@gmail.com','Moctezuma 587')
v = View()

print("1. Agregar contacto")
print("2. Editar contacto")
print("3. Borrar contacto")
print("4. Ver contacto")
print("5. Agregar cita")
print("6. Editar cita")
print("7. Borrar cita")
print("8. Ver cita")

while(True):
    R = int(input())
    if(R == 1):
        dic = {"id": "", "Nombre" : "", "Telefono": "", "Correo": "", "Direccion": ""}
        for i in dic.keys():
            print(i, "= ")
            dic[i] = input("")
        values = []
        for i,j in dic.items():
            values.append(j)
            print(values)
        s = m.agregar_contacto(int(values[0]),values[1],values[2],values[3],values[4])
        print(s)
    elif(R == 2):
        dic = {"id": "", "Nombre" : "", "Telefono": "", "Correo": "", "Direccion": ""}
        for i in dic.keys():
            print(i, "= ")
            dic[i] = input("")
        values = []
        for i,j in dic.items():
            values.append(j)
        m.actualizar_contacto_1(values)
    elif( R == 3):
        r = int(input("Contacto: "))
        f,c = m.borrar_contacto(r)
        if (f):
            v.borrar_contacto(c)
        else:
            v.contacto_no_existe(1)
    elif( R == 4):
        r = int(input("Contacto: "))
        s = m.leer_contacto(r)
        print(s.nombre, s.tel, s.correo, s.direccion)
    elif(R == 5):
        dic = {"idcita": "", "idcontacto" : "", "lugar": "", "fecha": "", "hora": "", "asunto":"" }
        for i in dic.keys():
            print(i, "= ")
            dic[i] = input("")
        values = []
        for i,j in dic.items():
            values.append(j)
        m.agregar_cita(int(values[0]),values[1],values[2],values[3],values[4],values[5])
    elif(R == 6):
        dic = {"idcita": "", "idcontacto" : "", "lugar": "", "fecha": "", "hora": "", "asunto":"" }
        for i in dic.keys():
            print(i, "= ")
            dic[i] = input("")
        values = []
        for i,j in dic.items():
            values.append(j)
        m.actualizar_cita_1(values)
    elif( R == 7):
        r = int(input("Cita: "))
        f,c = m.borrar_cita(r)
        if (f):
            v.borrar_cita(c)
        else:
            v.cita_no_existe(1)
    else:
        r = int(input("Cita: "))
        s = m.leer_cita(r)
        print(s)
    r = input("Otra operación ? Y == Si, N == No \n" )
    r = r.lower()
    if(r == 'y'):
        continue
    else:
        break
"""
cont = Controller()
cont.start()

