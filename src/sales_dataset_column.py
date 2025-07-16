class SalesDatasetColumn:
    """
    Represents a column in the sales dataset, composed by an identifier related
    to the column and the corresponding cells
    """

    def __init__(self, name: str):
        self.__name = name
        self.__cells = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def cells(self) -> list[str]:
        return self.__cells.copy()[1:]

    @name.setter
    def name(self, name: str):
        self.__name = name

    @cells.setter
    def cells(self, cells: list[str]):
        self.__cells = cells

    def append_cell_value(self, value: str):
        self.__cells.append(value)
