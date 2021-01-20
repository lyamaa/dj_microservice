FROM python:3.8.5
ENV PYTHONUNBUFFERED 1

WORKDIR /src
COPY requirements.txt /src/requirements.txt

RUN pip install -r requirements.txt
COPY . /src

CMD python manage.py runserver 0.0.0.0:8000

