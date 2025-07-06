from typing import Union, Dict

GenericsSchema = Dict[str, Union[float,int, bool]]

TransactionSchema: GenericsSchema = {
    "client_id": int,
    "credit_card": str,
    "store_name": str,
    "id_transaction": int,
    "transaction_type": str,
    "amount": float,
    "fraudulent": bool,
    "dateTime": str,
    "client_position": str,
} #type: ignore