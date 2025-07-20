from unittest import TestCase
from src.sales_dataset import SalesDataset


class TestSalesDatasetClass(TestCase):
    def test_extraction_behavior(self):
        sales = SalesDataset("tests/data/dataset.csv")
        expected_length = 15
        sales.extract_rows()
        self.assertEqual(
            len(sales.columns["order_id"].cells),
            expected_length,
            "Invalid Order ID column length!",
        )
        self.assertEqual(
            len(sales.columns["amount"].cells),
            expected_length,
            "Invalid Amount column length!",
        )
        self.assertEqual(
            len(sales.columns["profit"].cells),
            expected_length,
            "Invalid Profit column length!",
        )
        self.assertEqual(
            len(sales.columns["quantity"].cells),
            expected_length,
            "Invalid Quantity column length!",
        )
        self.assertEqual(
            len(sales.columns["category"].cells),
            expected_length,
            "Invalid Category column length!",
        )
        self.assertEqual(
            len(sales.columns["subcategory"].cells),
            expected_length,
            "Invalid Sub-Category column length!",
        )
        self.assertEqual(
            len(sales.columns["payment_mode"].cells),
            expected_length,
            "Invalid PaymentMode column length!",
        )
        self.assertEqual(
            len(sales.columns["order_date"].cells),
            expected_length,
            "Invalid Order Date column length!",
        )
        self.assertEqual(
            len(sales.columns["customer_name"].cells),
            expected_length,
            "Invalid CustomerName column length!",
        )
        self.assertEqual(
            len(sales.columns["state"].cells),
            expected_length,
            "Invalid State column length!",
        )
        self.assertEqual(
            len(sales.columns["city"].cells),
            expected_length,
            "Invalid City column length!",
        )
        self.assertEqual(
            len(sales.columns["year_month"].cells),
            expected_length,
            "Invalid Year-Month column length!",
        )

    def test_categories_list_length_when_extracting_from_rows(self):
        sales = SalesDataset("tests/data/dataset.csv")
        expect_quantity = 3
        columns = sales.columns["category"]
        sales.extract_rows()
        categories = sales.extract_categories_from_rows(columns)
        actual_size = len(categories)
        self.assertEqual(
            actual_size,
            expect_quantity,
            f"Categories list has unexpected quantity: {actual_size}\n"
            + "Expected quantity: {expect_quantity}",
        )

    def test_subcategories_list_length_when_extracting_from_rows(self):
        sales = SalesDataset("tests/data/dataset.csv")
        expect_quantity = 8
        columns = sales.columns["subcategory"]
        sales.extract_rows()
        categories = sales.extract_categories_from_rows(columns)
        actual_size = len(categories)
        self.assertEqual(
            actual_size,
            expect_quantity,
            f"Categories list has unexpected quantity: {actual_size}\n"
            + "Expected quantity: {expect_quantity}",
        )
