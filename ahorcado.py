import random


IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = ['lavadora','secadora','sofa','gobierno','platzi','maestro','programacion','tribunal','futbol','ardilla','computadora','telefono','paloma','laptop','pelicula','television','teclado','perro','gato','lenguaje','idioma','avion','vehiculo','control','color','deporte','ejercicio','juego','juguete','libro','aprendizaje','alumno','doctor','abogado','programa','carpeta','dinero','billete','moneda','carne','comida','fruta','verdura','arroz','manzana','platano','engranaje','python','java','javascript','ruby','zafiro','esmeralda','pikachu','bomba','agua','leche','avena','tortilla','taco','borrador','lapiz','pluma','platano','metal','arma','armadura','desconocido','correr','brincar']

def random_word():
    idx = random.randint(0,len(WORDS)-1)
    return WORDS[idx]

def show_board(hidden_word,tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('---- * ---- * ---- * ---- * ---- * ---- * ---- * ---- *')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0

    while True:
        show_board(hidden_word , tries)
        current_letter = input("Escoge una letra: ")

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
        
        if len(letter_indexes) == 0:
            tries += 1

            if tries == 6:
                show_board(hidden_word,tries)
                print('')
                print('¡Has perdido! :( La palabra era {}'.format(word))
                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter
            
            letter_indexes = []

        if "-" not in hidden_word:
            print(word)
            print('Felicidades, ¡ganaste!')
            break


if __name__ == "__main__":
    print('Bienvenidos al juego del ahorcado')
    run()