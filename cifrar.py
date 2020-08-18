KEYS = {
    'a': '97',
    'b': '98',
    'c': '99',
    'd': '100',
    'e': '101',
    'f': '102',
    'g': '103',
    'h': '104',
    'i': '105',
    'j': '106',
    'k': '107',
    'l': '108',
    'm': '109',
    'n': '110',
    'o': '111',
    'p': '112',
    'q': '113',
    'r': '114',
    's': '115',
    't': '116',
    'u': '117',
    'v': '118',
    'w': '119',
    'x': '120',
    'y': '121',
    'z': '122',
    'A': '65',
    'B': '66',
    'C': '67',
    'D': '68',
    'E': '69',
    'F': '70',
    'G': '71',
    'H': '72',
    'I': '73',
    'J': '74',
    'K': '75',
    'L': '76',
    'M': '77',
    'N': '78',
    'O': '79',
    'P': '80',
    'Q': '81',
    'R': '82',
    'S': '83',
    'T': '84',
    'U': '85',
    'V': '86',
    'W': '87',
    'X': '88',
    'Y': '89',
    'Z': '90',
    '.': '46',
    ',': '44',
    '?': '63',
    '!': '33',
    ' ': '32',
}

def cypher(message):
    cyper_message = ''

    for letter in message:
        cyper_message += bin(int(KEYS[letter]))
    return cyper_message


def decypher(message):
    decipher_message = ''

    for letter in message:
        for key,value in KEYS.items():
            if value == letter:
                decipher_message += key
    
    return decipher_message


def run():
    while True:
        command = input('''Bienvenido a criptografía, ¿qué deseas hacer?:
        [c]ifrar un mensaje
        [d]escifrar un mensaje
        [s]alir
        ''')

        if command == 'c':
            message = input('Escribe tu mensaje: ')
            cypher_ms = cypher(message)
            print(cypher_ms)
        elif command == 'd':
            message = input('Escribe tu mensaje cifrado: ')
            decypher_ms = decypher(message)
            print(decypher_ms)
        elif command == 's':
            break
        else:
            print('Comando no válido')

if __name__ == "__main__":
    run()