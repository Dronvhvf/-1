from abc import ABC, abstractmethod

class SocialNetwork(ABC):
    """Абстрактный класс для описания социальной сети."""

    def __init__(self, name: str, user_count: int) -> None:
        """
        Инициализация атрибутов социальной сети.

        :param name: Название социальной сети. Не может быть пустым.
        :param user_count: Количество пользователей. Должно быть больше или равно 0.
        :raises ValueError: Если параметры не соответствуют ограничениям.

        >>> network = Facebook(name="Facebook", user_count=2000000)
        """
        if not name:
            raise ValueError("Название социальной сети не может быть пустым.")
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.name = name
        self.user_count = user_count

    @abstractmethod
    def register_user(self, username: str) -> None:
        """Зарегистрировать нового пользователя."""
        pass

    @abstractmethod
    def post_content(self, content: str) -> None:
        """Опубликовать новый контент."""
        pass

class Facebook(SocialNetwork):
    """Конкретный класс для социальной сети Facebook."""

    def register_user(self, username: str) -> None:
        """
        Реализация метода регистрации нового пользователя.

        >>> network = Facebook(name="Facebook", user_count=2000000)
        >>> network.register_user("JohnDoe")
        Пользователь JohnDoe зарегистрирован в Facebook.
        """
        print(f"Пользователь {username} зарегистрирован в {self.name}.")

    def post_content(self, content: str) -> None:
        """
        Реализация метода публикации контента.

        >>> network = Facebook(name="Facebook", user_count=2000000)
        >>> network.post_content("Hello, world!")
        Опубликовано: Hello, world!
        """
        print(f"Опубликовано: {content}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()







