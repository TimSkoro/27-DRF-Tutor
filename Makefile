run:
	python manage.py runserver
migrate:
	python manage.py makemigrations
	python manage.py migrate
install:
	pip install -r requirements.txt
fast_start:
	sudo docker build -t django_demo .
	sudo docker run -p 8000:8000 django_demo
