"""
Unit tests for calculating credit rating
"""

import unittest
import credit_rating


class TestCreditRating(unittest.TestCase):

    def test_calculate_credit_rating(self):
        data = {
            "mortgages": [
                {
                    "credit_score": 750,
                    "loan_amount": 200000,
                    "property_value": 250000,
                    "annual_income": 60000,
                    "debt_amount": 20000,
                    "loan_type": "fixed",
                    "property_type": "single_family"
                },
                {
                    "credit_score": 680,
                    "loan_amount": 150000,
                    "property_value": 175000,
                    "annual_income": 45000,
                    "debt_amount": 10000,
                    "loan_type": "adjustable",
                    "property_type": "condo"
                }
            ]
        }

        rating = credit_rating.calculate_credit_rating(data.get("mortgages"))
        self.assertEqual(rating, "AAA")

    def test_calculate_individual_risk(self):
        data = {
            "credit_score": 750,
            "loan_amount": 200000,
            "property_value": 250000,
            "annual_income": 60000,
            "debt_amount": 20000,
            "loan_type": "fixed",
            "property_type": "single_family"
        }
        data_risk = credit_rating.calculate_individual_risk(data)
        self.assertEqual(data_risk, -2)


if __name__ == "__main__":
    unittest.main()
