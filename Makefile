
requirements-generate:
	@echo "Generate requirements.txt file with hashes."
	poetry export -f requirements.txt --with=test --output requirements.txt

build:
	@echo "Build project with docker."
	docker-compose build

run-with-logs:
	@echo "Running project with docker."
	docker-compose up

run-without-logs:
	@echo "Running project with docker."
	docker-compose up -d

run-without-docker:
	export DEBUG=1
	export DJANGO_ALLOWED_HOSTS="*"
	python3 src/manage.py runserver

.PHONY: test
test:
	@echo "Running tests with pytest."
	pytest -vvv --disable-warnings

makemigrations:
	@echo "Running makemigrations with docker."
	docker-compose exec onidata python3 src/manage.py makemigrations

migrate:
	@echo "Running migrate with docker."
	docker-compose exec onidata python3 src/manage.py migrate

create-super-user:
	@echo "Creating superuser."
	docker-compose exec onidata python3 src/manage.py createsuperuser

itsmine:
	@echo "Itsmine"
	sudo chown -R $USER src

shell:
	@echo "Shell on docker-compose."
	docker-compose exec onidata python3 src/manage.py shell

remove-pycaches:
	@echo "Delete pycaches files."
	find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

close:
	@echo "Down docker-compose containers"
	docker-compose down
