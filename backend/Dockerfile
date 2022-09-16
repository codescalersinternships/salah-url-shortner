FROM python:buster

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

RUN mkdir /app/db

VOLUME ["/app/db"]

EXPOSE 8000

CMD [ "python", "manage.py", "runserver"]