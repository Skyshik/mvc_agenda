from .contacto import Contacto
from .cita import Cita

class Model:

    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id(self,id_contacto):
        for c in self.contactos:
            if(c.id_contacto == id_contacto):
                return True, c 
        return False,0

    def esta_id_cita(self, id_cita):
        for c in self.citas:
            if(c.id_cita == id_cita):
                return True, c
        return False,0

    #Contacto methods -------------------------------
    def agregar_contacto(self, id_contacto, nombre,tel,correo,direccion):
        if not self.esta_id(id_contacto)[0]:
            c = Contacto(id_contacto, nombre,tel,correo,direccion)
            self.contactos.append(c)
            return True, c
        return False, c

    def leer_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)
        return e, c

    def actualizar_contacto(self,id_contacto,nombre,tel,correo,direccion):
        e, c = self.esta_id(id_contacto)
        if(e):
            if not (nombre == ''):
                c.nombre = nombre
            if not (tel == ''):            
                c.tel = tel
            if not (correo == ''):
                c.correo = correo
            if not (direccion == ''):
                c.direccion = direccion
            return True
        return False
    #Cambiada por la de arriba
    #def actualizar_contacto_1(self,lista):
    #    e, c = self.esta_id(int(lista[0]))
    #    if e:
    #        if not (lista[1] == ""):
    #            c.nombe = lista[1]
    #        if not (lista[2] == ""):    
    #            c.tel = lista[2]
    #        if not (lista[3] == ""):    
    #            c.correo = lista[3]
    #        if not (lista[4] == ""):
    #            c.direccion = lista[4]
    #        return True
    #    return False
    def borrar_contacto(self, id_contacto):
        e, contacto = self.esta_id(id_contacto)
        if e:
            self.contactos.remove(contacto)
            list_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            #for id in ids_temp:
            for c in list_temp:
                self.citas.remove(c)
            return True, contacto
        return False, 0

    def leer_contacto_letra(self,letra):
        Conta = []
        for i in self.contactos:
            if (i.nombre.lower().startswith(letra.lower())):
                Conta.append(i)
        return Conta

    
    def leer_todos_contactos(self):
        return self.contactos    


    #Cita methods -------------------------------

    def agregar_cita(self, id_cita, id_contacto, lugar,fecha,hora,asunto):
        if not self.esta_id(id_contacto)[0]:
            print("No existe este contacto")
            return False,0
        if not self.esta_id_cita(id_cita)[0]:
            c = Cita(id_cita,id_contacto,lugar,fecha,hora,asunto)
            self.citas.append(c)
            return True, c
        print("Ya esxiste la cita")
        return -1, 0

    def leer_cita(self, id_cita):
        e, c = self.esta_id_cita(id_cita)
        
        return e, c

    def leer_todas_citas(self):
        return self.citas
    
    def actualizar_cita(self,id_cita,id_contacto,lugar,fecha,hora,asunto):
        e, c = self.esta_id_cita(id_cita)
        if e:
            if not (id_contacto == ''):
                c.id_contacto = id_contacto
            if not (lugar == ''):
                c.lugar = lugar
            if not (fecha == ''):
                c.fecha = fecha
            if not (hora == ''):
                c.hora = hora
            if not (asunto == ''):
                c.asunto = asunto
            return True
        return False
    def actualizar_cita_1(self,lista):
        e, c = self.esta_id_cita(int(lista[0]))
        if e:
            if not (lista[1] == ""):
                c.id_contacto = lista[1]
            if not (lista[2] == ""):    
                c.lugar = lista[2]
            if not (lista[3] == ""):    
                c.fecha = lista[3]
            if not (lista[4] == ""):
                c.hora = lista[4]
            if not (lista[5] == ""):    
                c.asunto = lista[5]
            return True
        return False

    def borrar_cita(self, id_cita):
        e, c = self.esta_id_cita(id_cita)
        if(e):
            self.citas.remove(c)
            return True, c
        return False, 0

    def leer_citas_fecha(self, fecha):
        citas = []
        for i in self.citas:
            if(i.fecha.startswith(fecha)):
                citas.append(i)
        return citas

    def busqueda_cita_fecha_1(self,fecha):
        citas = [x for x in self.citas if x.fecha.startswith(fecha)]
        return citas


