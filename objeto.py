class Consola:

    def __init__(self,color,capacidad):
        self.color = color
        self.capacidad = capacidad

class PlayStation:    
    def define_color(self,color):
        self.color = color
        return color

    
    def define_capacidad(self,capacidad):
        self.capacidad = capacidad
        return capacidad


def run():

    consolita = PlayStation()

    while True:
        opcion = input('''
            ¿Cómo te gustaría que fuese tu PS4?
            [1] Color
            [2] Capacidad
            [3] Salir
        ''')

        if opcion=='1':
            color = input("Dinos de qué color quieres tu PS4: ")

            consolita.define_color(color)
            print("El color tu PS4 es {}".format(color))

        elif opcion=='2':
            capacidad = input("Dinos que qué capacidad quieres que sea tu PS4: ")

            consolita.define_capacidad(capacidad)
            print("La capacidad de tu PS4 es de {} GB".format(capacidad))

        elif opcion=='3':
            break
        else:
            print("Comando incorrecto")


if __name__ == "__main__":
    print("Crearé un objeto consola PS4")
    run()