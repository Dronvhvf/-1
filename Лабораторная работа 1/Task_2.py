from abc import ABC, abstractmethod

class Tree(ABC):
    """Абстрактный класс для описания дерева."""

    def __init__(self, species: str, height: float) -> None:
        """
        Инициализация атрибутов дерева.

        :param species: Вид дерева. Не может быть пустым.
        :param height: Высота дерева (в метрах). Должна быть больше 0.
        :raises ValueError: Если параметры не соответствуют ограничениям.

        >>> tree = Oak(species="Дуб", height=5)
        """
        if not species:
            raise ValueError("Вид дерева не может быть пустым.")
        if height <= 0:
            raise ValueError("Высота дерева должна быть больше 0.")

        self.species = species
        self.height = height

    @abstractmethod
    def grow(self, years: int) -> None:
        """Увеличить рост дерева."""
        pass

    @abstractmethod
    def photosynthesize(self) -> None:
        """Дерево выполняет фотосинтез."""
        pass

class Oak(Tree):
    """Конкретный класс для дерева вида дуб."""

    def grow(self, years: int) -> None:
        """
        Реализация метода роста дерева.

        >>> tree = Oak(species="Дуб", height=5)
        >>> tree.grow(10)
        Дуб вырос за 10 лет на 5.0 м.
        """
        print(f"Дуб вырос за {years} лет на {years * 0.5} м.")

    def photosynthesize(self) -> None:
        """
        Реализация метода фотосинтеза.

        >>> tree = Oak(species="Дуб", height=5)
        >>> tree.photosynthesize()
        Дуб Дуб выполняет фотосинтез.
        """
        print(f"Дуб {self.species} выполняет фотосинтез.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()