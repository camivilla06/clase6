class Paciente:
    def __init__(self):
        self.datos = {
            'nombre': '',
            'cedula': 0,
            'genero': '',
            'servicio': ''
        }

    # Métodos dinámicos
    def asignarDato(self, clave, valor):
        if clave in self.datos:
            self.datos[clave] = valor
    def verDato(self, clave):
        return self.datos.get(clave, None)

class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        
    def verificarPaciente(self, cedula):
        return any(p.verDato('cedula') == cedula for p in self.__lista_pacientes)
        
    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, c):
        for p in self.__lista_pacientes:
            if p.verDato('cedula') == c:
                return p
        return None
            
    def verNumeroPacientes(self):
        print("En el sistema hay:", len(self.__lista_pacientes), "pacientes")

def main():
    sis = Sistema() 
    while True:
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar paciente, \n2 ver Paciente\n\t--> ")) 
        if opcion == 1:
            cedula = int(input("Cédula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cédula >>".upper()) 
            else:    
                pac = Paciente() 
                pac.asignarDato('nombre', input("Nombre: ")) 
                pac.asignarDato('cedula', cedula)
                pac.asignarDato('genero', input("Género: ")) 
                pac.asignarDato('servicio', input("Servicio: ")) 
                sis.ingresarPaciente(pac)
                print("Paciente ingresado!") 
        elif opcion == 2:
            c = int(input("Cédula a buscar: ")) 
            p = sis.verDatosPaciente(c) 
            if p:
                print("Nombre:", p.verDato('nombre')) 
                print("Cédula:", p.verDato('cedula')) 
                print("Género:", p.verDato('genero')) 
                print("Servicio:", p.verDato('servicio')) 
            else:
                print("No existe un paciente con esa cédula") 
        elif opcion == 0:
            break 

if __name__ == "__main__":
    main()

        
        
        
        
        
        
