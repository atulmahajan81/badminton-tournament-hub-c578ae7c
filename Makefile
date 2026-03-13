dev:
	docker-compose up --build

test:
	pytest

deploy:
	./scripts/deploy.sh

migrate:
	./scripts/migrate.sh