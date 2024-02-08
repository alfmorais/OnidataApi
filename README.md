# API Onidata

- [Descrição detalhada do problema](INSTRUÇÕES.md).

Este projeto foi fortemente inspirado no guia de estilos de desenvolvimento de aplicações em Django do [HackSoftware](https://github.com/HackSoftware/Django-Styleguide), buscando aproveitar ao máximo as facilidades proporcionadas pelo Framework Django/DRF. No entanto, pensando em uma separação clara de responsabilidades, foram criadas duas camadas:

- Serviços: onde ocorre toda a manipulação de informações, cálculos de impostos e demais operações relacionadas à lógica de negócios da aplicação, contidas nos arquivos `services.py`.
- Repositórios: esta camada representa a comunicação com o banco de dados e está contida nos arquivos `repositories.py`. Aqui, todos os dados foram pré-processados pelo serializer/service e estão prontos para criar ou buscar recursos no banco de dados.

As demais camadas seguiram o padrão descrito no Django.

## Sumário

1. [Descrição do Projeto](#1)
2. [Requisitos do Sistema](#2)
3. [Alteração do arquivo .env](#3)
4. [Instalando as dependências do Sistema](#4)
5. [Rodando as migrações do Banco de Dados](#5)
6. [Executando os testes do projeto](#6)
7. [Criando um Super Usuário / Admin](#7)
8. [Rodando o sistema](#8)
9. [Testando o sistema](#9)
10. [Criando um Token de Autenticação](#10)
11. [Melhorias Implementadas](#11)
12. [Melhorias Previstas](#12)
13. [Considerações Finais](#13)


<div id='1'/>

## Descrição do Projeto:

O objetivo deste projeto é simular uma solicitação de empréstimo, onde o usuário pode solicitar um empréstimo através da API, fornecendo informações como valor, juros, número de parcelas, seguro, entre outros dados. Após a criação do empréstimo, o sistema gera automaticamente as transações de pagamento do empréstimo com base no número de parcelas. Todas as transações são criadas com um campo que representa o status do pagamento, inicialmente definido como falso. Esse campo é atualizado para verdadeiro pela API quando o pagamento é efetuado, incluindo o registro da data de pagamento.

Outras APIs têm como objetivo listar empréstimos por usuário, listar pagamentos de empréstimos e fornecer um extrato detalhado do empréstimo.

<div id='2'/>

## Requisitos do Sistema:

- Poetry (versão 1.7.1)
- Docker (versão 25.0.2, build 29cf629)
- Docker Compose (versão v2.24.3-desktop.1)

OBS: Caso os comandos com docker não funcionar, verifique a compatibilidade no arquivo Makefile. Ao invés de: docker-compose <comando> use docker compose <comando>.

<div id='3'/>

## Alteração do arquivo .env

Altera o nome do arquivo `.env.example` para `.env`

<div id='4'/>

## Instalando as dependências do Sistema:

Você pode executar o sistema de três maneiras possíveis:

- Rodando o sistema com Docker Compose:

```bash
make build
```

- Rodando o sistema com virtualenv:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Rodando o sistema com Poetry:

```bash
poetry install
poetry shell
```

<div id='5'/>

## Rodando as migrações do Banco de Dados:

- Rodando pelo Docker Compose:

```bash
make makemigrations
make migrate
```

- Rodando pelo Poetry e Virtualenv

```bash
python3 src/manage.py makemigrations
python3 src/manage.py migrate
```

<div id='6'/>

## Executando os testes do projeto:

Para executar os testes unitários e de integração do projeto, basta utilizar o seguinte comando:

```bash
make test
```

OBS: Certifique-se de que os testes estão sendo executados fora do container Docker e que o seu ambiente virtual está ativado.

<div id='7'/>

## Criando um Super Usuário / Admin:

Para criar um super usuário no Django, execute o seguinte comando e siga as instruções no terminal:

- Rodando pelo Docker Compose:

```bash
make create-super-user
```

OBS: Com esse usuário será possivel acessar o Painel Administrativo.

- Rodando pelo Poetry e Virtualenv

```bash
python3 src/manage.py createsuperuser
```

<div id='8'/>

## Rodando o sistema:

Para rodar o sistema com o docker compose:

```bash
make run-with-logs
```

Para rodar o sistema com Poetry ou Virtualenv

```bash
python3 src/manage.py runserver 0.0.0.0:8000
```

<div id='9'/>

## Testando o sistema:

Endpoints:

- **Auth**: POST `api-token-auth/` - Criar um token de autenticação
- **Loans**: GET `v1/loans/` - Listar todos os Empréstimos
- **Loans**: GET `v1/loans/` - Criar um Empréstimo
- **Payments**: PUT `v1/payments/` - Atualizar uma cobrança de Pagamento
- **Payments**: GET `v1/payments/:loan_uuid/` - Listar todos os Pagamentos por Empréstimo
- **Payments**: GET `v1/payments/:loan_uuid/balance/` - Listar o saldo devedor por Empréstimo

Na pasta `docs`, você encontrará dois arquivos:

1. [Instruções Detalhadas das Requisições HTTP na API](docs/Endpoints.md)
1. [Coleção em JSON do Postman, considerando todos os endpoints](docs/OnidataApi.postman_collection.json)

<div id='10'/>

## Criando um Token de Autenticação:

Para criar um token de autenticação, faça uma chamada HTTP para o endpoint POST `api-token-auth/` com as credenciais de usuário (body json com as chaves `username`, `password` e seus respectivos valores. Para exemplo completo veja a [documentação das chamadas dos Endpoints](docs/Endpoints.md)) criadas no passo anterior.

OBS: O Endpoint POST `api-token-auth/` não requer autenticação. No entanto, todas os outros endpoints requerem o parâmetro Authorization no cabeçalho da requisição HTTP.

<div id='11'/>

## Melhorias Implementadas:

- Declaração da quantidade de parcelas que o cliente pode solicitar.
- Criação automática dos pagamentos, ficando apenas a critério da atualização quando o pagamento for efetuado.
- Cálculo de Juros Compostos no momento da contratação do empréstimo.
- Cálculo do Custo Efetivo Total.
- Cálculo do Imposto Sobre Operações Financeiras seguindo as regulamentações vigentes.
- Desacoplamento da lógica de negócio do Framework Django.

<div id='12'/>

## Melhorias Previstas:

- Execução dos testes com Docker Compose.
- Implementação da funcionalidade de cálculo de juros compostos pro-rata dia.
- Implementação da funcionalidade de quitação antecipada do empréstimo.
- Implementação da conclusão de pagamento do empréstimo.
- Documentação no Swagger.
- Alteração das variáveis de ambiente para um arquivo .env e configuração no settings.py.
- Planejamento de uma esteira de CI/CD no Gitbuckets.

<div id='13'/>

## Considerações Finais:

Agradeço pela oportunidade de participar do processo de seleção da Matera/Onidata. Espero sinceramente poder fazer parte desta equipe.

Muito obrigado,

Alfredo de Morais

- [Github](https://github.com/alfmorais/)
- [Linkedin](https://www.linkedin.com/in/alfredomneto/)
