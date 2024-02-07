# API Onidata

- [Descrição detalhada do problema](INTRUÇÕES.md).

Esse projeto foi inspirado fortemente na guida de estilos de desenvolvimento de aplicações em Django - [HackSoftware](https://github.com/HackSoftware/Django-Styleguide).
Onde foi tentado ao máximo aproveitar as facilidades que o Framework Django / DRF provém. Porém pensando em uma camada de separação de responsabilidades, foi criado duas camadas:

- Serviços: Onde toda a manipulação de informações dados, cálculos de impostos, cálculos em gerais da aplicações estão nos arquivos `services.py`
- Repositórios: A camada que representa a comunicação com o banco de dados estão no arquivos `repositories.py`. Nessa camada todos os dados foram pré-tradados pelo serializer / service e estão pronto para Criar, Atualizar, Solicitar informações do Banco de Dados.

Outras camadas seguiu padrão que está descrito no Django.

## Requisitos do Sistema:

- Poetry (version 1.7.1)
- Docker version 25.0.2, build 29cf629
- Docker Compose version v2.24.3-desktop.1

## Instalando as depedências do Sistema:

Você pode usar rodar o sistema de 3 maneiras possiveis: 

- Rodando o sistema com o docker-compose:

```bash
make build-run-project
```

- Rodando o sistema com virtualenv:

```bash
pip install -r requirements.txt && python3 src/manage.py runserver
```

- Rodando o sistema com Poetry:

```bash
poetry install && poetry shell && python3 src/manage.py runserver
```

## Rodando os testes do projeto:

Para rodar os testes unitários e de integração no projeto basta rodar o comando:

```bash
make test
```

## Testando o sistema:

Na pasta `docs` possui dois arquivos:

1. [Instruções Detalhadas das Requisições HTTP na API](docs/Endpoints.md)
1. [Coleção em JSON do Postman, considerando todos os endpoints](docs/OnidataApi.postman_collection.json)


## Criando um SUPER USÚARIO:

Para criar um super usúario do Django basta rodar o comando e seguir os passos do terminal:

```bash
make create-super-user
```

## Criando um Token de Autenticação:

Para criar um token de autenticação basta fazer uma chamada HTTP para a API `api-token-auth/` com seus dados de usúarios criado no passo anterior.

OBS:
- API `api-token-auth/` não possui autenticação
- Todas as outras APIs são necessários receber o parâmetro `Authorization` no headers da requisição HTTP.

## Melhorias Previstas:

- Rodar os testes com docker-compose.
- Implementar a funcionalidade de cálculo de juros compostos `pro-rata dia`.
- Implementar a funcionalidade de quitação antecipada do empréstimo.
- Documentação em Swagger.
- Alterar as variaveis de ambiente para um arquivo `.env`
- Planejar uma esteira de CI/CD no gitbuckets.

## Considerações Finais:

Obrigado pela oportunidade de participar do processo de seleção da Matera / Onidata. Espero muito poder fazer parte dessa equipe.

Muito Obrigado
Alfredo de Morais

- [Github](https://github.com/alfmorais/)
- [Linkedin](https://www.linkedin.com/in/alfredomneto/)
