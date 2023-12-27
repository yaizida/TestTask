def is_even0(value):
    return value % 2 == 0


def is_even(value):
    return (value & 1) == 0


def is_even2(value):
    new_value = str(value / 2)
    for i in range(len(new_value)-1):
        if new_value[i] == '.' and new_value[i+1] != '0':
            return False
    return True


def is_even3(value):
    if [i for i in str(value/2)][::-1][0] != '0':
        return False
    return True


def is_even4(value):
    if value - int(value) == 0:
        return True
    return False


if __name__ == '__main__':
    value = int(input())
    print(is_even0(value))
    print(is_even(value))
    print(is_even2(value))
    print(is_even3(value))


""" Плюсы реализации первого метода:
    - Простота понимания
    - Применимость
    Минусы:
    - Скорость
    """


""" Плюсы реализации второго метода:
    - Скорость
    Минусы:
    - Нельзя расширить проверку
"""

"""Третий и четвертый метод:
    просто решил еще несколько варинатов сделать (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧"""
