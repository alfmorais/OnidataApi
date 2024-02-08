# Comandos Makefile

### Comando para gerar o arquivo requirements.txt com todos os hashes do Poetry.
```Makefile
requirements-generate:
	@echo "Generate requirements.txt file with hashes."
	poetry export -f requirements.txt --with=test --output requirements.txt
```

### Comando para build do projeto com o Docker Compose.
```Makefile
build:
	@echo "Build project with docker."
	docker-compose build
```

### Comando para subir os containers da aplicação com o Docker Compose com os Logs.
```Makefile
run-with-logs:
	@echo "Running project with docker."
	docker-compose up
```

### Comando para subir os container da aplicação com o Docker Compose sem os Logs.
```Makefile
run-without-logs:
	@echo "Running project with docker."
	docker-compose up -d
```

### Comando para rodar a aplicação sem o Docker Compose.
```Makefile
run-without-docker:
	export DEBUG=1
	export DJANGO_ALLOWED_HOSTS="*"
	python3 src/manage.py runserver
```

### Comando para o rodar os testes unitários e de integração com estão dentro da aplicação.
```Makefile
.PHONY: test
test:
	@echo "Running tests with pytest."
	pytest -vvv --disable-warnings
```

### Comando para gerar os arquivos de alteração do Banco de Dados pelo Docker Compose.
```Makefile
makemigrations:
	@echo "Running makemigrations with docker."
	docker-compose run onidata python3 src/manage.py makemigrations
```

### Comando para informar o banco de dados que houve uma alteração no Schema pelo Docker Compose.
```Makefile
migrate:
	@echo "Running migrate with docker."
	docker-compose run onidata python3 src/manage.py migrate
```

### Comando para criar um Super Usuário Django pelo Docker Compose.
```Makefile
create-super-user:
	@echo "Creating superuser."
	docker-compose run onidata python3 src/manage.py createsuperuser
```

### Comando para informar a aplicação que nos podemos alterar os arquivos de migration.
```Makefile
itsmine:
	@echo "Itsmine"
	sudo chown -R $USER src
```

### Comando para entrar no terminal do container da aplicação.
```Makefile
shell:
	@echo "Shell on docker-compose."
	docker-compose run onidata python3 src/manage.py shell
```

### Comando para deletar arquivos de pycache.
```Makefile
remove-pycaches:
	@echo "Delete pycaches files."
	find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
```

### Comando para fechar ou baixar os containers do Docker Compose.
```Makefile
close:
	@echo "Down docker-compose containers"
	docker-compose down
```