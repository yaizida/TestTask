"""Как вариант можно просто замкнуть односвязный список. """


class Node():
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class CircularList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.head = new_node

    def __str__(self):
        result = ''
        node = self.head
        while node:
            result += f'[{node.value}]->'
            node = node.next_node
        return result


if __name__ == "__main__":
    cl = CircularList()
    for i in range(10):
        cl.add_to_head(i)
    print(cl)


"""Плюсы:
    Простота исполнения если знать как работает односвязный список
    Минусы:
    Не очень оптимизированное решение"""
