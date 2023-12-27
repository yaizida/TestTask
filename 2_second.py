"""За основу взята очередь с огрониченнием по длине"""


class LimitedQueue:

    def __init__(self, max_n):
        self.max_n = max_n
        self.queue = [None] * self.max_n
        self.head = 0  # Голова указывает на индекс 0
        self.tail = 0  # Хвост указывает на индекс 0
        self.size = 0  # При создании очередь пуста, её длина - 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        if self.queue[self.tail] is not None:
            self.head = (self.head + 1) % self.max_n
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        if self.size < self.max_n:
            self.size += 1


q = LimitedQueue(8)
for i in range(10):
    q.push(i + 1)
print('В очередь с ограничением 8 добавили 10 элементов:', q.queue)


"""Плюсы: Давольно оптимизированное решние"""
"""Минусы: Не самая простая реализация методов"""

