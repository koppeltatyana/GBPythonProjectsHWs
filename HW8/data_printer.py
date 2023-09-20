class DataPrinter:
    """ Класс для методов вывода данных из файла """

    @staticmethod
    def print_data(file_name: str):
        """
        Вывод всех данных из файла

        :param file_name: Наименование файла
        """
        print('\nДанные в справочнике:')
        with open(file_name, 'r', encoding='utf-8') as file:
            print(file.read())

    @staticmethod
    def print_searched_data(file_name: str, user_for_search: dict[str]):
        """
        Вывод данных из файла по поисковой строке

        :param file_name: Наименование файла
        :param user_for_search: Данные пользователя, информацию по которому ищем
        """
        with open(file_name, 'r', encoding='utf-8') as file:
            users = [x.replace('\n', ' ') for x in file.read().strip().split('\n\n')]

        result = list(
            filter(
                lambda x:
                user_for_search['firstname'].lower() in x.split()[0].lower() and
                user_for_search['lastname'].lower() in x.split()[1].lower() and
                user_for_search['middlename'].lower() in x.split()[2].lower() and
                user_for_search['phone'].lower() in x.split()[3].lower() and
                user_for_search['address'].lower() in ''.join(x.split()[4].lower()),
                users
            )
        )

        if not result:
            print(f'\nУказанные пользовательские данные не дали результатов\n')
        else:
            print(f'\nРезультат поиска:')
            print(*result, end='\n\n')
