from Clase4_V3 import Entidad


class Mascota(Entidad):  # Hereda de Entidad
    def __init__(self):
        super().__init__()  # Inicializa nombre e id (historia)
        self.__tipo = ""
        self.__peso = ""
        self.__fecha_ingreso = ""
        self.__lista_medicamentos = []
        
    def asignarTipo(self, t):
        self.__tipo = t
    def verTipo(self):
        return self.__tipo
    def asignarPeso(self, p):
        self.__peso = p
    def verPeso(self):
        return self.__peso
    def asignarFecha(self, f):
        self.__fecha_ingreso = f
    def verFecha(self):
        return self.__fecha_ingreso
    def asignarLista_Medicamentos(self, n):
        self.__lista_medicamentos = n
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos

class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self, historia):
        for m in self.__lista_mascotas:
            if historia == m.verId():  # Usamos verId()
                return True
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self, mascota):
        self.__lista_mascotas.append(mascota) 
   
    def verFechaIngreso(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verId():  # Usamos verId()
                return masc.verFecha() 
        return None

    def verMedicamento(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verId():  # Usamos verId()
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verId():  # Usamos verId()
                self.__lista_mascotas.remove(masc)
                return True
        return False 

def main():
    servicio_hospitalario = sistemaV()
    while True:
        menu = int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas 
                       \n4- Ver medicamentos 
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu == 1:
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia = int(input("Ingrese la historia clínica: "))
            if not servicio_hospitalario.verificarExiste(historia):
                mas = Mascota()
                mas.asignarNombre(input("Nombre: "))
                mas.asignarId(historia)  # Usamos asignarId()
                mas.asignarTipo(input("Tipo (felino/canino): "))
                mas.asignarPeso(float(input("Peso: ")))
                mas.asignarFecha(input("Fecha (dd/mm/aaaa): "))
                nm = int(input("Cantidad de medicamentos: "))
                lista_med = []
                for _ in range(nm):
                    med = Medicamento() # type: ignore
                    med.asignarNombre(input("Nombre medicamento: "))
                    med.asignarDosis(int(input("Dosis: ")))
                    lista_med.append(med)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
                print("Mascota ingresada!")
            else:
                print("Ya existe una mascota con esa historia.")
        elif menu == 6:
            break

if __name__ == "__main__":
    main()





            

                

