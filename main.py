from src.sales_dataset import SalesDataset
from src.report import Report

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

    report.gen("out/Report.pdf")
