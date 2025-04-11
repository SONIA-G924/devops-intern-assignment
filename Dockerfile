FROM python:3.10-slim

WORKDIR /app
COPY . .

# Install build tools and PostgreSQL client libraries
RUN apt-get update && \
    apt-get install -y gcc libpq-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 5000
CMD ["python", "app.py"]

