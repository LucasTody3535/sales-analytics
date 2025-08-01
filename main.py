from os import remove, getcwd, sep
from webbrowser import open_new_tab

from src.sales_dataset import SalesDataset
from src.report import Report
from src.barchart import BarChart

if __name__ == "__main__":
    sales = SalesDataset("data/Sales Dataset.csv")
    report = Report("A4", "Portrait")

    sales.extract_rows()
    report.init("Sales Report for the XPTO Company")

    with open("templates/greetings.txt", encoding="utf-8") as greetings:
        content = greetings.read()
        content = content.replace("<t1>", "John Doe")
        content = content.replace("<t2>", "XPTO")

        font_data = {"family": "Times", "style": "", "size": 12}
        font_coord = {"x": report.dims()["left_m"], "y": 15}
        report.add_text(content, font_coord, font_data, multiline=True)

    categories = sales.extract_categories_from_rows(sales.columns["category"])
    subcategories = sales.extract_categories_from_rows(sales.columns["subcategory"])
    sales.group_categories_and_subcategories(categories, subcategories)
    sales.set_colors(categories)

    bar_chart = BarChart()

    categories_names = []
    categories_colors = []
    categories_profits = []
    subcategories_names = []
    subcategories_colors = []
    subcategories_profits = []
    for cat in categories:
        cat_color, subcat_colors = cat.extract_colors()
        cat_profit, subcat_profit = cat.extract_profits()
        categories_names.append(cat.name)
        categories_colors.append(f"tab:{cat_color}")
        categories_profits.append(cat_profit)
        for subcat in cat.subcategories:
            subcategories_names.append(subcat.name)
        for color in subcat_colors:
            subcategories_colors.append(f"tab:{color}")
        subcategories_profits.extend(subcat_profit)

    bar_chart.labels = categories_names
    bar_chart.data = categories_profits
    bar_chart.colors = categories_colors
    bar_chart.gen_chart(title="Total profit")

    categories_chart_image_path = "./out/categories_profit.png"
    most_profitable_category_idx = categories_profits.index(max(categories_profits))
    least_profitable_category_idx = categories_profits.index(min(categories_profits))

    with open("templates/categories.txt", encoding="utf-8") as categories_intro:
        content = categories_intro.read()
        content = content.replace(
            "<c1>", categories_names[most_profitable_category_idx].lower()
        )
        content = content.replace(
            "<c2>", categories_names[least_profitable_category_idx].lower()
        )

        font_data = {"family": "Times", "style": "", "size": 12}
        font_coord = {"x": report.dims()["left_m"], "y": 30}
        report.add_text(content, font_coord, font_data, multiline=True)

    bar_chart.save_as_image(categories_chart_image_path)
    img_dims = {"height": 110, "width": 180}
    img_coord = {"x": report.dims()["left_m"] + 10, "y": 40}
    report.add_image(categories_chart_image_path, img_dims, img_coord)

    bar_chart.clear()
    bar_chart.labels = subcategories_names
    bar_chart.data = subcategories_profits
    bar_chart.colors = subcategories_colors
    bar_chart.gen_chart(title="Total profit", labels_rotation=90)

    with open("templates/subcategories.txt", encoding="utf-8") as subcategories_intro:
        content = subcategories_intro.read()

        font_data = {"family": "Times", "style": "", "size": 12}
        font_coord = {"x": report.dims()["left_m"], "y": 155}
        report.add_text(content, font_coord, font_data, multiline=True)

    subcategories_chart_image_path = "./out/subcategories_profit.png"
    bar_chart.save_as_image(subcategories_chart_image_path)
    img_dims = {"height": 130, "width": 180}
    img_coord = {"x": report.dims()["left_m"] + 10, "y": 167}
    report.add_image(subcategories_chart_image_path, img_dims, img_coord)

    remove(categories_chart_image_path)
    remove(subcategories_chart_image_path)

    open_new_tab(f"{getcwd()}{sep}out{sep}Report.pdf")

    report.gen("out/Report.pdf")
