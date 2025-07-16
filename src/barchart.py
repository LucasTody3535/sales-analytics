import matplotlib.pyplot as plt


class BarChart:
    def __init__(self):
        self.__data = None
        self.__labels = None
        self.__colors = None
        self.__chart_fig, self.__chart_ax = plt.subplots()

    @property
    def data(self) -> list[float]:
        return self.__data

    @property
    def labels(self) -> list[str]:
        return self.__labels

    @property
    def colors(self) -> list[str]:
        return self.__colors

    @data.setter
    def data(self, data: list[float]):
        self.__data = data

    @labels.setter
    def labels(self, labels: list[str]):
        self.__labels = labels

    @colors.setter
    def colors(self, colors: list[str]):
        self.__colors = colors

    def __format_legend_labels(self) -> list[str]:
        formmated_data = []
        counter = 0
        for idx, data in enumerate(self.data):
            formmated_data.append("")
            counter = 0
            for char in str(int(data)):
                if counter == 3:
                    counter = 0
                    formmated_data[idx] += "."
                formmated_data[idx] += char
                counter += 1
            formmated_data[idx] = f"${formmated_data[idx]}"
        return formmated_data

    def gen_chart(self, title: str, labels_rotation: float = 0):
        formmated_data = self.__format_legend_labels()
        self.__chart_ax.bar(
            self.labels,
            self.data,
            label=formmated_data,
            color=self.colors,
        )
        plt.xticks(rotation=labels_rotation)
        self.__chart_ax.legend(title=title)

    def show(self):
        plt.show()

    def save_as_image(self, path: str):
        self.__chart_fig.savefig(path, dpi=500, bbox_inches="tight")

    def clear(self):
        self.__chart_ax.clear()
