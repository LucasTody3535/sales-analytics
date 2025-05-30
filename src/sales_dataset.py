import csv

from src.sales_dataset_column import SalesDatasetColumn

class SalesDataset:
    """
        Represents a sales dataset, responsible for extracting the values
        in the rows for further processing
    """
    def __init__(self, filename: str):
        self.set_filename(filename)
        self.set_columns({
            "order_id": SalesDatasetColumn("Order ID"),
            "amount": SalesDatasetColumn("Amount"),
            "profit": SalesDatasetColumn("Profit"),
            "quantity": SalesDatasetColumn("Quantity"),
            "category": SalesDatasetColumn("Category"),
            "subcategory": SalesDatasetColumn("Sub-Category"),
            "payment_mode": SalesDatasetColumn("PaymentMode"),
            "order_date": SalesDatasetColumn("Order Date"),
            "customer_name": SalesDatasetColumn("Customer Name"),
            "state": SalesDatasetColumn("State"),
            "city": SalesDatasetColumn("City"),
            "year_month": SalesDatasetColumn("Year-Month")
        })

    def set_filename(self, filename: str):
        self.__filename = filename

    def get_filename(self) -> str:
        return self.__filename

    def set_columns(self, columns: [str, SalesDatasetColumn]):
        self.__columns = columns

    def get_columns(self) -> dict[str, SalesDatasetColumn]:
        return self.__columns

    def extract_rows(self):
        columns = self.get_columns()
        filename = self.get_filename()
        with open(filename, 'r', newline='', encoding='UTF-8') as sales:
            reader = csv.reader(sales, delimiter=',', quotechar=' ')
            for row in reader:
                columns["order_id"].append_cell_value(row[0])
                columns["amount"].append_cell_value(row[1])
                columns["profit"].append_cell_value(row[2])
                columns["quantity"].append_cell_value(row[3])
                columns["category"].append_cell_value(row[4])
                columns["subcategory"].append_cell_value(row[5])
                columns["payment_mode"].append_cell_value(row[6])
                columns["order_date"].append_cell_value(row[7])
                columns["customer_name"].append_cell_value(row[8])
                columns["state"].append_cell_value(row[9])
                columns["city"].append_cell_value(row[10])
                columns["year_month"].append_cell_value(row[11])
