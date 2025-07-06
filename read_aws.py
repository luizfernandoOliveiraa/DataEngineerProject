import pandas as pd

url ="https://luizoliveiraestudoss3.s3.us-east-1.amazonaws.com/api/api-response-compra2025-07-06T13%3A58%3A03.parquet"

df = pd.read_parquet(url)
print(df.head(5))