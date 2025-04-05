class Mascota:
    def __init__(self):
        self.datos = {
            'nombre': '',
            'historia': 0,
            'tipo': '',
            'peso': 0,
            'fecha': '',
            'medicamentos': []
        }

    def asignarDato(self, clave, valor):
        if clave in self.datos:
            self.datos[clave] = valor
    def verDato(self, clave):
        return self.datos.get(clave, None)

class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self, historia):
        return any(m.verDato('historia') == historia for m in self.__lista_mascotas)
        
    def ingresarMascota(self, mascota):
        self.__lista_mascotas.append(mascota)
        return True
    
    # Resto de métodos similares a la versión original...

def main():
    servicio = sistemaV()
    while True:
        opcion = int(input('''\n1- Ingresar mascota \n2- Salir\nOpción: '''))
        if opcion == 1:
            historia = int(input("Historia clínica: "))
            if not servicio.verificarExiste(historia):
                mas = Mascota()
                mas.asignarDato('nombre', input("Nombre: "))
                mas.asignarDato('historia', historia)
                # ... (resto de asignaciones)
                servicio.ingresarMascota(mas)
            else:
                print("Mascota ya existe!")
        elif opcion == 2:
            break

if __name__ == "__main__":
    main()





            

                

