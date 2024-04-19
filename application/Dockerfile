
FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY model/model.pkl model/model.pkl


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]