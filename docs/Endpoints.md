# Lista de Endpoints do Projeto Onidata

## POST: api-token-auth/ -> Criar um token de autenticação

Requisição:

```curl
curl --location 'http://127.0.0.1:8000/api-token-auth/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "joaquim",
    "password": "1"
}'
```

Resposta:

```json
{
  "token": "98904c5ffbdff622a424d4b997a00417655aa5e2"
}
```

## POST: v1/loans/ -> Criar um Empréstimo

Requisição:

```curl
curl --location 'http://127.0.0.1:8000/v1/loans/' \
--header 'Authorization: Token 98904c5ffbdff622a424d4b997a00417655aa5e2' \
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
    "id": "98a71b4e-962b-4105-a2e4-2ec329122338",
    "amount": "5000.00",
    "interest_rate": "1.10",
    "ip_address": "172.27.74.161",
    "date": "2024-02-08T00:37:53.965698Z",
    "bank": "Nu Pagamentos SA",
    "customer": 1,
    "installments": 3,
    "cet_amount": "5483.86",
    "iof_interest_rate": "55.90",
    "insurance": "5.00"
  }
}
```

## GET: v1/loans/ -> Listar todos os Empréstimos

Requisição:

```curl
curl --location 'http://0.0.0.0:8000/v1/loans/' \
--header 'Authorization: Token 98904c5ffbdff622a424d4b997a00417655aa5e2'
```

Resposta:

```json
{
  "data": [
    {
      "id": "98a71b4e-962b-4105-a2e4-2ec329122338",
      "amount": "5000.00",
      "interest_rate": "1.10",
      "ip_address": "172.27.74.161",
      "date": "2024-02-08T00:37:53.965698Z",
      "bank": "Nu Pagamentos SA",
      "customer": 1,
      "installments": 3,
      "cet_amount": "5483.86",
      "iof_interest_rate": "55.90",
      "insurance": "5.00"
    }
  ]
}
```

## GET: v1/payments/:loan_uuid/ -> Listar todos os Pagamentos por Empréstimo

Requisição:

```curl
curl --location 'http://0.0.0.0:8000/v1/payments/98a71b4e-962b-4105-a2e4-2ec329122338/' \
--header 'Authorization: Token 98904c5ffbdff622a424d4b997a00417655aa5e2'
```

Resposta:

```json
{
  "data": [
    {
      "id": "f2d49a63-fc5c-4b12-bb3f-b25cd4502315",
      "loan": "98a71b4e-962b-4105-a2e4-2ec329122338",
      "installment_amount": "1827.95",
      "installment_number": 1,
      "date": null,
      "is_paid": false
    },
    {
      "id": "05564d3d-4735-4bc9-b210-5aefd562d2d5",
      "loan": "98a71b4e-962b-4105-a2e4-2ec329122338",
      "installment_amount": "1827.95",
      "installment_number": 2,
      "date": null,
      "is_paid": false
    },
    {
      "id": "f8ef45c9-5683-438e-9f97-08a7630f6279",
      "loan": "98a71b4e-962b-4105-a2e4-2ec329122338",
      "installment_amount": "1827.95",
      "installment_number": 3,
      "date": null,
      "is_paid": false
    }
  ]
}
```

## GET: v1/payments/:loan_uuid/balance/-> Listar o saldo devedor por Empréstimo

Requisição:

```curl
curl --location 'http://0.0.0.0:8000/v1/payments/98a71b4e-962b-4105-a2e4-2ec329122338/balance/' \
--header 'Authorization: Token 98904c5ffbdff622a424d4b997a00417655aa5e2'
```

Resposta:

```json
{
  "data": {
    "loan_id": "98a71b4e-962b-4105-a2e4-2ec329122338",
    "installments_paid": 1,
    "installments_missing_payment": 2,
    "total_installments": 3,
    "amount_paid": "1827.95",
    "amount_missing_payment": "3655.90"
  }
}
```

## PUT: v1/payments/ -> Atualizar uma cobrança de Pagamento

Requisição:

```curl
curl --location --request PUT 'http://0.0.0.0:8000/v1/payments/' \
--header 'Authorization: Token 98904c5ffbdff622a424d4b997a00417655aa5e2' \
--header 'Content-Type: application/json' \
--data '{
    "id": "f2d49a63-fc5c-4b12-bb3f-b25cd4502315",
    "is_paid": true
}'
```

Resposta:

```json
{
  "data": {
    "id": "f2d49a63-fc5c-4b12-bb3f-b25cd4502315",
    "loan": "98a71b4e-962b-4105-a2e4-2ec329122338",
    "installment_amount": "1827.95",
    "installment_number": 1,
    "date": "2024-02-08T00:38:33.009005Z",
    "is_paid": true
  }
}
```
