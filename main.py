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

        font_data = { "family": "Times", "style": "", "size": 12 }
        font_coord = { "x": report.dims()["left_m"], "y": 15 }
        report.add_text(content, font_coord, font_data, multiline=True)

    categories = sales.extract_categories_from_rows(sales.get_columns()["category"])
    subcategories = sales.extract_categories_from_rows(sales.get_columns()["subcategory"])
    sales.group_categories_and_subcategories(categories, subcategories)
    sales.set_colors(categories)

    bar_chart = BarChart()

    categories_names = []
    categories_colors = []
    categories_profits = []
    for cat in categories:
        cat_color, subcat_colors = cat.extract_colors()
        cat_profit, subcat_profit = cat.extract_profits()
        categories_names.append(cat.get_name())
        categories_colors.append(f"tab:{cat_color}")
        categories_profits.append(cat_profit)

    bar_chart.set_labels(categories_names)
    bar_chart.set_data(categories_profits)
    bar_chart.set_colors(categories_colors)
    bar_chart.gen_chart(title="Total profit")

    report.gen("out/Report.pdf")
