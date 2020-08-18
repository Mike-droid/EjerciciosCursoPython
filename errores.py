#Este código lanzará un error si el denominador es = 0

def run(numerador,denominador):
    try:
        print(numerador / denominador)
    except:
        print("No se puede dividir entre 0")


if __name__ == "__main__":
    numerador = float(input("Ingresa un numerador: "))
    denominador = float(input("Ingresa un denominador: "))
    run(numerador,denominador)