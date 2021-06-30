FROM python:3

WORKDIR /flask-app

COPY API.py .
COPY books.csv .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "API.py" ]

EXPOSE 5000