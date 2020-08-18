import turtle

def main():
    window = turtle.Screen()
    mike = turtle.Turtle()

    make_square(mike)

    turtle.mainloop()
        

def make_square(mike):
    length = int(input("Tamaño del cuadrado: "))
    for i in range(4):
        make_line_and_turn(mike,length)


def make_line_and_turn(mike,length):
    mike.forward(length)
    mike.left(90)


if __name__ == "__main__":
    main()