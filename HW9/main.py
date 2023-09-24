import pandas as pd
from pandas import DataFrame


def task_40(file_content: DataFrame):
    """
    Задача 40:
    Работать с файлом california_housing_train.csv, который находится в папке sample_data.
    Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

    :param file_content: Экземпляр класса DataFrame (прочитанный файл)
    """
    return file_content[df.population < 500].median_house_value.median()


def task_42(file_content: DataFrame):
    """
    Задача 42: Узнать какая максимальная households в зоне минимального значения population.

    :param file_content: Экземпляр класса DataFrame (прочитанный файл)
    """
    return file_content[
        file_content.population == file_content.population.min()
    ].households.max()


if __name__ == '__main__':
    df = pd.read_csv('sample_data/california_housing_train.csv')  # чтение файла
    print('Средняя стоимость дома, где кол-во людей от 0 до 500 (population) =', task_40(file_content=df), '\n\n')
    print('Максимальная households в зоне минимального значения population =', task_42(file_content=df), '\n\n')
