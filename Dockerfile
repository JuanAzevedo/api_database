FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Cria a pasta "instance"
RUN mkdir -p /app/instance

EXPOSE 5001

CMD ["python", "app.py"]
