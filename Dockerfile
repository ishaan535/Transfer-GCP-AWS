FROM python:3.10-slim

WORKDIR /app

COPY transfer.py .
COPY requirements.txt .
COPY peerless-column-367317-cf4d7beb576d.json .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "transfer.py"]
