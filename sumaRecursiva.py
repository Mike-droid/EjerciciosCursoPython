
def suma_recursiva(numero):
    if numero<=0:
        return 0
    else:
        return numero + suma_recursiva(numero-1)


if __name__ == "__main__":
    numero = int(input("Ingrese un número para sumarlo recursivamente: "))

    resultado = suma_recursiva(numero)

    print(resultado)