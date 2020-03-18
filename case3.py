import turtle


def get_num_hexagons():
    try:
        number = int(input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '))
        if 4 <= number <= 20:
            return number
        else:
            raise ValueError
    except ValueError:
        while True:
            try:
                number = int(input('Оно должно быть от 4 до 20: '))
                if 4 <= number <= 20:
                    return number
                else:
                    raise ValueError
            except ValueError:
                continue


def filling_colors():
    print('Допустимые цвета заливки: ')
    print(' ' + 'красный', 'cиний', 'зеленый', 'желтый', 'ораньжевый', 'фиолетовый',
          'розовый ', sep='\n ')


def get_color_choice():
    color = input('Пожалуйста, введите цвет: ')
    if color == 'красный' or color == 'синий' or color == 'зеленый' or color == 'желтый' or color == 'ораньжевый' or color == 'фиолетовый' or color == 'розовый':
        return color
    else:
        while True:
            color = input("'" + color + "' не является верным значением. Пожалуйста, повторите попытку: ")
            if color == 'красный' or color == 'синий' or color == 'зеленый' or color == 'желтый' or color == 'ораньжевый' or color == 'фиолетовый' or color == 'розовый':
                return color
            else:
                continue


def draw_hexagon(x, y, side_len, color):
    if color == 'красный':
        color = 'red'
    elif color == 'синий':
        color = 'blue'
    elif color == 'зеленый':
        color = 'green'
    elif color == 'желтый':
        color = 'yellow'
    elif color == 'ораньжевый':
        color = 'orange'
    elif color == 'фиолетовый':
        color = 'purple'
    elif color == 'розовый':
        color = 'pink'
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.left(30)
    for i in range(6):
        turtle.forward(side_len)
        turtle.right(60)
    turtle.right(30)
    turtle.end_fill()
    turtle.up()


def main():
    number = get_num_hexagons()
    filling_colors()
    color1 = get_color_choice()
    color2 = get_color_choice()
    turtle.speed(0)
    turtle.screensize(500, 500)
    side_len = 500 / (number * 3**0.5)
    x = -250
    y = 200
    for j in range(number):
        if j % 2 == 0:
            color1, color2 = color2, color1
        turtle.up()
        turtle.goto(x, y)
        turtle.down()
        for i in range(number):
            if i % 2:
                draw_hexagon(x, y, side_len, color1)
            else:
                draw_hexagon(x, y, side_len, color2)
            x = x + 500 / number
        y = y - 1.5 * side_len
        if j % 2:
            x -= (number - 0.5) * (500 / number)
        else:
            x -= (number + 0.5) * (500 / number)
    turtle.mainloop()


if __name__ == '__main__':
    main()
