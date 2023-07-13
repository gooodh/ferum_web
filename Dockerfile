FROM python:3.10 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code


# Copy project
COPY . /code/

RUN pip install -r requirements.txt




