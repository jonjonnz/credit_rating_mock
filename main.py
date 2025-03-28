import credit_rating
import json

with open("input.json", "r") as f:
    json_data = f.read()

data = json.loads(json_data)

rating = credit_rating.calculate_credit_rating(data.get("mortgages"))

print(rating)
