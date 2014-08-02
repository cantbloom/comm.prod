.PHONY: default, clean, webserver, pull, syntax, test, lint

BASE = $(shell pwd)/conf

ifndef WEBSERVER_PORT
	WEBSERVER_PORT=8000
endif

default: webserver

clean:
	find . -type f -name '*.pyc' -delete

webserver: clean
	python manage.py runserver 0.0.0.0:$(WEBSERVER_PORT)

pull:
	git pull
	pip install -r requirements.txt
	./manage.py collectstatic --noinput
	./manage.py syncdb

syntax:
	find . -name "*.pyc" | xargs -n1 rm -f
	python -mcompileall . && echo "Congrats - No syntax error detected :)"

test:
	./manage.py test

lint:
	flake8 --exclude=venv/* .
