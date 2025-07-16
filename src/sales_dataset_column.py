class SalesDatasetColumn:
    """
    Represents a column in the sales dataset, composed by an identifier related
    to the column and the corresponding cells
    """

    def __init__(self, name: str):
        self.__name = name
        self.__cells = []

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_cells(self, cells: list[str]):
        self.__cells = cells

    def get_cells(self) -> list[str]:
        return self.__cells.copy()[1:]

    def append_cell_value(self, value: str):
        self.__cells.append(value)
