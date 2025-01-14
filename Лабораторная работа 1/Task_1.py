from abc import ABC, abstractmethod

class Car(ABC):
    """Абстрактный класс для описания автомобиля."""

    def __init__(self, brand: str, fuel_capacity: float) -> None:
        """
        Инициализация атрибутов автомобиля.

        :param brand: Название марки автомобиля. Не может быть пустым.
        :param fuel_capacity: Емкость топливного бака (в литрах). Должна быть больше 0.
        :raises ValueError: Если параметры не соответствуют ограничениям.

        >>> car = Sedan(brand="Toyota", fuel_capacity=50)
        """
        if not brand:
            raise ValueError("Марка автомобиля не может быть пустой.")
        if fuel_capacity <= 0:
            raise ValueError("Емкость бака должна быть больше 0.")

        self.brand = brand
        self.fuel_capacity = fuel_capacity

    @abstractmethod
    def drive(self, distance: float) -> None:
        """Вести автомобиль."""
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        """Заправить автомобиль."""
        pass

class Sedan(Car):
    """Конкретный класс автомобиля типа седан."""

    def drive(self, distance: float) -> None:
        """
        Реализация метода для движения автомобиля.

        >>> car = Sedan(brand="Toyota", fuel_capacity=50)
        >>> car.drive(100)
        Автомобиль Toyota проехал 100 км.
        """
        print(f"Автомобиль {self.brand} проехал {distance} км.")

    def refuel(self, fuel: float) -> None:
        """
        Реализация метода для заправки автомобиля.

        >>> car = Sedan(brand="Toyota", fuel_capacity=50)
        >>> car.refuel(20)
        Заправлено 20 литров топлива для Toyota.
        """
        print(f"Заправлено {fuel} литров топлива для {self.brand}.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()