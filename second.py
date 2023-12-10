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


class CircularBufferUsingArray:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = [None] * max_size
        self.head = 0
        self.size = 0

    def append(self, value):
        if self.size < self.max_size:
            index = (self.head + self.size) % self.max_size
            self.buffer[index] = value
            self.size += 1
        else:
            print("Buffer is full")

    def get(self):
        result = []
        for i in range(self.size):
            index = (self.head + i) % self.max_size
            result.append(self.buffer[index])
        return result

"""Плюсы(2):
    - Не зависит от доп. импортов
    Минусы(2):
    - Скорость
    """
