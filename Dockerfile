FROM python:3.12.7-slim
LABEL authors="milosz7"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0"]