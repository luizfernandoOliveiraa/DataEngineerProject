from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random
import pathlib

app = FastAPI()
fake = Faker()

file_path = pathlib.Path(__file__).parent / "transactions.csv"

try:
    df = pd.read_csv(file_path)
    df['index'] = range(1, len(df) + 1)
    df.set_index('index', inplace=True)
except FileNotFoundError:
    raise RuntimeError(
        f"Arquivo de dados '{file_path}' não encontrado. "
        "Execute 'task gen-data' para criá-lo."
    ) from None

@app.get("/gerar_transaction")
async def gerar_transcation():
    index = random.randint(1, len(df)-1)
    tuple = df.iloc[index]
    return {
        "client_id": fake.random_int(min=100000, max=999999),
        "credit_card": fake.credit_card_provider(),
        "store_name": fake.company(),
        "id_transaction": int(tuple["idTransactions"]),
        "transaction_type": str(tuple["idTransactions"]),
        "amount": round(float(tuple["amount"]), 2),
        "fraudulent": bool(tuple["fraudulent"]),
        "dateTime": fake.iso8601(),
        "client_position": str(fake.location_on_land()),
    }

@app.get("/gerar_transaction/{numero_registro}")
async def gerar_transaction(numero_registro: int):
    
    if numero_registro < 1:
        return {"error": "O número de registro deve ser maior que 1"} 
    
    transactions = []
    for _ in range(numero_registro):
        index = random.randint(1, len(df)-1)
        tuple = df.iloc[index]
        
        transaction = {
        "client_id": fake.random_int(min=100000, max=999999),
        "credit_card": fake.credit_card_provider(),
        "store_name": fake.company(),
        "id_transaction": int(tuple["idTransactions"]),
        "transaction_type": str(tuple["idTransactions"]),
        "amount": round(float(tuple["amount"]), 2),
        "fraudulent": bool(tuple["fraudulent"]),
        "dateTime": fake.iso8601(),
        "client_position": str(fake.location_on_land()),
    }
        
        transactions.append(transaction)
    return transactions