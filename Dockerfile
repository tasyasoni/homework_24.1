FROM python:3

WORKDIR /Online_lessons_Docker

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .