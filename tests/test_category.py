from unittest import TestCase
from src.category import Category


class TestCategoryClass(TestCase):
    def test_correctness_of_colors_extraction_behavior(self):
        expected_color = "red"
        category = Category("Office", 400, expected_color, [])
        subcategories = [
            Category("Paper", 33.4, expected_color, []),
            Category("Notebook", 44.32, expected_color, []),
            Category("Pens", 10.02, expected_color, []),
        ]
        category.subcategories = subcategories
        category_color, subcategories_colors = category.extract_colors()
        expected_colors_list = [expected_color] * len(subcategories_colors)
        self.assertEqual(
            expected_colors_list,
            subcategories_colors,
            f"Color extraction returns unexpected values for subcategories: {subcategories_colors}!\n"
            + f"Expected values: {expected_colors_list}!",
        )
        self.assertEqual(
            category_color,
            expected_color,
            f"Color extraction returns incorrect color for category: {category_color}!\nExpected value: {expected_color}",
        )

    def test_correctness_of_profits_extraction_behavior(self):
        expected_subcategories_profits = [33.4, 44.32, 10.02]
        expected_category_profit = sum(expected_subcategories_profits)
        category = Category("Office", expected_category_profit, "red", [])
        subcategories = [
            Category("Paper", expected_subcategories_profits[0], "red", []),
            Category("Notebook", expected_subcategories_profits[1], "red", []),
            Category("Pens", expected_subcategories_profits[2], "red", []),
        ]
        category.subcategories = subcategories
        category_profit, subcategories_profits = category.extract_profits()
        self.assertEqual(
            subcategories_profits,
            expected_subcategories_profits,
            f"Profit extraction returns unexpected values for subcategories: {subcategories_profits}!\n"
            + f"Expected values: {expected_subcategories_profits}!",
        )
        self.assertEqual(
            category_profit,
            expected_category_profit,
            f"Profit extraction returns incorrect profit for category: {category_profit}!\nExpected value: {expected_category_profit}",
        )
