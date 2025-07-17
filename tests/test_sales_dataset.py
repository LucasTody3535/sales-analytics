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
