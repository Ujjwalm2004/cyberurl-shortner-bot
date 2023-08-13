FROM python:3.8-slim-buster

WORKDIR /cyberurl-shortner-bot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]
