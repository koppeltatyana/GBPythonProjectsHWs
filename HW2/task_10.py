"""
Задача 10: На столе лежат N монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
from random import choice


def get_random_binary_array(array_length: int = 10) -> list[int]:
    """
    Получить случайный бинарный массив

    :param array_length: Длина массива
    :return: Бинарный массив переданной длины
    """
    return [choice([0, 1]) for x in range(array_length)]


def find_element_indexes(array: list[int], value: int) -> list[int]:
    """
    Получить список индексов вхождений элемента value в массив

    :param array: Исходный массив чисел
    :param value: Элемент для поиска в массиве
    :return: Массив индексов вхождений
    """
    result = []
    for i in range(len(array)):
        if array[i] == value:
            result += [i]
    return result


def answer(array: list[int]) -> str:
    """
    Получение ответа на вопрос в задаче

    :param array: Бинарный массив орлов (0) и решек (1)
    :return: Строка с ответом на вопрос в задаче
    """
    head_count = len(find_element_indexes(array=array, value=0))
    if head_count == len(array) - head_count:
        return 'Количество орлов и решек одинаковое. Можете переворачивать либо орлов, либо решек'
    elif head_count < len(array) - head_count:
        return f'Можете переворачивать орлов, так как их меньше ({head_count} шт), ' \
               f'чем решек ({len(array) - head_count} шт)'
    else:
        return f'Можете переворачивать решки, так как их меньше ({len(array) - head_count} шт), ' \
               f'чем орлов ({head_count} шт)'


if __name__ == "__main__":
    while True:
        array_len = int(input('Введите количество монеток, на которых хотите посмотреть: '))
        if array_len == 1:
            print('С одной монеткой неинтересно, попробуйте еще раз.')
        elif array_len < 0:
            print('С отрицательным количеством монет ничего не выйдет. Попробуйте еще раз.')
        else:
            break
    binary_array = get_random_binary_array(array_length=array_len)
    print('Ваш массив монеток (0 - орел, 1 - решка):', *binary_array)
    print(answer(binary_array))
