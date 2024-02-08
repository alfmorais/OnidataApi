# API Onidata

- [Descrição detalhada do problema](INSTRUÇÕES.md).

Este projeto foi fortemente inspirado no guia de estilos de desenvolvimento de aplicações em Django do [HackSoftware](https://github.com/HackSoftware/Django-Styleguide), buscando aproveitar ao máximo as facilidades proporcionadas pelo Framework Django/DRF. No entanto, pensando em uma separação clara de responsabilidades, foram criadas duas camadas:

- Serviços: onde ocorre toda a manipulação de informações, cálculos de impostos e demais operações relacionadas à lógica de negócios da aplicação, contidas nos arquivos `services.py`.
- Repositórios: esta camada representa a comunicação com o banco de dados e está contida nos arquivos `repositories.py`. Aqui, todos os dados foram pré-processados pelo serializer/service e estão prontos para criar ou buscar recursos no banco de dados.

As demais camadas seguiram o padrão descrito no Django.

## Descrição do Projeto:

O objetivo deste projeto é simular uma solicitação de empréstimo, onde o usuário pode solicitar um empréstimo através da API, fornecendo informações como valor, juros, número de parcelas, seguro, entre outros dados. Após a criação do empréstimo, o sistema gera automaticamente as transações de pagamento do empréstimo com base no número de parcelas. Todas as transações são criadas com um campo que representa o status do pagamento, inicialmente definido como falso. Esse campo é atualizado para verdadeiro pela API quando o pagamento é efetuado, incluindo o registro da data de pagamento.

Outras APIs têm como objetivo listar empréstimos por usuário, listar pagamentos de empréstimos e fornecer um extrato detalhado do empréstimo.

## Requisitos do Sistema:

- Poetry (versão 1.7.1)
- Docker (versão 25.0.2, build 29cf629)
- Docker Compose (versão v2.24.3-desktop.1)

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

## Executando os testes do projeto:

Para executar os testes unitários e de integração do projeto, basta utilizar o seguinte comando:

```bash
make test
```

OBS: Certifique-se de que os testes estão sendo executados fora do container Docker e que o seu ambiente virtual está ativado.

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

## Rodando o sistema:

Para rodar o sistema com o docker compose:

```bash
make run-with-logs
```

Para rodar o sistema com Poetry ou Virtualenv

```bash
python3 src/manage.py runserver 0.0.0.0:8000
```

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

## Criando um Token de Autenticação:

Para criar um token de autenticação, faça uma chamada HTTP para o endpoint POST `api-token-auth/` com as credenciais de usuário criadas no passo anterior.

OBS: O Endpoint POST `api-token-auth/` não requer autenticação. No entanto, todas os outros endpoints requerem o parâmetro Authorization no cabeçalho da requisição HTTP.

## Melhorias Implementas:

- Declaração da quantidade de parcelas que o cliente pode solicitar.
- Criação automática dos pagamentos, ficando apenas a critério da atualização quando o pagamento for efetuado.
- Cálculo de Juros Compostos no momento da contratação do empréstimo.
- Cálculo do Custo Efetivo Total.
- Cálculo do Imposto Sobre Operações Financeiras seguindo as regulamentações vigentes.
- Desacoplamento da lógica de negócio do Framework Django.

## Melhorias Previstas:

- Execução dos testes com Docker Compose.
- Implementação da funcionalidade de cálculo de juros compostos pro-rata dia.
- Implementação da funcionalidade de quitação antecipada do empréstimo.
- Documentação no Swagger.
- Alteração das variáveis de ambiente para um arquivo .env e configuração no settings.py.
- Planejamento de uma esteira de CI/CD no Gitbuckets.

## Considerações Finais:

Agradeço pela oportunidade de participar do processo de seleção da Matera/Onidata. Espero sinceramente poder fazer parte desta equipe.

Muito obrigado,

Alfredo de Morais

- [Github](https://github.com/alfmorais/)
- [Linkedin](https://www.linkedin.com/in/alfredomneto/)
