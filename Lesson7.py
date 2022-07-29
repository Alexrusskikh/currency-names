class Matrix:

    def __init__(self, elements):
        row_len = len(elements[0])
        self.elements = elements
        self.n_rows = len(self.elements)
        self.n_columns = len(self.elements[0])

        for row in elements:
            if len(row) != row_len:
                print('Матрица имеет неправильный разммер')
                self.elements = None
                self.n_rows = None
                self.n_columns = None
                break

    def __str__(self):
        return str(self.elements)

    def __add__(self, other):
        try:
            return [[self.elements[i][j] + other.elements[i][j] for j in range(self.n_columns)]
                    for i in range(self.n_rows)]
        except IndexError as e:
            print('Матрицы имеют несовместимый размер')
        except TypeError as e:
            print('Не заданы элементы матрицы')

    def __mul__(self, other):
        summ = 0
        temp_matrix = []
        result_matrix = []
        if self.n_columns != other.n_rows:
            print('Матрицы имеют несовместимый размер')
        else:
            for k in range(self.n_rows):
                for j in range(other.n_columns):
                    for i in range(self.n_columns):
                        summ = summ + self.elements[k][i] * other.elements[i][j]
                    temp_matrix.append(summ)
                    summ = 0
                result_matrix.append(temp_matrix)
                temp_matrix = []
            return result_matrix
matrix_1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix_2 = Matrix([[9, 8, 7], [6, 5, 4]])
print(matrix_1)
s = matrix_1 + matrix_2
m = matrix_1 * matrix_2
print(s)
print(m)

matrix_3 = Matrix([[1, 2, 3], [1, 2, 3]])
matrix_4 = Matrix([[1, 2], [2, 3], [3, 4]])
s = matrix_3 + matrix_4
m = matrix_3 * matrix_4
print(s)
print(m)

#Задание2
from abc import ABC, abstractmethod

class Clothing(ABC):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    @abstractmethod
    def calc_square(self, w, h):
        pass

class Coat(Clothing):
    def __init__(self, w, h):
        super().__init__(w, h)
    @property
    def calc_square(self):
        return self.w / 6.5 + 0.5

class Suit(Clothing):
    def __init__(self, w, h):
        super().__init__(w, h)
    @property
    def calc_square(self):
        return self.h * 2 + 0.3
coat = Coat(3.25, 3)
suit = Suit(4, 4.35)
print(coat.calc_square + suit.calc_square)

#Задание3
class Cell:

    def __init__(self, quantity):
        if type(quantity) == int:
            self.quantity = quantity
        else:
            raise Exception('Некорректный аргумент')

    def __str__(self):
        return f'{self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell(self.quantity - other.quantity)
        else:
            print('Разность количества ячеек двух клеток НЕ больше нуля')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, cells_num):
        result = ''
        for i in range(int(self.quantity / cells_num)):
            result += f'{"*" * cells_num}\\n'
        result += f'{"*" * (self.quantity % cells_num)}'
        return result
c_1 = Cell(27)
c_2 = Cell(4)

print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1.make_order(10))
print(c_2.make_order(2))