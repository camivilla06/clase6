class Sistema:
    def __init__(self, archivo='pacientes.txt'):
        self.__archivo = archivo

    def verificarPaciente(self, cedula):
        with open(self.__archivo, 'r') as f:
            for linea in f.readlines():
                if linea.split(',')[1] == str(cedula):
                    return True
        return False

    def ingresarPaciente(self, nombre, cedula, genero, servicio):
        with open(self.__archivo, 'a') as f:
            f.write(f"{nombre},{cedula},{genero},{servicio}\n")
        return True

    def verDatosPaciente(self, cedula):
        with open(self.__archivo, 'r') as f:
            for linea in f.readlines():
                datos = linea.strip().split(',')
                if datos[1] == str(cedula):
                    return datos
        return None

def main():
    sis = Sistema()
    while True:
        opcion = int(input("\n0. Salir \n1. Ingresar paciente \n2. Buscar paciente\nOpción: "))
        if opcion == 1:
            cedula = int(input("Cédula: "))
            if not sis.verificarPaciente(cedula):
                nombre = input("Nombre: ")
                genero = input("Género: ")
                servicio = input("Servicio: ")
                sis.ingresarPaciente(nombre, cedula, genero, servicio)
                print("Paciente guardado!")
            else:
                print("Cédula ya existe.")
        elif opcion == 2:
            cedula = int(input("Cédula a buscar: "))
            datos = sis.verDatosPaciente(cedula)
            if datos:
                print("Nombre:", datos[0])
                print("Cédula:", datos[1])
                print("Género:", datos[2])
                print("Servicio:", datos[3])
            else:
                print("No encontrado.")
        elif opcion == 0:
            break

if __name__ == "__main__":
    main()

        
        
        
        
        
        
