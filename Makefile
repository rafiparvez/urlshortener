.PHONY: build rebuild migrate run

build:
	docker-compose build
rebuild:
	docker-compose build --force-rm --no-cache
run:
	docker-compose up -d --build
migrate:
	docker-compose exec web python manage.py migrate --noinput
