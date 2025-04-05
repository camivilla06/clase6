class sistemaV:
    def __init__(self, archivo='mascotas.csv'):
        self.__archivo = archivo

    def ingresarMascota(self, nombre, historia, tipo, peso, fecha, medicamentos):
        with open(self.__archivo, 'a') as f:
            meds_str = '|'.join([f"{m['nombre']}:{m['dosis']}" for m in medicamentos])
            f.write(f"{nombre},{historia},{tipo},{peso},{fecha},{meds_str}\n")

    # Resto de métodos (verificar, eliminar, etc.) implementados con archivos...

def main():
    servicio = sistemaV()
    # Lógica similar a la original pero guardando en archivos...





            

                

