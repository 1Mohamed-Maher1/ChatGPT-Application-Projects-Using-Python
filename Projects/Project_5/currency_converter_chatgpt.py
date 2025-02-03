import requests

def get_currency_input(prompt):
    """Prompts user for currency input and returns the input."""
    return input(prompt).strip().upper()

def get_amount():
    """Prompts user for the amount and validates it as a positive float."""
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("The amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("The amount must be a numeric value!")

def convert_currency(init_currency, target_currency, amount, api_key):
    """Sends a conversion request to the API and returns the converted amount."""
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Sorry, there was a problem. Please try again later.")
        return None
    
    return response.json().get('result')

def main():
    # Get user input for currencies and amount
    init_currency = get_currency_input("Enter an initial currency (e.g., USD): ")
    target_currency = get_currency_input("Enter a target currency (e.g., EUR): ")
    amount = get_amount()

    # Replace {API-KEY} with your actual API key
    api_key = "{API-KEY}"  

    # Perform currency conversion
    converted_amount = convert_currency(init_currency, target_currency, amount, api_key)
    
    if converted_amount is not None:
        print(f"{amount} {init_currency} = {converted_amount} {target_currency}")

# Run the program
main()
