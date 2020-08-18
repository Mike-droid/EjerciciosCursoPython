from lampara import Lampara
#!Estamos trayendo la clase desde el archivo lampara.py

def run():
    lamparita = Lampara(_is_turned_on=False)

    while True:
        command = input('''
        ¿Qué deseas hacer?
        [p]render
        [a]pagar
        [s]alir
        ''')

        if command == 'p':
            lamparita.turn_on()
        elif command == 'a':
            lamparita.turn_off()
        else:
            break


if __name__ == "__main__":
    run()