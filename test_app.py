# test_app.py
import unittest
import pandas as pd
from app import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_customers_by_revenue

class TestRevenueCalculations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a simple dataset for testing."""
        data_dict = {
            'order_id': [1, 2, 3, 4],
            'customer_id': [101, 102, 101, 103],
            'order_date': ['2024-01-15', '2024-02-20', '2024-01-25', '2024-03-10'],
            'product_id': [201, 202, 201, 203],
            'product_name': ['Product A', 'Product B', 'Product A', 'Product C'],
            'product_price': [50, 30, 50, 70],
            'quantity': [2, 3, 1, 5]
        }
        cls.data = pd.DataFrame(data_dict)

    def test_compute_monthly_revenue(self):
        result = compute_monthly_revenue(self.data)
        expected = pd.DataFrame({
            'month': ['2024-01', '2024-02', '2024-03'],
            'revenue': [150, 90, 350]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_compute_product_revenue(self):
        result = compute_product_revenue(self.data)
        expected = pd.DataFrame({
            'product_name': ['Product A', 'Product B', 'Product C'],
            'revenue': [150, 90, 350]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_compute_customer_revenue(self):
        result = compute_customer_revenue(self.data)
        expected = pd.DataFrame({
            'customer_id': [101, 102, 103],
            'revenue': [150, 90, 350]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_top_customers_by_revenue(self):
        customer_revenue = compute_customer_revenue(self.data)
        result = top_customers_by_revenue(customer_revenue)
        expected = pd.DataFrame({
            'customer_id': [103, 101, 102],
            'revenue': [350, 150, 90]
        }).reset_index(drop=True)
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
