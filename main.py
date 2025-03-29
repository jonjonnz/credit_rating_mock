import credit_rating
import json


def main():
    try:
        with open("input.json", "r") as f:
            json_data = f.read()

        data = json.loads(json_data)

        rating = credit_rating.calculate_credit_rating(data.get("mortgages"))

        print(f"Final Credit Rating: {rating}")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()
