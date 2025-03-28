import json


def calculate_credit_rating(mortgages) -> str:
    rating = 0
    for data in mortgages:
        data_rating = calculate_individual_rating(data)
        rating += data_rating

    if rating <= 2:
        return "AAA"
    elif rating <= 5:
        return "BBB"

    return "C"


def calculate_ltv_risk(loan_amount: float, property_value: float) -> int:
    ratio = loan_amount / property_value

    if ratio > 0.9:
        return 2
    elif ratio > 0.8:
        return 1

    return 0


def calculate_dti_risk(debt_amount: float, annual_income: float) -> int:
    ratio = debt_amount / annual_income

    if ratio > 0.5:
        return 2
    elif ratio > 0.4:
        return 1

    return 0


def process_credit_score_risk(credit_score: int) -> int:
    if credit_score >= 700:
        return -1
    elif credit_score < 650:
        return 1

    return 0


def process_loan_type_risk(loan_type: str) -> int:
    if loan_type == "fixed":
        return -1
    elif loan_type == "adjustable":
        return 1

    return 0


def process_property_type_risk(property_type: str) -> int:
    if property_type == "single_family":
        return 0
    elif property_type == "condo":
        return 1

    return 0


def average_credit_score_risk(total_credit: float, num_of_mortgages: int) -> int:
    avg = total_credit / num_of_mortgages

    if avg >= 700:
        return -1
    elif avg < 650:
        return 1

    return 0


def calculate_individual_rating(data) -> int:
    pass
