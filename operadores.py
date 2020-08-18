def run():
    numA = int(input('Teclea el primer numero: '))
    numB = int(input('Teclea el segundo numero: '))
    textoA = str(numA)
    textoB = str(numB)
    print(textoA + ' + ' + textoB + ' = ' + str(numA+numB))
    print(textoA + ' - ' + textoB + ' = ' + str(numA-numB))
    print(textoA + ' * ' + textoB + ' = ' + str(numA*numB))
    print(textoA + ' / ' + textoB + ' = ' + str(numA/numB))
    print(textoA + ' ** ' + textoB + ' = ' + str(numA**numB))
    print(textoA + ' // ' + textoB + '= ' + str(numA//numB))
    print(textoA + ' % ' + textoB + '= ' + str(numA%numB))


if __name__ == "__main__":
    run()