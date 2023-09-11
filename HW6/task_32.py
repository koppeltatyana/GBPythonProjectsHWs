# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint


def get_random_array(array_len: int) -> list[int]:
    """
    Получение массива случайных чисел

    :param array_len: Длина массива
    :return: Массив чисел
    """
    return [randint(0, 10) for _ in range(array_len)]

def get_diapazone_array(array: list[int], min_value: int, max_value: int) -> list[int]:
    """
    Получение массива индексов чисел, где значения будут лежать в интервале  (min_value, max_value)

    :param array: Входной массив чисел
    :param min_value: Нижняя граница интервала
    :param max_value: Верхняя граница интервала
    :return: Массив индексов чисел
    """
    return [i for i in range(len(array)) if array[i] > min_value and array[i] < max_value]


if __name__ == "__main__":
    n = int(input("Введите длину массива: "))
    array = get_random_array(array_len=n)
    print("Сгенерированный массив чисел:", array)
    min_value = int(input("Введите минимальное значение массива: "))
    max_value = int(input("Введите максимальное значение массива: "))
    if min_value > max_value:
        min_value, max_value = max_value, min_value
    print(
        f"Массив индексов, принадлежащий интервалу ({min_value}, {max_value}):",
        get_diapazone_array(array=array, min_value=min_value, max_value=max_value),
    )
