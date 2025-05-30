from typing import Self

class Category:
    """
        This class represents a Category of the 'Category' column of the
        sales dataset
    """
    def __init__(self, name: str, profit: float, color: str, subcategories: list[Self]):
        self.set_name(name)
        self.set_profit(profit)
        self.set_color(color)
        self.set_subcategories(subcategories)

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_profit(self, profit: float):
        self.__profit = profit

    def get_profit(self) -> float:
        return self.__profit

    def set_color(self, color: str):
        self.__color = color

    def get_color(self) -> str:
        return self.__color

    def set_subcategories(self, subcategories: list[Self]):
        self.__subcategories = subcategories

    def get_subcategories(self) -> list[Self]:
        return self.__subcategories
