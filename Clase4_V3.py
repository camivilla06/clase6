class Entidad:
    def __init__(self):
        self.__nombre = ''
        self.__id = 0  # Cedula o Historia Clínica

    # Métodos comunes
    def verNombre(self):
        return self.__nombre
    def verId(self):
        return self.__id
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarId(self, id):
        self.__id = id

class Paciente(Entidad):
    def __init__(self):
        super().__init__()  # Hereda nombre e id
        self.__genero = ''
        self.__servicio = ''

    # Métodos específicos
    def asignarGenero(self, g):
        self.__genero = g
    def verGenero(self):
        return self.__genero
    def asignarServicio(self, s):
        self.__servicio = s
    def verServicio(self):
        return self.__servicio

class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        
    def verificarPaciente(self, cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verId():  # Usamos verId() en lugar de verCedula()
                return True 
        return False
        
    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, c):
        if not self.verificarPaciente(c):
            return None
        for p in self.__lista_pacientes:
            if c == p.verId():  # Usamos verId()
                return p
            
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 

def main():
    sis = Sistema() 
    while True:
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente\n\t--> ")) 
        
        if opcion == 1:
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                pac = Paciente() 
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarId(cedula)  # Usamos asignarId()
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
        elif opcion == 2:
            c = int(input("Ingrese la cedula a buscar: ")) 
            p = sis.verDatosPaciente(c) 
            if p != None:
                print("Nombre: " + p.verNombre()) 
                print("Cedula: " + str(p.verId()))  # Usamos verId()
                print("Genero: " + p.verGenero()) 
                print("Servicio: " + p.verServicio()) 
            else:
                print("No existe un paciente con esa cedula") 
        elif opcion == 0:
            break 

if __name__ == "__main__":
    main()

        
        
        
        
        
        
