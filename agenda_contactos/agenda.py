import csv


class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []


    def add(self, name, phone, email):
        contact = Contact(name,phone,email)
        self._contacts.append(contact)
        self._save()
        

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)
        

    def delete(self,name):
        for i, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[i]
                break

    
    def search(self,name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            print("No se encontró el contacto {}".format(name))

    def _save(self):
        with open('contacts.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))


    def _print_contact(self,contact):
        print("--- * --- * --- * --- *--- * --- *--- * --- *")
        print("Nombre: {}".format(contact.name))
        print("Teléfono: {}".format(contact.phone))
        print("Email: {}".format(contact.email))
        print("--- * --- * --- * --- *--- * --- *--- * --- *")


def run():

    contact_book = ContactBook()

    try:
        with open('contacts.csv','rt',encoding="utf8") as f:
            reader = csv.reader(f)
        for i,row in enumerate(reader):
            if i==0:
                continue
            elif row==[]:
                continue
            else:
                contact_book.add(row[0],row[1],row[2])
    except FileNotFoundError:
        print("No existe el archivo 'contacts.csv', Debe añadir un nuevo contacto para crearlo.")


    while True:
        command = input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        ''')

        if command == 'a':
            name = input("Escribe el nombre del contacto: ")
            phone = input("Escribe el número del contacto: ")
            email = input("Escribe el email del contacto: ")

            contact_book.add(name,phone,email)

        elif command == 'ac':
            name = input("Escribe el nombre del contacto que quieres actualizar: ")

            contacto_viejo = contact_book.search(name)
            contacto_viejo = contact_book.delete(name)

            print("Ahora actualiza los campos: ")

            name2 = input("Escribe el nombre del contacto: ")
            phone = input("Escribe el número del contacto: ")
            email = input("Escribe el email del contacto: ")

            contact_book.add(name2,phone,email)


        elif command == 'b':
            name = input("Escribe el nombre del contacto: ")

            contact_book.search(name)

        elif command == 'e':
            name = input("Escribe el nombre del contacto a eliminar: ")

            contact_book.delete(name)

        elif command == 'l':
            contact_book.show_all()

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print("BIENVENIDO A LA AGENDA DE CONTACTOS")
    run()