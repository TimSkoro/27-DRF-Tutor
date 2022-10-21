run:
	python manage.py runserver
migrate:
	python manage.py makemigrations
	python manage.py migrate
install:
	pip install -r requirements.txt
