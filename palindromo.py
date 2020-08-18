def palindromo2(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    else:
        return False


if __name__ == "__main__":
    word = input("Escribe una palabra: ")
    resultado = palindromo2(word)

    if resultado:
        print("Sí es palíndromo")
    else:
        print("No es palíndromo")