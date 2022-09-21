FROM python:3.11-rc-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt


RUN mkdir /app/db

VOLUME ["/app/db"]

EXPOSE 8000

COPY . /app/

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]