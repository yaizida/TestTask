def quicksort(array):
    """Быстрая сортировка."""
    if len(array) <= 1:
        return array
    middle_element_index = len(array) // 2
    pivot = array[middle_element_index]
    left, center, right = partition(array, pivot)
    return quicksort(left) + center + quicksort(right)


def partition(array, pivot):
    left, center, right = [], [], []
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        elif item == pivot:
            center.append(item)

    # Кортеж с тремя списками
    return left, center, right


# можно конечно sys.std.readline().rstrip().split()
# Но я не вижу смысла
print(quicksort(list(map(int, input().split()))))


"""В худшем случае сложность алгоритма O(n**2)
    Основной принцип в основе алгоритма Разделяй и властвуй
    Опорный эдемент может быть любым
"""
