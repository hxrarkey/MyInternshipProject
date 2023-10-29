import requests


# Step 1: Fetch real-time exchange rate data from an API
def get_exchange_rates(base_currency):
    # Replace 'YOUR_API_KEY' with your actual API key or endpoint
    api_url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return data['rates']
    else:
        print("Failed to fetch exchange rate data.")
        return None


# Step 2: Prompt the user for input
def get_user_input():
    while True:
        try:
            amount = float(input("Enter the amount in your base currency: "))
            base_currency = input("Enter the base currency (e.g., USD, EUR, INR): ").upper()
            target_currency = input("Enter the target currency (e.g., USD, EUR, INR): ").upper()
            return amount, base_currency, target_currency
        except ValueError:
            print("Invalid input. Please enter a numeric amount.")
        except KeyError:
            print("Invalid currency code. Please use a valid three-letter currency code.")


# Step 3: Perform the currency conversion and display the result
def convert_currency(amount, base_currency, target_currency, exchange_rates):
    if target_currency not in exchange_rates:
        print("Unsupported target currency.")
    else:
        exchange_rate = exchange_rates[target_currency]
        converted_amount = amount * exchange_rate
        print(f"{amount} {base_currency} is equal to {converted_amount} {target_currency}")
        print(f"Exchange rate: 1 {base_currency} = {exchange_rate} {target_currency}")


# Step 4: Main program
if __name__ == "__main__":
    print("Welcome to the Currency Converter!")

    base_currency = input("Enter the base currency (e.g., USD, EUR, INR): ").upper()
    exchange_rates = get_exchange_rates(base_currency)

    if exchange_rates:
        amount, base_currency, target_currency = get_user_input()
        convert_currency(amount, base_currency, target_currency, exchange_rates)
