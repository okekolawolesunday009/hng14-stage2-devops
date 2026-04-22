FROM python:3.11

WORKDIR /app

COPY requirements.txt .
pip install --no-cache-dir requirements.txt
COPY . .

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD wget --no-verbose --tries=1 --spider http://localhost:6379/ || exit 1
CMD ["python", "worker.py"]