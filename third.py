def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


# можно конечно sys.std.readline().rstrip().split()
# Но я не вижу смысла
print(quicksort(list(map(int, input().split()))))


"""В худшем случае сложность алгоритма O(n**2)
    Основной принцип в основе алгоритма Разделяй и властвуй
    Опорный эдемент может быть любым
"""
