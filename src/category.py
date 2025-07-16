from typing import Self


class Category:
    """
    This class represents a Category of the 'Category' column of the
    sales dataset
    """

    def __init__(self, name: str, profit: float, color: str, subcategories: list[Self]):
        self.__name = name
        self.__profit = profit
        self.__color = color
        self.__subcategories = subcategories

    @property
    def name(self) -> str:
        return self.__name

    @property
    def profit(self) -> float:
        return self.__profit

    @property
    def color(self) -> str:
        return self.__color

    @property
    def subcategories(self) -> list[Self]:
        return self.__subcategories

    @name.setter
    def name(self, name: str):
        self.__name = name

    @profit.setter
    def profit(self, profit: float):
        self.__profit = profit

    @color.setter
    def color(self, color: str):
        self.__color = color

    @subcategories.setter
    def subcategories(self, subcategories: list[Self]):
        self.__subcategories = subcategories

    def extract_colors(self) -> tuple[str, list[str]]:
        subcat_colors = []
        for subcategory in self.subcategories:
            subcat_colors.append(subcategory.color)
        return (self.color, subcat_colors)

    def extract_profits(self) -> tuple[float, list[float]]:
        subcat_profits = []
        for subcategory in self.subcategories:
            subcat_profits.append(subcategory.profit)
        return (self.profit, subcat_profits)
