# Lista de Endpoints do Projeto Onidata

## POST: v1/loans/ -> Criar um Empréstimo

Requisição:
```curl
curl --location 'http://0.0.0.0:8000/v1/loans/' \
--header 'Authorization: Token 04626463b3ccdf17684b58db4a57b225377639dc' \
--header 'Content-Type: application/json' \
--data '{
    "amount": 5000.00,
    "interest_rate": 1.1,
    "ip_address": "172.27.74.161",
    "bank": "Nu Pagamentos SA",
    "installments": 3,
    "insurance": 5.0
}'
```

Resposta:
```json
{
    "data": {
        "id": "f8b2443f-a474-462e-9eb2-f38e1e7f854d",
        "amount": "5000.00",
        "interest_rate": "1.10",
        "ip_address": "172.27.74.161",
        "date": "2024-02-06T23:13:57.747016Z",
        "bank": "Nu Pagamentos SA",
        "customer": 1,
        "installments": 3,
        "cet_amount": "7577.66",
        "iof_interest_rate": "2050.00",
        "insurance": "5.00"
    }
}
```

## GET: v1/loans/ -> Listar todos os Empréstimos

Requisição:
```curl
curl --location 'http://0.0.0.0:8000/v1/loans/' \
--header 'Authorization: Token 04626463b3ccdf17684b58db4a57b225377639dc'
```

Resposta:
```json
{
    "data": [
        {
            "id": "2b0816bd-3744-4c53-a3e4-ba4f1161c2f9",
            "amount": "10000.00",
            "interest_rate": "1.10",
            "ip_address": "172.27.74.161",
            "date": "2024-02-06T21:07:29.901394Z",
            "bank": "Nu Pagamentos SA",
            "customer": 1,
            "installments": 10,
            "cet_amount": "16018.88",
            "iof_interest_rate": "4100.00",
            "insurance": "5.00"
        },
        {
            "id": "f8b2443f-a474-462e-9eb2-f38e1e7f854d",
            "amount": "5000.00",
            "interest_rate": "1.10",
            "ip_address": "172.27.74.161",
            "date": "2024-02-06T23:13:57.747016Z",
            "bank": "Nu Pagamentos SA",
            "customer": 1,
            "installments": 3,
            "cet_amount": "7577.66",
            "iof_interest_rate": "2050.00",
            "insurance": "5.00"
        }
    ]
}
```

## POST: api-token-auth/ -> Criar um token de autenticação

Requisição:
```curl
curl --location 'http://0.0.0.0:8000/api-token-auth/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "alfredo",
    "password": "1"
}'
```

Resposta:
```json
{
    "token": "04626463b3ccdf17684b58db4a57b225377639dc"
}
```

## GET: v1/payments/:loan_uuid/ -> Listar todos os Pagamentos por Empréstimo

Requisição:
```curl
curl --location 'http://0.0.0.0:8000/v1/payments/f8b2443f-a474-462e-9eb2-f38e1e7f854d/' \
--header 'Authorization: Token 04626463b3ccdf17684b58db4a57b225377639dc'
```

Resposta:
```json
{
    "data": [
        {
            "id": "3838f699-a7f3-4ccc-8cdd-ddbb56c68989",
            "loan": "f8b2443f-a474-462e-9eb2-f38e1e7f854d",
            "installment_amount": "2525.89",
            "installment_number": 1,
            "date": null,
            "is_paid": false
        },
        {
            "id": "d469b4d9-efb2-4b9d-bc9a-933ab3ddc880",
            "loan": "f8b2443f-a474-462e-9eb2-f38e1e7f854d",
            "installment_amount": "2525.89",
            "installment_number": 2,
            "date": null,
            "is_paid": false
        },
        {
            "id": "9590d27f-eafa-461f-90e8-bebff3e73bd1",
            "loan": "f8b2443f-a474-462e-9eb2-f38e1e7f854d",
            "installment_amount": "2525.89",
            "installment_number": 3,
            "date": null,
            "is_paid": false
        }
    ]
}
```

## GET: v1/payments/ -> Atualizar uma cobrança de Pagamento

Requisição:
```curl
curl --location --request PUT 'http://0.0.0.0:8000/v1/payments/' \
--header 'Authorization: Token 04626463b3ccdf17684b58db4a57b225377639dc' \
--header 'Content-Type: application/json' \
--data '{
    "id": "3838f699-a7f3-4ccc-8cdd-ddbb56c68989",
    "is_paid": true
}'
```

Resposta:
```json
{
    "data": {
        "id": "3838f699-a7f3-4ccc-8cdd-ddbb56c68989",
        "loan": "f8b2443f-a474-462e-9eb2-f38e1e7f854d",
        "installment_amount": "2525.89",
        "installment_number": 1,
        "date": "2024-02-06T23:18:40.309638Z",
        "is_paid": true
    }
}
```

## GET: v1/payments/:loan_uuid/balance/-> Listar o saldo devedor por Empréstimo

Requisição:
```curl
curl --location 'http://0.0.0.0:8000/v1/payments/f8b2443f-a474-462e-9eb2-f38e1e7f854d/balance/' \
--header 'Authorization: Token 04626463b3ccdf17684b58db4a57b225377639dc'
```

Resposta:
```json
{
    "data": {
        "loan_id": "f8b2443f-a474-462e-9eb2-f38e1e7f854d",
        "installments_paid": 1,
        "installments_missing_payment": 2,
        "total_installments": 3,
        "amount_paid": "2525.89",
        "amount_missing_payment": "5051.78"
    }
}
```
