# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union


class Parallelogram:
        def __init__(self, lenth: Union[int, float], width: Union[int, float], hight: Union[int, float]):
            """
            Создание и подготовка к работе объекта "Параллелограм"
            :param lenth: длина
            :param width: ширина
            :param hight: высота
            Примеры:
            >>> par1 = Parallelogram(5, 6, 7)  # инициализация экземпляра класса
            """
            if not isinstance(lenth, (int, float)):
                raise TypeError("Длина параллелограма должна быть типа int или float")
            if lenth <= 0:
                raise ValueError("Длина параллелограма должна быть положительным числом")
            self.lenth = lenth

            if not isinstance(width, (int, float)):
                raise TypeError("Ширина параллелограма должна быть типа int или float")
            if width <= 0:
                raise ValueError("Ширина параллелограма должна быть положительным числом")
            self.width = width

            if not isinstance(hight, (int, float)):
                raise TypeError("Высота параллелограма должна быть типа int или float")
            if hight <= 0:
                raise ValueError("Высота параллелограма должна быть положительным числом")
            self.hight = hight
        def volume(self):
            """
            Функция, которая вычисляет объем параллелограма
            :return: объем параллелограма
            Примеры:
            >>> par1 = Parallelogram(5, 6, 7)
            >>> par1.volume()
            """
            return self.lenth * self.width * self.hight
        def square(self):
            """
            Функция, которая вычисляет общую площадь параллелограма
            :return: общая площадь параллелограма
            Примеры:
            >>> par1 = Parallelogram(5, 6, 7)
            >>> par1.square()
            """
            return 2*(self.lenth * self.width + self.lenth * self.hight + self.width * self.hight)

class Point:
    def __init__(self, x: float, y: float, z: float):
        """
        Создание и подготовка к работе объекта "Точка"
        :param x: координата x
        :param y: координата y
        :param z: координата z
        Примеры:
        >>> point1 = Point(5, 13, 7)  # инициализация экземпляра класса
        """
        self.x = x
        self.y = y
        self.z = z
    def change_x(self, dx: float):
        """
        Функция, которая изменяет координату x точки
        :return: новая координата x
        Примеры:
        >>> point1 = Point(5, 13, 7)
        >>> point1.change_x(3)
        """
        x = self.x + dx
        return x
    def dist_(self):
        """
        Функция, которая считает расстояние от начала координат до точки
        :return: расстояние от начала координат до точки
        Примеры:
        >>> point1 = Point(5, 13, 7)
        >>> point1.dist_()
        """
        return (self.x**2 + self.y**2 + self.z**2)**0.5

class Crew:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Команда"
        :param name: имя
        :param age: возраст
        Примеры:
        >>> per1 = Crew("Маша", 21)  # инициализация экземпляра класса
        """
        if not isinstance(name, (str)):
            raise TypeError("Имя должно быть типа str")
        self.name = name

        if not isinstance(age, (int)):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")
        self.age = age

    def change_age(self, d_age):
        """
        Функция, которая меняет возраст на заданное число
        :return: новый возраст
        Примеры:
        >>> per1 = Crew("Маша", 21)
        >>> per1.change_age(3)
        """
        return self.age + d_age

    def change_name(self, new_name: str):
        """
        Функция, которая меняет возраст на заданное число
        :return: новый возраст
        Примеры:
        >>> per1 = Crew("Маша", 21)
        >>> per1.change_name("Саша")
        """
        self.name = new_name
        print(self.name)

if __name__ == "__main__":
    import doctest
    doctest.testmod() # тестирование примеров, которые находятся в документации

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass