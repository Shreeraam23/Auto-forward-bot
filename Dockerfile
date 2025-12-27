# Op Dockerfile
FROM python:3.10.4-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "angel.py"]
