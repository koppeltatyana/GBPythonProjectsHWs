class DataCreate:
    """ Класс для получения данных с консоли """

    # ---------------------------------- ПРЕФИКСЫ ДЛЯ ДОБАВЛЕНИЯ НОВОГО ПОЛЬЗОВАТЕЛЯ --------------------------------- #
    firstname_prefix = 'Введите имя: '
    lastname_prefix = 'Введите фамилию: '
    middlename_prefix = 'Введите отчество: '
    phone_prefix = 'Введите номер телефона: '
    address_prefix = 'Введите адрес: '

    # --------------------------------------- ПРЕФИКСЫ ДЛЯ УДАЛЕНИЯ ПОЛЬЗОВАТЕЛЯ ------------------------------------- #
    delete_firstname_prefix = 'Введите имя пользователя, которого необходимо удалить: '
    delete_lastname_prefix = 'Введите фамилию пользователя, которого необходимо удалить: '
    delete_middlename_prefix = 'Введите отчество пользователя, которого необходимо удалить: '
    delete_phone_prefix = 'Введите телефон пользователя, которого необходимо удалить: '
    delete_address_prefix = 'Введите адрес пользователя, которого необходимо удалить: '

    # ------------------------------------- ПРЕФИКСЫ ДЛЯ РЕДАКТИРОВАНИЯ ПОЛЬЗОВАТЕЛЯ --------------------------------- #
    new_firstname_prefix = 'Введите новое имя: '
    new_lastname_prefix = 'Введите новую фамилию: '
    new_middlename_prefix = 'Введите новое отчество: '
    new_phone_prefix = 'Введите новый телефон: '
    new_address_prefix = 'Введите новый адрес: '

    # ---------------------------------------- ПРЕФИКСЫ ДЛЯ ПОИСКА ПОЛЬЗОВАТЕЛЯ -------------------------------------- #
    search_firstname_prefix = 'Введите имя пользователя, которого необходимо найти: '
    search_lastname_prefix = 'Введите фамилию пользователя, которого необходимо найти: '
    search_middlename_prefix = 'Введите отчество пользователя, которого необходимо найти: '
    search_phone_prefix = 'Введите телефон пользователя, которого необходимо найти: '
    search_address_prefix = 'Введите адрес пользователя, которого необходимо найти: '

    def input_data_for_search(self):
        return {
            'firstname': self.data_input(self.search_firstname_prefix),
            'lastname': self.data_input(self.search_lastname_prefix),
            'middlename': self.data_input(self.search_middlename_prefix),
            'phone': self.data_input(self.search_phone_prefix),
            'address': self.data_input(self.search_address_prefix),
        }

    def input_new_user_data(self):
        return {
            'firstname': self.data_input(self.new_firstname_prefix),
            'lastname': self.data_input(self.new_lastname_prefix),
            'middlename': self.data_input(self.new_middlename_prefix),
            'phone': self.data_input(self.new_phone_prefix),
            'address': self.data_input(self.new_address_prefix),
        }

    def input_data_for_delete(self):
        return {
            'firstname': self.data_input(self.delete_firstname_prefix),
            'lastname': self.data_input(self.delete_lastname_prefix),
            'middlename': self.data_input(self.delete_middlename_prefix),
            'phone': self.data_input(self.delete_phone_prefix),
            'address': self.data_input(self.delete_address_prefix),
        }

    @staticmethod
    def data_input(prefix: str):
        """
        Метод для считывания пользовательских данных с консоли с переданным префиксом

        :param prefix: Префикс
        :return: Введенная пользователем строка
        """
        return input(prefix).title()

    @staticmethod
    def create_data_string(
        firstname: str = None, lastname: str = None, middlename: str = None, phone: str = None, address: str = None,
    ):
        """
        Формирование строки для записи в файл

        :param firstname: Имя пользователя
        :param lastname: Фамилия пользователя
        :param middlename: Отчество пользователя
        :param phone: Телефон пользователя
        :param address: Адрес пользователя
        :return: Строка (Имя Фамилия Отчество\nТелефон\nАдрес)
        """
        return f'{firstname} {lastname} {middlename}\n{phone}\n{address}\n\n'
