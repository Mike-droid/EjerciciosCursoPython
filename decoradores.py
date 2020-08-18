def protected(func):
    def wrapper(password):
        if password == 'platzi':
            return func()
        else:
            print("La contraseña es incorrecta.")
    return wrapper


@protected
def protected_func(): #!Unicamente se ejecuta la función si el password es correcto
    print('Tu contraseña es correcta.')


if __name__ == "__main__":
    password = input("Ingresa tu contraseña: ")

    protected_func(password)