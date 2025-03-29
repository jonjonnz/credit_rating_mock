"""
Business logic for calculating credit rating
"""


def calculate_credit_rating(mortgages) -> str:
    """
    Implement the credit rating calculation logic for residential mortgage-backed securities (RMBS)
    :param mortgages: List of mortgages
    :return: Credit rating (AAA or BBB or C)
    """
    if len(mortgages) == 0:
        return "No mortgages available"

    risk = 0
    total_credit_score = 0
    for data in mortgages:
        data_risk = calculate_individual_risk(data)
        print(f"Risk for the Following mortgage{data} is: {data_risk}")
        risk += data_risk
        total_credit_score += data.get("credit_score")

    acs_risk = average_credit_score_risk(total_credit_score, len(mortgages))
    risk += acs_risk
    if risk <= 2:
        return "AAA"
    elif risk <= 5:
        return "BBB"

    return "C"


def calculate_ltv_risk(loan_amount: float, property_value: float) -> int:
    """
    LTV is the ratio of the loan amount to the property value. Higher LTV ratios are riskier.
    :param loan_amount: The total loan amount of the mortgage.
    :param property_value: The value of the mortgaged property.
    :return: risk score based on LTV
    """
    ratio = loan_amount / property_value

    if ratio > 0.9:
        return 2
    elif ratio > 0.8:
        return 1

    return 0


def calculate_dti_risk(debt_amount: float, annual_income: float) -> int:
    """
    DTI is the ratio of the borrower’s existing debt to their annual income. Higher DTI ratios are riskier.
    :param debt_amount: The borrower’s existing debt amount.
    :param annual_income: The borrower’s annual income.
    :return: risk score based on DTI
    """
    ratio = debt_amount / annual_income

    if ratio > 0.5:
        return 2
    elif ratio > 0.4:
        return 1

    return 0


def process_credit_score_risk(credit_score: int) -> int:
    """
    The credit score indicates the borrower's ability to repay the loan. Higher credit scores are less risky.
    :param credit_score: (between 300 and 850) The credit score of the borrower.
    :return: risk score based on credit
    """
    if credit_score >= 700:
        return -1
    elif credit_score < 650:
        return 1

    return 0


def process_loan_type_risk(loan_type: str) -> int:
    """
    The type of mortgage loan also affects the risk.
    :param loan_type: ("fixed" or "adjustable"): The type of mortgage loan.
    :return: risk score based on loan type
    """
    if loan_type == "fixed":
        return -1
    elif loan_type == "adjustable":
        return 1

    return 0


def process_property_type_risk(property_type: str) -> int:
    """
    The type of property also impacts the risk.
    :param property_type: ("single_family" or "condo"): The type of property.
    :return: risk score based on property type
    """
    if property_type == "single_family":
        return 0
    elif property_type == "condo":
        return 1

    return 0


def average_credit_score_risk(total_credit: float, num_of_mortgages: int) -> int:
    """
    Once the individual risk scores are calculated for each mortgage, adjust the final score based on the average credit score
    :param total_credit: Sum of all the credit scores available
    :param num_of_mortgages: Number of mortgages
    :return: risk score based on average credit score
    """
    avg = total_credit / num_of_mortgages

    if avg >= 700:
        return -1
    elif avg < 650:
        return 1

    return 0


def calculate_individual_risk(data) -> int:
    """
    Calculate all the risk scores for each individual mortgage
    :param data: json of mortgage data
    :return: individual risk score based on all calculations
    """
    risk = 0

    ltv = calculate_ltv_risk(data.get("loan_amount"), data.get("property_value"))
    risk += ltv

    dti = calculate_dti_risk(data.get("debt_amount"), data.get("annual_income"))
    risk += dti

    credit = process_credit_score_risk(data.get("credit_score"))
    risk += credit

    l_type = process_loan_type_risk(data.get("loan_type"))
    risk += l_type

    p_type = process_property_type_risk(data.get("property_type"))
    risk += p_type

    return risk
