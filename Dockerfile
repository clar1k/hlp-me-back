FROM python:3.11.3-slim


WORKDIR /app
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app

RUN apt-get clean

CMD uvicorn main:app --port=8000 --host=0.0.0.0