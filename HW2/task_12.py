"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""
import math


def answer(mult: int, summ: int) -> list[tuple]:
    """
    Получить список возможных пар чисел

    :param mult: Значение произведения чисел
    :param summ: Значение суммы чисел
    :return: Список кортежей чисел
    """
    d = summ ** 2 - 4 * mult
    if d < 0:
        print(f'Нет таких чисел, которые бы удовлетворяли правилам:\nx + y = {summ}\nx * y = {mult}')
        return []

    num_1_1 = (summ + math.sqrt(d)) / 2
    num_1_2 = (summ - math.sqrt(d)) / 2
    if num_1_1 == num_1_2:
        num_2 = summ - num_1_1
        return [(num_1_1, num_2)]
    else:
        num_2_1 = summ - num_1_1
        num_2_2 = summ - num_1_2
        return [(num_1_1, num_2_1), (num_1_2, num_2_2)]


if __name__ == "__main__":
    nums_mult = int(input('Петя вводит произведение чисел: '))
    nums_summ = int(input('Петя вводит сумму чисел: '))
    print('Числа, загаданные Петей: ', *answer(mult=nums_mult, summ=nums_summ))
