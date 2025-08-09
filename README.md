# 🏦 Projeto ETL de transações Financeiras

Este projeto simula uma API e uma ETL (Extração, Transformação e Carga)** para dados de transações financeiras. Ele foi desenvolvido com foco em gerar dados de forma automatica via api com o **FastAPI** e **Faker**, tratar os dados e transforma-los em formato **Parquet** visando diminuir o custo de armazenamento e processamento de dados, utilizar a biblioteca **boto3** para fazer a conexão com a **AWS** e enviar os dados para o Lake no **S3**.

---

## 📌 Visão Geral

O projeto é dividido em duas partes principais:

### 1. 🔧 API Geradora de Dados

Desenvolvida com **FastAPI**, a API permite a geração de dados sintéticos que representam transações financeiras. Cada transação contém:

- ID do cliente  
- Número de cartão de crédito (fictício)  
- Loja (fictícia)  
- ID da transação  
- Tipo da transação  
- Valor da transação  
- Indicador de transação fraudulenta (True/False)
- Data e hora da transação  


### 2. 🔄 ETL

Um script Python que:

- Consome dados da API  
- Valida os dados conforme um schema padrão  
- Realiza transformações simples (se necessário)  
- Armazena os dados em **arquivos Parquet** no **Amazon S3**

---

## ⚙️ Pré-Requisitos

- Python 3.12+  
- Conta AWS com credenciais válidas  
- Bucket criado na AWS S3

---

## 🚀 Como Executar o Projeto

### 1. Clone o Repositório

```bash
1.  git clone <https://github.com/luizfernandoOliveiraa/DataEngineerProject.git>
    cd DataEngineerProject
```

### 2. Instalar Dependências com Poetry
```bash
poetry install
```
### 3. Ative o Ambiente Virtual
```bash
poetry shell
```

### 4. Configure as Credenciais AWS

```bash
Recomenda-se criar um arquivo .env na raiz do projeto com o seguinte conteúdo:

AWS\ACCESS_KEY\ID = Sua Acess Key da AWS
AWS\SECRET\ACCESSKEY = Sua Secret Key da AWS
AWS\REGION = Região do serviço S3 na AWS
AWS\BUCKET\NAME = Bucket na AWS
DELTA_LAKE_S3_PATH = Path do Lake no S3

```

### 5. Inicie o Servidor FastAPI (Gerador de Dados)
```bash
No shell do poetry execute: uvicorn backend.api.extract:app --reload
A API estará disponível em: http://127.0.0.1:8000
```

### 6. Execute a Pipeline ETL
```
Em outro terminal, com o ambiente virtual ainda ativo:

python backend/app.py
```
#### Esse script irá:
    - Coletar 30 transações geradas pela API
    - Validá-las conforme o schema
    - Salvar os dados no S3 em formato .parquet
Você verá logs no console indicando sucesso ou falhas.



### 🗂️ Estrutura do Projeto (Opcional)
```
DwProject/

DwProject/
├── backend/
│   ├── api/
│   │   └── extract.py      # FastAPI para gerar dados
│   ├── app.py              # Script ETL
│   ├── schema.py           # Schema de validação dos dados
│   └── s3_utils.py         # Funções auxiliares para salvar no S3
├── .env                    # Variáveis de ambiente (não versionar)
├── pyproject.toml          # Dependências gerenciadas pelo Poetry
└── README.md
```
### 📦 Tecnologias Utilizadas

    FastAPI
    Faker
    Boto3
    Pandas
    Uvicorn
    Poetry

