from HW8.data import WELCOME_STRING
from data_writer import DataWriter
from data_create import DataCreate
from data_printer import DataPrinter


class Interface:
    """ Класс для пользовательского интерфейса """

    FILE_NAME = 'notebook.txt'

    def interface(self):
        while True:
            print(WELCOME_STRING)
            variant = int(input('Введите номер варианта: '))
            data_create = DataCreate()
            match variant:
                case 1:
                    print('Введите пользовательские данные: ')
                    user_data = DataCreate.create_data_string(
                        firstname=data_create.data_input(data_create.firstname_prefix),
                        lastname=data_create.data_input(data_create.lastname_prefix),
                        middlename=data_create.data_input(data_create.middlename_prefix),
                        phone=data_create.data_input(data_create.phone_prefix),
                        city=data_create.data_input(data_create.city_prefix),
                    )
                    DataWriter.write_data(file_name=self.FILE_NAME, text=user_data)
                case 2:
                    DataPrinter.print_data(file_name=self.FILE_NAME)

                case 3:
                    print('\nВведите данные пользователя, которого необходимо найти '
                          '(можете ничего не вводить, тогда по этому полю не будет производиться поиск пользователей)')
                    DataPrinter.print_searched_data(
                        file_name=self.FILE_NAME,
                        user_for_search=data_create.input_data_for_search(),
                    )

                case 4:

                    print('Введите пользовательские данными для удаления '
                          '(можете ничего не вводить, тогда по этому полю не будет производиться поиск пользователей)')
                    DataWriter().delete_data(
                        file_name=self.FILE_NAME,
                        user_data_for_deleting=data_create.input_data_for_delete(),
                    )
                case 5:
                    print('Введите данными пользователя, для которого необходимо изменить данные '
                          '(можете ничего не вводить, тогда по этому полю не будет производиться поиск пользователей)')

                    DataWriter().edit_data(
                        file_name=self.FILE_NAME,
                        user_for_search=data_create.input_data_for_search(),
                    )
                case 6:
                    print('Программа будет завершена')
                    return
                case _:
                    print('Не был выбран ни один из предложенных вариантов. Программа будет завершена')
                    return
