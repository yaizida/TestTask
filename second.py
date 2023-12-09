from collections import deque


# Дек
class Deque:
    def __init__(self, max_size):
        self.item = deque(maxlen=max_size)

    def append(self, value):
        self.item.append(value)

    def get(self):
        return list(self.item)


"""Плюсы(1):
    - Удобство
    Минусы(1):
    - Зависимость дополнительного импорта"""


# Очередь
class Queue:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.insert(0, item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)


"""Плюсы(2):
    - Не зависит от импортов
    Минусы(2):
    - Скорость
    """
