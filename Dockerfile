FROM python:3.10-slim-buster

RUN apt-get update
RUN apt-get install -y  \
    && apt install tzdata -y

ENV TZ="Europe/Dublin"
ENV FLASK_ENV="dev"

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app()"]
