def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


if __name__ == "__main__":
    number = int(input("Escribe un número para calcular su factorial: "))
    resultado = factorial(number)
    print("El factorial es " + str(resultado))