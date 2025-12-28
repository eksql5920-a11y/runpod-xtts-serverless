FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY serverless ./serverless

CMD ["python", "serverless/xtts_handler.py"]
