from data_source.api import APICollector
from contracts.schema import TransactionSchema
from aws.client import S3Client

schema = TransactionSchema
aws = S3Client()

minha_classe = APICollector(schema,aws).start(30,"http://127.0.0.1:8000/gerar_transaction")

print(minha_classe)
