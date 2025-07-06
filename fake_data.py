import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_fake_transactions(num_transactions=500):
    transactions = []
    for _ in range(num_transactions):
        idTransactions = fake.random_int(min=100000, max=999999)
        transactionType = random.choice(["CASH-IN", "CASH-OUT", "DEBIT", "PAYMENT", "TRANSFER"]),
        amount = round(fake.random_number(digits=5, fix_len=True) / 100, 2)
        fraudulent = fake.boolean(chance_of_getting_true=5)
        transactions.append({
            "idTransactions": idTransactions,
            "transactionType": transactionType[0],  # Unpack the tuple
            "amount": amount,
            "fraudulent": fraudulent,
        })
    return pd.DataFrame(transactions)

if __name__ == "__main__":
    df_transactions = generate_fake_transactions()
    df_transactions.to_csv("backend/api/transactions.csv", index=False)
    print("Generated transactions.csv with 500 fake transactions.")
