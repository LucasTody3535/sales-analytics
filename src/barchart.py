import matplotlib.pyplot as plt

class BarChart:
    def __init__(self):
        self.__data= None
        self.__labels = None
        self.__colors = None
        self.__chart_fig, self.__chart_ax = plt.subplots()

    def set_data(self, data: list[float]):
        self.__data = data

    def get_data(self) -> list[float]:
        return self.__data

    def set_labels(self, labels: list[str]):
        self.__labels = labels

    def get_labels(self) -> list[str]:
        return self.__labels

    def set_colors(self, colors: list[str]):
        self.__colors = colors

    def get_colors(self) -> list[str]:
        return self.__colors

    def __format_legend_labels(self) -> list[str]:
        formmated_data = []
        counter = 0
        for idx, data in enumerate(self.get_data()):
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

    def gen_chart(self, title: str):
        formmated_data = self.__format_legend_labels()
        self.__chart_ax.bar(self.get_labels(), self.get_data(), label=formmated_data, color=self.get_colors())
        self.__chart_ax.legend(title=title)

    def show(self):
        plt.show()

    def save_as_image(self, path: str):
        self.__chart_fig.savefig(path)

    def clear(self):
        self.__chart_ax.clear()
