class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'  # Уровень доступа по умолчанию для обычных сотрудников

    # Геттер для ID
    @property
    def user_id(self):
        return self.__user_id

    # Геттер для имени
    @property
    def name(self):
        return self.__name

    # Геттер для уровня доступа
    @property
    def access_level(self):
        return self.__access_level

    # Устанавливаем имя
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("Name must be a string.")

    def __str__(self):
        return f"User(ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'  # Уровень доступа для администраторов
        self.__user_list = []

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User) and user not in self.__user_list:
            self.__user_list.append(user)
        else:
            raise ValueError("Invalid user or user already exists.")

    # Метод для удаления пользователя
    def remove_user(self, user):
        if user in self.__user_list:
            self.__user_list.remove(user)
        else:
            raise ValueError("User not found.")

    # Геттер для списка пользователей
    @property
    def user_list(self):
        return self.__user_list

    def __str__(self):
        return f"Admin(ID: {self.user_id}, Name: {self.name}, Access Level: {self.access_level}, Managed Users: {len(self.__user_list)})"


# Пример использования
if __name__ == "__main__":
    # Создаем пользователей
    user1 = User(user_id=1, name="Alice")
    user2 = User(user_id=2, name="Bob")

    # Создаем администратора
    admin = Admin(user_id=100, name="Charlie")

    # Добавляем пользователей через администратора
    admin.add_user(user1)
    admin.add_user(user2)

    print(admin)  # Показывает информацию об администраторе и управляемых пользователях

    # Удаляем одного пользователя
    admin.remove_user(user1)

    print(admin)  # Обновленная информация об администраторе



