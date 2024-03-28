import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def treat_shape(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def treat_shape(self):
        print("Rectangle Info:", end=" ")
        if math.fabs(self.width - self.height) > 5:
            print("Rectangle Area: ", round(self.height * self.width, 2))
        elif self.width - self.height == 0:
            print("Square perimeter: ", round(self.width * 4, 2))
        else:
            print("Rectangle perimeter", round(2 * (self.width + self.height), 2))


class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def treat_shape(self):
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
            print('Triangle Perimeter: ',
                  round(math.sqrt(math.pow(self.height, 2) + math.pow(self.width / 2, 2)) * 2 + self.width, 2))
        else:
            self.print_triangle()

    def print_triangle(self):
        if self.width % 2 == 0 or self.width > self.height * 2:
            print("Triangle can not be printed.")
        else:
            l = [x for x in range(1, int(self.width) + 1, 2)]
            opt = len(l) - 2
            lines = self.height - 2
            times = int(lines / opt)
            print(" " * (int((self.width - l[0]) / 2)), "*" * l[0])  # one time only
            for c in range(times + int(lines % opt)):
                print(" " * int(int((self.width - l[1]) / 2)), "*" * (l[1]))
            for d in range(opt - 1):  # rest to be treated!
                for i in range(times):
                    print(" " * int(int((self.width - l[d + 2]) / 2)), "*" * (l[d + 2]))
            print(" " * (int((self.width - l[-1]) / 2)), "*" * l[-1])


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
            shape = Rectangle(width, height)
        else:
            shape = Triangle(width, height)
        shape.treat_shape()

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
