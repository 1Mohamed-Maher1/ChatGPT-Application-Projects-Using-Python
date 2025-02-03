import requests

init_currency = input("Enter an intial currency: ")
target_currency = input("Enter an intial currency: ")

while True:
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("The amount must be a numberic value!")
        continue
    if amount == 0:
        print("The amount must be greater than 0")
        continue
    else:
        break

url = "https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "{API-KEY}"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if(status_code != 200):
    print("Sorry, there was a problem. Please try again later.")
    quit()

result = response.json()
converted_amount = result['result']
print(f"{amount} {init_currency} = {converted_amount} {target_currency}")
###########################################################################
# import requests

# # Input for initial and target currencies
# init_currency = input("Enter an initial currency (e.g., EGP): ")
# target_currency = input("Enter a target currency (e.g., USD): ")

# # Prompt for the amount and validate input
# while True:
#     try:
#         amount = float(input("Enter the amount: "))
#         if amount <= 0:
#             print("The amount must be greater than 0.")
#             continue
#         break
#     except ValueError:
#         print("The amount must be a numeric value!")

# # API URL setup using f-string formatting
# url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

# # Headers with API key (replace {API-KEY} with actual API key)
# headers = {
#     "apikey": "{API-KEY}"  # Replace with your actual API key
# }

# # Send the request
# response = requests.get(url, headers=headers)

# # Check response status
# if response.status_code != 200:
#     print("Sorry, there was a problem. Please try again later.")
# else:
#     # Parse JSON and display result
#     result = response.json()
#     print(f"{amount} {init_currency} = {result['result']} {target_currency}")
