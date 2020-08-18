def foreign_change_calculator(amount):
    mex_to_col = 161.03

    return mex_to_col * amount


def main():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a pesos colombianos\n')

    amount = float(input('¿Cuántos pesos mexicanos quieres convertir a pesos colombianos?: '))

    result =  foreign_change_calculator(amount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(amount,result))


if __name__ == "__main__":
    main()