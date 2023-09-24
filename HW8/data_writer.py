from data_create import DataCreate


class DataWriter:
    """ Класс для записи данных в файл """

    @staticmethod
    def write_data(file_name: str, text: str, write_mode: str = 'a'):
        """
        Запись данных в файл

        :param file_name: Наименование файла, в который будет производиться запись
        :param text: Записываемый в файл текст
        :param write_mode: Режим записи ('a' - запись без удаления содержимого, 'w' - очистка файла перед записью)
        """
        with open(file_name, write_mode, encoding='utf-8') as file:
            file.write(text)
        print('\n\n')

    def edit_data(self, file_name: str, user_for_search: dict[str]):
        """
        Редактирование данных пользователя

        :param file_name: Наименование файла
        :param user_for_search: Данные пользователя, для которого изменяем данные
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
                user_for_search['city'].lower() in ' '.join(x.split()[4:]).lower(),
                users
            )
        )

        if not result:
            print('\nПользователь с указанными данными не был найден. Ни один из пользователей не будет изменен\n')
            return

        if len(result) > 1:
            print(f'\nБыло найдено больше 1 пользователя с указанными данными. '
                  f'Вы уверены, что хотите отредактировать всех, тем самым удалив дубликаты?\n')
            answer = input('Введите ваш вариант (y / n): ')
            match answer:
                case 'y':
                    pass

                case 'n':
                    print('\nНи один из пользователей не будет удален\n')
                    return
                case _:
                    print('\nНи один из пользователей не будет удален\n')
                    return

        new_user_data = DataCreate().input_new_user_data()
        users = [x for x in users if x not in result]
        data = ''
        for item in users:
            data += DataCreate.create_data_string(
                firstname=item.split()[0],
                lastname=item.split()[1],
                middlename=item.split()[2],
                phone=item.split()[3],
                city=' '.join(item.split()[4:]),
            )
        data += DataCreate.create_data_string(
            firstname=new_user_data['firstname'],
            lastname=new_user_data['lastname'],
            middlename=new_user_data['middlename'],
            phone=new_user_data['phone'],
            city=new_user_data['city'],
        )
        print(f'\nБудет изменен пользователь:', *result)
        self.write_data(file_name=file_name, text=data, write_mode='w')

    def delete_data(self, file_name: str, user_data_for_deleting: dict[str]):
        """
        Удаление пользовательских данных

        :param file_name:
        :param user_data_for_deleting: Данные пользователя, которого необходимо удалить
        """
        with open(file_name, 'r', encoding='utf-8') as file:
            users = [x.replace('\n', ' ') for x in file.read().strip().split('\n\n')]

        result = list(
            filter(
                lambda x:
                user_data_for_deleting['firstname'].lower() in x.split()[0].lower() and
                user_data_for_deleting['lastname'].lower() in x.split()[1].lower() and
                user_data_for_deleting['middlename'].lower() in x.split()[2].lower() and
                user_data_for_deleting['phone'].lower() in x.split()[3].lower() and
                user_data_for_deleting['city'].lower() in ' '.join(x.split()[4:]).lower(),
                users
            )
        )
        if not result:
            print('Пользователь с указанными данными не был найден. Ни один из пользователей не будет удален')
            return

        if len(result) > 1:
            print(f'Было найдено больше 1 пользователя с указанными данными. Вы уверены, что хотите удалить всех?')
            answer = input('Введите ваш вариант (y / n): ')
            match answer:
                case 'y':
                    pass

                case 'n':
                    print('Ни один из пользователей не будет удален')
                    return
                case _:
                    print('Ни один из пользователей не будет удален')
                    return

        data = ''
        users = [x for x in users if x not in result]
        for item in users:
            data += DataCreate.create_data_string(
                firstname=item.split()[0],
                lastname=item.split()[1],
                middlename=item.split()[2],
                phone=item.split()[3],
                city=' '.join(item.split()[4:]),
            )
        print(f'\nБудет удален пользователь:', *result, sep='\n')
        self.write_data(file_name=file_name, text=data, write_mode='w')
