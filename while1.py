import random

def run():
    number_found = False
    random_number = random.randint(0,101)
    intentos = 1
    while not number_found:
        number = int(input("Escribe un numero entre 0 y 100: "))
    
        if number == random_number:
            print("Felicidades, encontraste el numero, te ha tomado {} intentos".format(intentos))
            number_found = True
        elif number>random_number:
            print("El número es más pequeño")
            intentos+=1
        else:
            print("El número es más grande")
            intentos+=1


if __name__ == "__main__":
    run()