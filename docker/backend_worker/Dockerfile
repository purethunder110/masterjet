FROM python:3.12

RUN apt-get -y update \
    && apt-get install -y nano \
    && apt-get install -y python3-setuptools \
    && apt-get clean \
    && rm -rf  /var/lib/apt/lists/*

COPY . /app
 
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000
ENV PYTHONUNBUFFERED 1


CMD ["python","manage.py","runserver"]
