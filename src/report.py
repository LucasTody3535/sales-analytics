from fpdf import FPDF


class Report:
    def __init__(self, page_format: str, orientation: str):
        self.__pdf = FPDF(format=page_format, orientation=orientation)

    def init(self, title: str):
        margin = 5
        self.add_page()
        self.__pdf.set_margin(margin)

        font_data = {"family": "Times", "style": "B", "size": 20}
        font_coord = {"x": self.dims()["left_m"], "y": 10}
        self.add_text(title, font_coord, font_data)

    def gen(self, filename: str):
        self.__pdf.output(filename)

    def dims(self) -> dict[str, float]:
        pdf = self.__pdf
        return {
            "height": pdf.eph,
            "width": pdf.epw,
            "left_m": pdf.l_margin,
            "right_m": pdf.r_margin,
            "top_m": pdf.t_margin,
            "bottom_m": pdf.b_margin,
        }

    def add_image(self, path: str, dims: dict[str, float], coord: dict[str, float]):
        self.__pdf.image(
            path, h=dims["height"], w=dims["width"], y=coord["y"], x=coord["x"]
        )

    def add_text(
        self,
        text: str,
        coord: dict[str, float],
        font_data: dict[str, str],
        multiline=False,
    ):
        pdf = self.__pdf
        pdf.set_font(font_data["family"], font_data["style"], font_data["size"])
        if multiline:
            width = self.dims()["width"]
            self.__pdf.set_y(coord["y"])
            self.__pdf.set_x(coord["x"])
            self.__pdf.multi_cell(w=width, h=5, text=text, align="L")
            return
        pdf.text(coord["x"], coord["y"], text)

    def add_page(self):
        self.__pdf.add_page()
