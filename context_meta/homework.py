import csv
import os


# TASK 1
class ChangeDir:
    def __init__(self, directory):
        self.requested_directory = directory
        self.start_dir = os.getcwd()

    def __enter__(self):
        os.chdir(self.requested_directory)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.start_dir)


with ChangeDir('dir1'):
    print(os.listdir())

with ChangeDir('dir2'):
    print(os.listdir())


# TASK 2
class ReadItems:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        if self.mode == 'r':
            self.opened_file = open(self.file)
            self.file_dict = csv.DictReader(self.opened_file)
            return self.file_dict
        raise ValueError('context manager only reads files')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.opened_file.close()


def show_items(file):
    with ReadItems(file, 'r') as items:
        for item in items:
            print(item)


show_items('items.csv')


# TASK 3
class Student:
    def __init__(self, name, stud_id):
        self.name = name
        self.stud_id = stud_id
        self.lap = self.Laptop()

    def show(self):
        """Вывести информацию о студенте и его ноутбуке"""
        print(self.__repr__())

    def __repr__(self):
        return f'{self.name} {self.stud_id}\n{self.lap.__repr__()}'

    class Laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.cpu = 'i5'
            self.ram = 8

        def __repr__(self):
            return f'{self.brand} {self.cpu} {self.ram}'


# Создаем двух студентов
s1 = Student('Ivan', 2)
s2 = Student('Mary', 3)

# Выводим данные по студенту и его ноутбуку
s1.show()

# Увеличиваем память у ноутбука студента s1
s1.lap.ram = 16
s1.show()

# У каждого студента отдельный ноутбук (уникальный объект)
lap1 = s1.lap
lap2 = s2.lap
print(id(lap1))
print(id(lap2))


# TASK 4
class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs = {k.upper(): v for k, v in attrs.items()}
        return type.__new__(cls, name, bases, attrs)


class Math(metaclass=Meta):
    pi = 3.141592653589793
    e = 2.718281828459045
    tau = 6.283185307179586


m = Math()
print(m.PI)

print(m.E)

print(m.pi)
