import pandas as pd

df = pd.read_csv("Task4a_data.csv")


def convert_gbp_to_usd(amount_local):
    rate = df["GBP - USD"][0]
    amount_usd = amount_local * rate
    return round(amount_usd, 2)


# Add function below to convert USD to GBP
def convert_usd_to_gbp(amount_local):
    rate = df["USD - GBP"][0]
    amount_gbp = amount_local * rate
    return round(amount_gbp, 2)


def convert_gbp_to_eur(amount_local):
    rate = df["GBP - EUR"][0]
    amount_eur = amount_local * rate
    return round(amount_eur, 2)


def convert_eur_to_gbp(amount_local):
    rate = df["EUR - GBP"][0]
    amount_gbp = amount_local * rate
    return round(amount_gbp, 2)


amount = float(input("Enter amount in GBP: "))
print(convert_usd_to_gbp(amount))

amount = float(input("Enter amount in USD: "))
print(convert_gbp_to_usd(amount))

amount = float(input("Enter your amount in GBP: "))
print(convert_gbp_to_eur(amount))

amount = float(input("Enter amount in EUR: "))
print(convert_eur_to_gbp(amount))
