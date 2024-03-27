import math


def deal_with_rectangle(w, h):
    print("Rectangle Info:", end=" ")
    if math.fabs(w - h) > 5:
        print("Rectangle Area: ", round(h * w, 2))
    elif w - h == 0:
        print("Square perimeter: ", round(w * 4, 2))
    else:
        print("Rectangle perimeter", round(2 * (w + h), 2))


def print_triangle(w, h):
    if w % 2 == 0 or w > h * 2:
        print("Triangle can not be printed.")
    else:
        l = [x for x in range(1, int(w) + 1, 2)]
        opt = len(l) - 2
        lines = h - 2
        times = int(lines / opt)
        print(" " * (int((w - l[0]) / 2)), "*" * l[0])  # one time only
        for c in range(times + int(lines % opt)):
            print(" " * int(int((w - l[1]) / 2)), "*" * (l[1]))
        for d in range(opt - 1):  # rest to be treated!
            for i in range(times):
                print(" " * int(int((w - l[d + 2]) / 2)), "*" * (l[d + 2]))
        print(" " * (int((w - l[-1]) / 2)), "*" * l[-1])


def deal_with_triangle(w, h):
    opt = input('Choose an option! 1 for print the perimeter or 2 to print the Triangle:')
    while True:
        try:
            opt = int(opt)
            if opt < 1 or opt > 2:
                raise ValueError('Error! option must be an integer: 1/2!')
            else:
                break
        except ValueError as err:
            print(err)
            opt = input('Choose an option! 1 for print the perimeter or 2 to print the Triangle:')
    if opt == 1:
        print('Triangle Perimeter: ', round(math.sqrt(math.pow(h, 2) + math.pow(w / 2, 2)) * 2 + w, 2))
    else:
        print_triangle(w, h)


if __name__ == "__main__":
    print('TWITTER TOWERS ~ BY BRURIA ANAEL COHEN ~')

    x = input('\nChoose an option! 1 for Rectangle or 2 for Triangle, 3 to EXIT:')
    while True:
        try:
            x = int(x)
            if x < 1 or x > 3:
                raise ValueError('Error! option must be an integer: 1/2/3!')
            else:
                break
        except ValueError as exp:
            print(exp)
            x = input('Enter valid option! 1 for Rectangle or 2 for Triangle, 3 to EXIT:')

    while x != 3:
        height = input('\nEnter heihgt! ')
        while True:
            try:
                height = float(height)
                if height < 2:
                    raise ValueError('Error! Enter valid height: positive float number greater than or equal to 2!')
                else:
                    break
            except ValueError as exp:
                print(exp)
                height = input('Enter heihgt! ')

        width = input('Enter width! ')
        while True:
            try:
                width = float(width)
                if width < 0:
                    raise ValueError('Error! Enter valid width: positive float number:')
                else:
                    break
            except ValueError as exp:
                print(exp)
                height = input('Enter width! ')

        if x == 1:
            deal_with_rectangle(width, height)
        else:
            deal_with_triangle(width, height)

        x = input('\nChoose an option! 1 for Rectangle or 2 for Triangle, 3 to EXIT:')
        while True:
            try:
                x = int(x)
                if x < 1 or x > 3:
                    raise ValueError('Error! option must be an integer: 1/2/3!')
                else:
                    break
            except ValueError as exp:
                print(exp)
                x = input('Enter valid option! 1 for Rectangle or 2 for Triangle, 3 to EXIT:')
    print("\nThank you for building TwitterTowers!\n\t\t\t\t* * * *\n")
