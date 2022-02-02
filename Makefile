run:
	python pt_proj/manage.py runserver
migrate:
	python pt_proj/manage.py makemigrations
	python pt_proj/manage.py migrate
files:
	python pt_proj/manage.py collectstatic
lint:
	isort --recursive .
	flake8 pt_proj
messages:
	django-admin makemessages -l ru --ignore=static --ignore=media  --ignore=venv
translate:
	django-admin compilemessages --ignore=static --ignore=media  --ignore=venv
