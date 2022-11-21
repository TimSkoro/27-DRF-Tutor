FROM python:3.8-slim
ENV SECRET_KEY="hello_group_27"
WORKDIR drf_tutpor/
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python drf_tutpor/manage.py migrate
CMD python manage.py collectstatic --noinput
CMD python manage.py runserver 0.0.0.0:8000 --noreload